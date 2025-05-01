from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from public.ui_py import Ui_TrackCardWrapper


class TrackCard(QWidget):
    on_delete = Signal(int)

    def __init__(self, parent=None,
                 track_id = 0,
                 image = u':/icons/icons/defaultImg.png',
                 title='Без названия',
                 artist='Автор не найден'
                 ):
        super().__init__(parent)

        self.ui = Ui_TrackCardWrapper()
        self.ui.setupUi(self)

        pixmap = QPixmap(image)
        self.ui.trackImage.setPixmap(pixmap)
        self.ui.title.setText(title)
        self.ui.artist.setText(artist)

        self.ui.delete_button.clicked.connect(lambda: self.on_delete.emit(track_id))

