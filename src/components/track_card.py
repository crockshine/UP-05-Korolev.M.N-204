from PySide6.QtWidgets import QWidget

from public.ui_py import Ui_TrackCard


class TrackCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TrackCard()
        self.ui.setupUi(self)

