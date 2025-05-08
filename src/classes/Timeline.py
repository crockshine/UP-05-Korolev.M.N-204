import time
from PySide6.QtCore import QTimer


class Timeline:
    def __init__(self, audio_player):
        super().__init__()
        self.audio_player = audio_player

        self.timer = QTimer()
        self.timer.setInterval(1000)

        self._start_time = 0
        self._total_paused_time = 0
        self._is_paused = False
        self._last_pause_start = 0

        self.timer.timeout.connect(self._handle_timer)
        self.audio_player.main_ui.timeline.sliderReleased.connect(self.apply_seek)
        self.audio_player.main_ui.timeline.sliderPressed.connect(self.pause_timer)

    def apply_seek(self):
        position = self.audio_player.main_ui.timeline.value()
        position_in_seconds = int((position / 500) * self.audio_player.duration)
        print(position_in_seconds, self.audio_player.duration)

        self.audio_player.set_seek(position_in_seconds)

        # новое время старта
        self._start_time = time.time() - position_in_seconds

        # нужно забыть все паузы, тк по сути начинается новый таймлайн
        self._total_paused_time = 0

        if self._is_paused:
            self._last_pause_start = time.time()

    def start_timer(self, is_new: bool = False):
        if is_new:
            self.reset_timer()

        # были на паузе?
        if self._is_paused:
            self._total_paused_time += time.time() - self._last_pause_start
            self._is_paused = False

        self.timer.start()

    def pause_timer(self):
        if not self._is_paused:
            self._last_pause_start = time.time()
            self._is_paused = True
            self.timer.stop()

    def _handle_timer(self):
        if not self._is_paused:
            elapsed = time.time() - self._total_paused_time - self._start_time
            progress = int((elapsed / self.audio_player.duration) * 500)
            print(progress)
            self.audio_player.main_ui.timeline.setValue(min(500, max(0, progress)))

    def reset_timer(self):
        self.timer.stop()
        self._start_time = time.time()
        self._total_paused_time = 0
        self._is_paused = False
        self._last_pause_start = 0
        self.audio_player.main_ui.timeline.setValue(0)