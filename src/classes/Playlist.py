from PySide6.QtWidgets import QFileDialog

from src.classes.JSON import JSON
from src.components.track_card import TrackCard
from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash


class Playlist:
    def __init__(self, audio_player, main):
        super().__init__()
        self.audio_player = audio_player
        self.main = main

    # переменные
        self.db = self.audio_player.db
        self._cards_cache = {}  # {хэш: TrackCard}

    # обработчики
        self.main.addTrackButton.clicked.connect(self.add_track)

    # первый рендер
        self.render_card_list()


    def toggle_play(self, track_hash: str):
        # выбранный трек - текущий?
        if self.audio_player.current_track and self.audio_player.current_track.get('hash') == track_hash:
            if self.audio_player.device.running:
                self.audio_player.pause()
            else:
                self.audio_player.play()
        else:
            track = self.db.get_track_by_hash(track_hash)
            if not track:
                # сообщение об ошибке
                return

            _track_source = track.get('source', None)
            if not _track_source:
                return

            self.audio_player.current_track = track
            self.audio_player.update_stream(_track_source)
            self.audio_player.main_screen.update_main_ui()

            self.update_cards_styles(track_hash)


    def add_track(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            None,
            "Выберите аудиофайлы",
            "",
            "Аудиофайлы (*.mp3 *.ogg *.flac *.wav)"
        )

        if not file_paths:
            return

        for fp in file_paths:
            audio_hash = get_content_hash(fp)
            if audio_hash in self._cards_cache:
                continue

            metadata = extract_metadata(fp)
            metadata.update({
                'hash': audio_hash,
                'source': fp
            })
            self.db.append(metadata)

        self.render_card_list()


    def delete_track(self, track_hash: str):
        if self.audio_player.current_track.get('hash') == track_hash:
            self.audio_player.reset_stream()

        self.db.delete(track_hash)
        self._cards_cache.pop(track_hash, None)
        self.render_card_list()



    def render_card_list(self):
        # восстановление стилей текущего трека
        _current_track_before = self.audio_player.current_track.get('hash') \
            if self.audio_player.current_track else None

        self._cards_cache.clear()
        self._clear_card_list()

        print(self.db.load())
        for track in self.db.load():
            if track['hash'] in self._cards_cache:
                continue

            card = TrackCard(
                track_hash=track['hash'],
                title=track['title'],
                artist=track['artist'],
                image=track['cover'],
            )
            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            self.main.cardList.addWidget(card)
            self._cards_cache[track['hash']] = card

        # восстановление выделения текущего трека
        if _current_track_before and _current_track_before in self._cards_cache:
            self.update_cards_styles(_current_track_before)

    def _clear_card_list(self):
        while self.main.cardList.count():
            item = self.main.cardList.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

    def update_cards_styles(self, track_hash: str):
        # очистка
        for card in self._cards_cache.values():
            card.set_playing_style(False)

        # применение
        if track_hash in self._cards_cache:
            self._cards_cache[track_hash].set_playing_style(True)


