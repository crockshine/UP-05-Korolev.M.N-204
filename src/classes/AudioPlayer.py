import miniaudio
import time
from PySide6.QtCore import QTimer

from src.classes.ControlUnit import ControlUnit
from src.classes.JSON import JSON
from src.classes.MainScreen import MainScreen
from src.classes.Playlist import Playlist
from src.classes.Settings import Settings
from src.classes.Timeline import Timeline
from src.features.find_index import find_index


class AudioPlayer:
    def __init__(self, main):
    # переменные
        self.current_track = {}
        self.db = JSON('db.json')
        self.settings = Settings().settings

    # аудио поток
        self.device = miniaudio.PlaybackDevice()
        self.stream = None
        self.duration = 0
        self.sample_rate = 44100

    # классы
        self.playlist = Playlist(self, main.main_ui)
        self.main_screen = MainScreen(self, main.main_ui)
        self.timeline = Timeline(self, main.main_ui)
        self.control_unit = ControlUnit(self, main.main_ui)



    def prev(self):
        index = find_index(self.db.data, self.current_track.get('hash'))

        if index == -1:
            return

        if index == 0:
            self.current_track = self.db.data[len(self.db.data) - 1]
        else:
            self.current_track = self.db.data[index - 1]

        self.update_stream(self.current_track.get('source'))


    def next(self, is_auto = True):
        index = find_index(self.db.data, self.current_track.get('hash'))

        if index == -1:
            return

        _need_to_start = True

        # трек не зацикливается?
        if self.settings.get('loop') != 'self':
            # трек последний?
            if index == len(self.db.data) - 1:
                self.current_track = self.db.data[0]

                # если нет зацикливания
                if self.settings.get('loop') is None and is_auto:
                    self.pause()
                    self.timeline.reset_timer()
                    _need_to_start = False

            else:
                self.current_track = self.db.data[index + 1]

        self.update_stream(self.current_track.get('source'), _need_to_start)


    def update_stream(self, source, need_to_start = True):
        if self.device.running:
            self.device.stop()


        file_info = miniaudio.get_file_info(source)
        self.duration = file_info.duration
        self.sample_rate = file_info.sample_rate


        self.stream = miniaudio.stream_file(source)

        if need_to_start:
            self.device.start(self.stream)
            self.timeline.start_timer(is_new=True)
            self.control_unit.update_ui_play_pause_button(False)

        self.playlist.update_cards_styles(self.current_track.get('hash'))
        self.main_screen.update_main_ui()


    def set_seek(self, position_seconds):
        if not self.stream:
            return

        was_playing = self.device.running

        self.device.stop()

        self.stream = miniaudio.stream_file(
            self.current_track.get('source'),
            seek_frame=int(position_seconds * self.sample_rate)
        )

        if was_playing:
            self.play()

    def reset_stream(self):
        self.pause()
        self.timeline.reset_timer()
        self.current_track = {}
        self.stream = None
        self.duration = 0
        self.main_screen.update_main_ui()

    def pause(self):
        if self.device.running:
            self.device.stop()
        self.timeline.pause_timer()
        self.control_unit.update_ui_play_pause_button(True)

    def play(self):
        if not self.stream:
            if self.current_track:
                self.update_stream(self.current_track.get('source'))
            return

        self.device.start(self.stream)
        self.timeline.start_timer()
        self.control_unit.update_ui_play_pause_button(False)