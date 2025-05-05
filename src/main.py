import os
import sys
import time

import miniaudio

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               )
from PySide6.QtGui import QPixmap

from public.ui_py import Ui_MainWindow
from src.classes.ControlUnit import ControlUnit
from src.classes.MainScreen import MainScreen
from src.classes.Playlist import Playlist
from src.classes.Timeline import Timeline


class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
    # переменные
        self.current_track = {}

    # аудио
        self.device = miniaudio.PlaybackDevice()
        self.stream = None
        self.duration = 0

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
        self.timeline = Timeline(self)
        self.control_unit = ControlUnit(self)


    def set_seek(self, position):
        if not self.device:
            return

        _before_state = self.device.running

        self.device.stop()
        self.timeline.pause_timer()

        self.stream = miniaudio.stream_file(self.current_track.get('source'), seek_frame=position * 41000)

        if _before_state:
            self.device.start(self.stream)
            self.timeline.start_timer()


    def update_stream(self, source: str):
        """
        Переключение трека:
        1) Меняет и запускает другой аудио поток
        2) Информация о продолжительности
        3) Запуск таймлайна
        """
        if not self.device:
            return

        self.device.stop()
        self.stream = miniaudio.stream_file(source)
        self.duration = miniaudio.get_file_info(source).duration
        self.device.start(self.stream)

        self.control_unit.update_ui_play_pause_button(False)
        self.timeline.start_timer(is_new=True)


    def reset_stream(self):
        """
        Сброс всех значений потока
        """
        if not self.device:
            return

        self.device.stop()
        self.stream = None
        self.current_track = None
        self.duration = 0

        self.timeline.reset_timer()
        self.main_screen.update_main_ui()
        self.control_unit.update_ui_play_pause_button(True)


    def pause(self):
        if not self.device:
            return

        self.device.stop()
        self.timeline.pause_timer()
        self.control_unit.update_ui_play_pause_button(True)


    def play(self):
        if not self.device:
            return

        self.device.start(self.stream)
        self.timeline.start_timer(is_new=False)
        self.control_unit.update_ui_play_pause_button(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.setWindowTitle('Музыкальный проигрыватель')
    window.show()
    sys.exit(app.exec())