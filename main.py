import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout

from ui_main import Ui_MainWindow
from ui_track_card import Ui_TrackCard

class AudioPlayer(QMainWindow):
    def __init__(self):
        super(AudioPlayer, self).__init__()
        self.ui = Ui_MainWindow()
        self.track_card = Ui_TrackCard()

        self.ui.setupUi(self)
        self.ui.scrollAreaWidgetContents.setLayout(self.track_card)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()

    sys.exit(app.exec())

