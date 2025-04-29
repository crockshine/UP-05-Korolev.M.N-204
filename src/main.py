import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from public.ui_py import Ui_MainWindow
from components.track_card import TrackCard
from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash


class AudioPlayer(QMainWindow):
    def __init__(self):
        super(AudioPlayer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.track_card = TrackCard()

        self.ui.addTrackButton.clicked.connect(self.add_track)

    def add_track(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите аудиофайлы",
            "",
            "Аудиофайлы (*.mp3 *.ogg *.flac *.wav)"
        )

        if file_paths:
            for fp in file_paths:
                metadata = extract_metadata(fp)
                audio_hash = get_content_hash(fp)
                print(fp, audio_hash)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()

    sys.exit(app.exec())

