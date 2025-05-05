from PySide6.QtGui import QPixmap, QTransform, QIcon

from src.features.prepare_image import prepare_image


class MainScreen:
    def __init__(self, audio_player):
        super().__init__()
        self.audio_player = audio_player

        self.is_open_sidebar = True
        self.audio_player.main_ui.show_hidden_button.clicked.connect(self.toggle_sidebar)

        self.pixmap = self.audio_player.main_ui.show_hidden_button.icon().pixmap(32, 32)
        self.rotated_pixmap = self.pixmap.transformed(QTransform().rotate(180))

    def toggle_sidebar(self):
        self.is_open_sidebar = not self.is_open_sidebar
        self.audio_player.main_ui.playList.setVisible(self.is_open_sidebar)

        if self.is_open_sidebar:
            self.audio_player.main_ui.show_hidden_button.setIcon(QIcon(self.pixmap))
        else:
            self.audio_player.main_ui.show_hidden_button.setIcon(QIcon(self.rotated_pixmap))


    def update_main_ui(self):
        track = self.audio_player.current_track
        print(track)
        _pixmap = QPixmap(
            prepare_image(track.get('cover') if track else None)
        )
        self.audio_player.main_ui.mainSection.update_image(_pixmap if track else QPixmap(':icons/icons/defaultGradient.png'))
        self.audio_player.main_ui.image.setPixmap(_pixmap)

        self.audio_player.main_ui.title.setText(track.get('title', 'Без названия') if track else '')
        self.audio_player.main_ui.artist.setText(track.get('artist', 'Автор не найден') if track else '')
