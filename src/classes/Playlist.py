from PySide6.QtWidgets import QFileDialog
from src.classes.ThreadLoading import ThreadLoading
from src.components.track_card import TrackCard


class Playlist:
    def __init__(self, audio_player, main, settings, errors):
        super().__init__()
        self.settings = settings
        self.errors = errors
        self.audio_player = audio_player
        self.main = main
        self.db = self.audio_player.db

        self.main.addTrackButton.clicked.connect(self.add_track)
        self.errors.on_delete.connect(self.delete_track)

        self.thread_load = ThreadLoading(self.db)
        self.thread_load.ready_track.connect(self.stream_render)

        self.render_card_list()

    def stream_render(self, track_data):
        self.db.append(track_data)
        _hsh = track_data["hash"]

        try:
            card = TrackCard(
                track_hash=_hsh,
                title=track_data['title'],
                artist=track_data['artist'],
                image=track_data['cover']
            )

            self.main.cardList.addWidget(card)
            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            self.main.label.setText("")
        except Exception as e:
            print(e)

    def toggle_play(self, track_hash: str):
        current_hash = self.audio_player.current_track.get("hash") if self.audio_player.current_track else None

        if current_hash == track_hash:
            if self.audio_player.device.running:
                self.audio_player.pause()
            else:
                self.audio_player.play()
        else:
            track = self.db.get_track_by_hash(track_hash)

            if self.settings.get('random'):
                self.db.shuffle(track_hash)

            self.audio_player.update_stream(track)

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
        current_hash = self.audio_player.current_track.get("hash") if self.audio_player.current_track else None

        if current_hash == track_hash:
            self.audio_player.reset_stream()

        self.db.delete_track(track_hash)

        for i in range(self.main.cardList.count()):
            widget = self.main.cardList.itemAt(i).widget()
            if isinstance(widget, TrackCard) and widget.track_hash == track_hash:
                widget.deleteLater()
                break


    def render_card_list(self):
        self.clear_card_list()

        all_tracks = self.db.read()
        if not all_tracks:
            self.main.label.setText("Плейлист пуст")
            return

        self.main.label.setText("")

        # сортировка по порядку
        hash_to_track = {track["hash"]: track for track in all_tracks}
        for _hsh in self.db.playlist_order:
            track = hash_to_track.get(_hsh)
            if not track:
                continue

            card = TrackCard(
                track_hash=_hsh,
                title=track['title'],
                artist=track['artist'],
                image=track['cover'],
            )
            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            self.main.cardList.addWidget(card)

    def clear_card_list(self):
        while self.main.cardList.count():
            item = self.main.cardList.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

        self.main.label.setText("Плейлист пуст")

    def update_cards_styles(self, track_hash: str):
        for i in range(self.main.cardList.count()):
            widget = self.main.cardList.itemAt(i).widget()
            if isinstance(widget, TrackCard):
                widget.set_playing_style(widget.track_hash == track_hash)
