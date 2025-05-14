import time

from PySide6.QtCore import QTimer


class Timeline:
    def __init__(self, audio_player, main):
        self.audio_player = audio_player
        self.main = main

        self.timer = QTimer()
        self.timer.setInterval(100)

        self._last_update = 0
        self._total_time = 0
        self._is_paused = True

        self.timer.timeout.connect(self.update_position)
        self.main.timeline.sliderReleased.connect(self.apply_seek)
        self.main.timeline.sliderPressed.connect(self.pause_timer) # для плавного UI


    def apply_seek(self):

        position = self.main.timeline.value()
        position_seconds = (position / 500) * self.audio_player.duration
        self.audio_player.set_seek(position_seconds)

        self._total_time = position_seconds
        self._last_update = time.time()

        if not self._is_paused:
            self.timer.start()

    def start_timer(self, is_new=False):
        if is_new:
            self._total_time = 0

        self._last_update = time.time()
        self._is_paused = False
        self.timer.start()

    def pause_timer(self):
        if not self._is_paused:
            self._is_paused = True
            self.timer.stop()

    def update_position(self):
        if not self._is_paused and self.audio_player.stream:
            # в каждый интервал начисялем +- указанное время обновления
            # можно было в тотал += 100, но так будет точнее
            now = time.time()
            d = now - self._last_update
            self._last_update = now
            self._total_time += d

            current_time = min(self._total_time, self.audio_player.duration)
            progress = int((current_time / self.audio_player.duration) * 500)
            self.main.timeline.setValue(min(500, max(0, progress)))

            if current_time >= self.audio_player.duration:
                self.audio_player.next()

    def reset_timer(self):
        self.pause_timer()
        self._total_time = 0
        self.main.timeline.setValue(0)