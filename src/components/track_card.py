from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget

from public.ui_py import Ui_TrackCardWrapper
from src.features.prepare_image import prepare_image
from src.features.trim_string import trim_string


class TrackCard(QWidget):
    on_delete = Signal(str)
    on_play = Signal(str)

    def __init__(self, parent=None,
                 track_hash = '',
                 image = '',
                 title='Без названия',
                 artist='Автор не найден'
                 ):
        super().__init__(parent)

        self.track_hash = track_hash
        self.ui = Ui_TrackCardWrapper()
        self.ui.setupUi(self)

        _cover, _ = prepare_image(image if image is not None else None)

        self.ui.trackImage.setPixmap(_cover)
        self.ui.title.setText(trim_string(title))
        self.ui.artist.setText(trim_string(artist))

        self.ui.delete_button.clicked.connect(lambda: self.on_delete.emit(track_hash))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.on_play.emit(self.track_hash)

    def set_playing_style(self, is_playing):
        if is_playing:
            self.ui.TrackCard.setStyleSheet("background-color:rgba(0, 0, 0, 20);")
        else:
            self.ui.TrackCard.setStyleSheet("background: transparent; border-bottom: 1px solid rgba(0,0,0,50);")
