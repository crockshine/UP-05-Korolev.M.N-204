import miniaudio

from src.classes.ControlUnit import ControlUnit
from src.classes.JSON import JSON
from src.classes.MainScreen import MainScreen
from src.classes.Playlist import Playlist
from src.classes.Settings import Settings
from src.classes.Timeline import Timeline
from src.features.find_index import find_index


# декоратор проверки наличия информации в бд
def required_data(func):
    def wrapper(self, *args, **kwargs):
        if not self.db.playlist_order:
            self.main.timeline.setEnabled(False)
            return
        return func(self, *args, **kwargs)

    return wrapper


class AudioPlayer:
    def __init__(self, main):
    # переменные
        self.main = main.main_ui

        self.current_track = None
        self.db = JSON()

        self.settings = Settings().settings

    # аудио поток
        self.device = miniaudio.PlaybackDevice()
        self.stream = None
        self.duration = 0

    # классы
        self.main_screen = MainScreen(self, self.main)
        self.timeline = Timeline(self,self.main)
        self.control_unit = ControlUnit(self, self.main)

        self.playlist = Playlist(self, self.main,  self.settings)

        self.main.timeline.setEnabled(False)

    # генерация случайного порядка
    def random(self):
        if self.settings.get('random') and self.db.playlist_order:
            self.db.shuffle(self.current_track['hash'] if self.current_track else None)
        else:
            self.db.get_playlist_order()

    # предыдущий трек
    @required_data
    def prev(self):
        if not self.current_track:
            return

        index = find_index(self.db.playlist_order, self.current_track['hash'])
        if index == -1:
            return

        if index == 0:
            new_track = self.db.get_track_by_hash(self.db.playlist_order[len(self.db.playlist_order) - 1])
            self.current_track = new_track
        else:
            new_track = self.db.get_track_by_hash(self.db.playlist_order[index - 1])
            self.current_track = new_track


        self.update_stream(self.current_track['filepath'])

    # следующий трек
    @required_data
    def next(self, is_auto = True):
        if not self.current_track:
            return

        index = find_index(self.db.playlist_order, self.current_track['hash'])
        if index == -1:
            return

        _need_to_start = True
        _loop = self.settings.get('loop')

        # выборка, как зациклить
        if index == len(self.db.playlist_order) - 1:
            if not (_loop == 'self' and is_auto):
                new_track = self.db.get_track_by_hash(self.db.playlist_order[0])
                self.current_track = new_track

            if _loop is None and is_auto:
                self.pause()
                self.timeline.reset_timer()
                _need_to_start = False

        else:
            if not(_loop == 'self' and is_auto):
                new_track = self.db.get_track_by_hash(self.db.playlist_order[index + 1])
                self.current_track = new_track

        self.update_stream(self.current_track['filepath'], _need_to_start)

    # обновление потока воспроизведения (переключение трека)
    @required_data
    def update_stream(self, source, need_to_start = True):
        self.main.timeline.setEnabled(True)

        if self.device.running:
            self.device.stop()

        file_info = miniaudio.get_file_info(source)
        self.duration = file_info.duration

        self.stream = miniaudio.stream_file(source)

        if need_to_start:
            self.device.start(self.stream)
            self.timeline.start_timer(is_new=True)
            self.control_unit.update_ui_play_pause_button(False)

        self.playlist.update_cards_styles(self.current_track['hash'])
        self.main_screen.update_main_ui()

    # установка перемотки
    @required_data
    def set_seek(self, position_seconds):
        was_playing = self.device.running

        self.device.stop()


        self.stream = miniaudio.stream_file(
            self.current_track['filepath'],
            seek_frame=int(position_seconds * 44100)
        )

        if was_playing:
            self.play()

    # пауза
    @required_data
    def pause(self):
        if self.device.running:
            self.device.stop()
        self.timeline.pause_timer()
        self.control_unit.update_ui_play_pause_button(True)

    # воспроизвести
    @required_data
    def play(self):
        if not self.current_track :
            track = self.db.get_track_by_hash(self.db.playlist_order[0])

            self.current_track = track

            self.update_stream(self.current_track['filepath'])
            self.device.stop()

        self.device.start(self.stream)
        self.timeline.start_timer()
        self.control_unit.update_ui_play_pause_button(False)

    # сброс всех значений
    def reset_stream(self):
        self.pause()
        self.timeline.reset_timer()
        self.current_track = {}
        self.stream = None
        self.duration = 0
        self.main_screen.update_main_ui()
