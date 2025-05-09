import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QApplication)
from PySide6.QtGui import QPixmap
from public.ui_py import Ui_MainWindow
from src.classes.AudioPlayer import AudioPlayer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    # первоначальный ui
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.main_ui.artist.setText('')
        self.main_ui.title.setText('')
        self.main_ui.mainSection.update_image(QPixmap(':icons/icons/defaultGradient.png'))
        self.main_ui.cardList.setAlignment(Qt.AlignmentFlag.AlignTop)

    # главный класс
        self.audio_player = AudioPlayer(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Музыкальный проигрыватель')
    window.show()
    sys.exit(app.exec())