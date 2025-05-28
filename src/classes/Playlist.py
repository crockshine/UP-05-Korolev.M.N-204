from PySide6.QtWidgets import QFileDialog
from src.classes.ThreadLoading import ThreadLoading
from src.components.track_card import TrackCard
from PySide6.QtCore import Signal


class Playlist:
    def __init__(self, audio_player, main, settings):
        super().__init__()
    # переменные
        self.settings = settings
        self.audio_player = audio_player
        self.main = main
        self.db = self.audio_player.db

    # обработчики
        self.main.addTrackButton.clicked.connect(self.add_track)

    # доп. поток
        self.thread_load = ThreadLoading(self.db)
        self.thread_load.ready_track.connect(self.stream_render)

    # первый рендер
        self.render_card_list()

    def stream_render(self, card_data):
        _hsh = next(iter(card_data))
        try:
            card = TrackCard(
                track_hash=_hsh,
                title=card_data[_hsh]['title'],
                artist=card_data[_hsh]['artist'],
                image=card_data[_hsh]['cover']
            )

            self.main.cardList.addWidget(card)
            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            self.main.label.setText("")
        except Exception as e:
            print(e)

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

        self.thread_load.data_received.emit(file_paths)

    def delete_track(self, track_hash: str):
        if self.audio_player.current_track and next(iter(self.audio_player.current_track)) == track_hash:
            self.audio_player.reset_stream()

        self.db.delete_track(track_hash)
        for i in range(self.main.cardList.count()):
            widget = self.main.cardList.itemAt(i).widget()
            if isinstance(widget, TrackCard) and widget.track_hash == track_hash:
                widget.deleteLater()
                break


    def render_card_list(self):
        # восстановление стилей текущего трека
        _current_track_hash_before = next(iter(self.audio_player.current_track)) \
            if self.audio_player.current_track else None

        self._clear_card_list()

        _load_data = self.db.read()
        if not _load_data:
            self.main.label.setText("Плейлист пуст")
            return
        self.main.label.setText("")

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

