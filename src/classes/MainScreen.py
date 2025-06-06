from PySide6.QtGui import QPixmap, QTransform, QIcon
from PySide6.QtWidgets import QSizePolicy

from src.features.prepare_image import prepare_image


class MainScreen:
    def __init__(self, audio_player, main):
        super().__init__()
        self.audio_player = audio_player
        self.main = main

        self.is_open_sidebar = True
        self.main.show_hidden_button.clicked.connect(self.toggle_sidebar)

        self.pixmap = self.main.show_hidden_button.icon().pixmap(32, 32)
        self.rotated_pixmap = self.pixmap.transformed(QTransform().rotate(180))


    def toggle_sidebar(self):
        self.is_open_sidebar = not self.is_open_sidebar
        self.main.playList.setVisible(self.is_open_sidebar)

        if self.is_open_sidebar:
            self.main.show_hidden_button.setIcon(QIcon(self.pixmap))
        else:
            self.main.show_hidden_button.setIcon(QIcon(self.rotated_pixmap))


    def update_main_ui(self):
        track_info = self.audio_player.current_track

        _cover, _bg = prepare_image(track_info.get('cover') if track_info else None)

        self.main.mainSection.update_image(_bg)
        self.main.image.setPixmap(_cover)

        self.main.title.setText(track_info.get('title', 'Без названия') if track_info else '')
        self.main.artist.setText(track_info.get('artist', 'Автор не найден') if track_info else '')

        self.main.title.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
