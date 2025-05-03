import os
import sys
import time

import miniaudio

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               )
from PySide6.QtGui import QPixmap

from public.ui_py import Ui_MainWindow
from src.classes.MainScreen import MainScreen
from src.classes.Playlist import Playlist


class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

    # переменные
        self.current_track_hash = None

    # аудио
        self.device = miniaudio.PlaybackDevice()
        self.stream = None

        self.duration = 0
        self.start_play_time = 0
        self.time_on_pause = 0

        self.interval = QTimer()

    # первоначальный ui
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.main_ui.artist.setText('')
        self.main_ui.title.setText('')
        self.main_ui.mainSection.update_image(QPixmap(':icons/icons/defaultGradient.png'))
        self.main_ui.cardList.setAlignment(Qt.AlignmentFlag.AlignTop)

    # классы
        self.playlist = Playlist(self)
        self.main_screen = MainScreen(self)

    # обработчики

    def update_stream(self, source: str):
        """
        меняет и запускает аудио поток
        """
        self.device.stop()

        self.stream = miniaudio.stream_file(source)
        self.duration = miniaudio.get_file_info(source).duration

        self.device.start(self.stream)
        self.start_play_time = time.time()

        self.interval.start(1000)

    def reset_stream(self):
        self.device.stop()
        self.stream = None
        self.main_screen.update_main_ui(None)
        self.current_track_hash = None

    def pause(self):
        self.device.stop()
        self.interval.stop()

    def play(self):
        self.device.start(self.stream)
        self.interval.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.setWindowTitle('Музыкальный проигрыватель')
    window.show()
    sys.exit(app.exec())