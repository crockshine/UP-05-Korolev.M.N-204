from time import sleep

from PySide6.QtWidgets import QFileDialog

from src.components.track_card import TrackCard
from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash


class Playlist:
    def __init__(self, audio_player, main, settings):
        super().__init__()
        self.settings = settings
        self.audio_player = audio_player
        self.main = main

    # переменные
        self.db = self.audio_player.db

    # обработчики
        self.main.addTrackButton.clicked.connect(self.add_track)

    # первый рендер
        self.render_card_list()


    def toggle_play(self, track_hash: str):
        # выбранный трек - текущий?
        if self.audio_player.current_track and next(iter(self.audio_player.current_track)) == track_hash:
            if self.audio_player.device.running:
                self.audio_player.pause()
            else:
                self.audio_player.play()
        else:
            track = self.db.get_track_by_hash(track_hash)
            if track is None:
                # сообщение об ошибке
                return

            _track_source = track[track_hash].get('source', None)
            if _track_source is None:
                # алгоритм поиска трека
                return

            if self.settings.get('random'):
                self.db.shuffle(track_hash)

            self.audio_player.current_track = track
            self.audio_player.update_stream(_track_source)

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
            if audio_hash in self.db.playlist_order:
                continue

            metadata = extract_metadata(fp)
            self.db.append({audio_hash: metadata})

        self.render_card_list()


    def delete_track(self, track_hash: str):
        if self.audio_player.current_track and next(iter(self.audio_player.current_track)) == track_hash:
            self.audio_player.reset_stream()

        self.db.delete(track_hash)
        self.render_card_list()


    def render_card_list(self):
        # восстановление стилей текущего трека
        _current_track_hash_before = next(iter(self.audio_player.current_track)) \
            if self.audio_player.current_track else None

        self._clear_card_list()

        _load_data = self.db.data

        for _hsh in _load_data:
            track = _load_data[_hsh]
            card = TrackCard(
                track_hash=_hsh,
                title = track['title'],
                artist=track['artist'],
                image=track['cover'],
            )
            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            if _hsh == _current_track_hash_before:
                card.set_playing_style(True)

            self.main.cardList.addWidget(card)


    def _clear_card_list(self):
        while self.main.cardList.count():
            item = self.main.cardList.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

    def update_cards_styles(self, track_hash: str):
        # обновляем стили
        for i in range(self.main.cardList.count()):
            widget = self.main.cardList.itemAt(i).widget()
            if isinstance(widget, TrackCard):
                widget.set_playing_style(widget.track_hash == track_hash)

