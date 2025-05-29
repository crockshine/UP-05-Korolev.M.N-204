import os
import miniaudio

from src.classes.ControlUnit import ControlUnit
from src.classes.JSON import JSON
from src.classes.MainScreen import MainScreen
from src.classes.Playlist import Playlist
from src.classes.Settings import Settings
from src.classes.Timeline import Timeline
from src.errors.CannotFindTrack import CannotFindTrack
from src.features.find_index import find_index
from src.features.get_content_hash import get_content_hash


# есть ли порядок
def required_data(func):
    def wrapper(self, *args, **kwargs):
        if not self.db.playlist_order:
            self.main.timeline.setEnabled(False)
            return
        return func(self, *args, **kwargs)
    return wrapper


class AudioPlayer:
    def __init__(self, main):

        self.main = main.main_ui
        self.db = JSON('db.json')

        self.errors = CannotFindTrack(self.db)
        self.current_track = None
        self.settings = Settings().settings

        self.device = miniaudio.PlaybackDevice()
        self.stream = None
        self.duration = 0

        self.main_screen = MainScreen(self, self.main)
        self.timeline = Timeline(self, self.main)
        self.control_unit = ControlUnit(self, self.main)
        self.playlist = Playlist(self, self.main, self.settings, self.errors)

        self.main.timeline.setEnabled(False)
        self.db.on_clear.connect(self.full_reset)

    def random(self):
        if self.settings.get('random') and self.current_track:
            self.db.shuffle(self.current_track["hash"])
        else:
            self.db.restore_order()


    @required_data
    def prev(self):
        if not self.current_track:
            return

        index = find_index(self.db.playlist_order, self.current_track["hash"])
        if index == -1:
            return

        new_hash = self.db.playlist_order[-1] if index == 0 else self.db.playlist_order[index - 1]

        new_track = self.db.get_track_by_hash(new_hash)
        if new_track:
            self.current_track = new_track
            self.update_stream(new_track)


    @required_data
    def next(self, is_auto=True):
        if not self.current_track:
            return

        index = find_index(self.db.playlist_order, self.current_track["hash"])
        if index == -1:
            return

        _need_to_start = True
        _loop = self.settings.get('loop')

        new_track = None

        if index == len(self.db.playlist_order) - 1:
            if not (_loop == 'self' and is_auto):
                new_track = self.db.get_track_by_hash(self.db.playlist_order[0])

            if _loop is None and is_auto:
                self.pause()
                self.timeline.reset_timer()
                _need_to_start = False
        else:
            if not (_loop == 'self' and is_auto):
                new_track = self.db.get_track_by_hash(self.db.playlist_order[index + 1])

        if new_track:
            self.update_stream(new_track, _need_to_start)


    @required_data
    def update_stream(self, new_track, need_to_start=True):
        source = new_track.get("source") if new_track else None

        if new_track is None:
            self.errors.show_JSON_erorr_dialog()
            self.full_reset()
        elif (
                source is None
                or not os.path.exists(source)
                or get_content_hash(source) != new_track.get("hash", None)):

            self.errors.show_cannot_find_dialog(
                new_track.get("title", None),
                new_track.get("hash", None)
            )
        else:
            self.current_track = new_track
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

            self.playlist.update_cards_styles(self.current_track.get("hash"))
            self.main_screen.update_main_ui()


    @required_data
    def set_seek(self, position_seconds):
        was_playing = self.device.running

        self.device.stop()

        self.stream = miniaudio.stream_file(
            self.current_track["source"],
            seek_frame=int(position_seconds * 44100)
        )

        if was_playing:
            self.play()


    def pause(self):
        if self.device.running:
            self.device.stop()
        self.timeline.pause_timer()
        self.control_unit.update_ui_play_pause_button(True)


    @required_data
    def play(self):
        if not self.current_track:
            first_hash = self.db.playlist_order[0]
            self.current_track = self.db.get_track_by_hash(first_hash)
            self.update_stream(self.current_track)
            self.device.stop()

        self.device.start(self.stream)
        self.timeline.start_timer()
        self.control_unit.update_ui_play_pause_button(False)


    def reset_stream(self):
        self.pause()
        self.timeline.reset_timer()
        self.current_track = None
        self.stream = None
        self.duration = 0
        self.main_screen.update_main_ui()


    def full_reset(self):
        self.reset_stream()
        self.playlist.clear_card_list()
        self.db.clear_JSON()
