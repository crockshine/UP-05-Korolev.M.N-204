from PySide6.QtGui import QPixmap

from src.features.prepare_image import prepare_image


class MainScreen:
    def __init__(self, audio_player):
        super().__init__()
        self.audio_player = audio_player
        self.audio_player.interval.timeout.connect(self.update_progress_bar)


    def update_progress_bar(self):
        return
        # if not self.device: return
        # _current_time = time.time()
        # _progress = (_current_time - self.start_play_time - self.time_on_pause) / self.duration * 100
        # self.main_ui.timeline.setValue(int(_progress))

    def update_main_ui(self, track: dict or None = None):
        _pixmap = QPixmap(
            prepare_image(track.get('cover') if track else None)
        )
        self.audio_player.main_ui.mainSection.update_image(_pixmap if track else QPixmap(':icons/icons/defaultGradient.png'))
        self.audio_player.main_ui.image.setPixmap(_pixmap)

        self.audio_player.main_ui.title.setText(track.get('title', 'Без названия') if track else '')
        self.audio_player.main_ui.artist.setText(track.get('artist', 'Автор не найден') if track else '')
