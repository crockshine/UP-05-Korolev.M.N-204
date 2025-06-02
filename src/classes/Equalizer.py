from PySide6.QtCore import QObject, Signal
import soundfile as sf
import numpy as np
import scipy.signal as signal
from PySide6.QtWidgets import QMainWindow

from public.ui_py.ui_sound_settings import Ui_sound_settings

bands = [
    (60, 170), (170, 310),
    (310, 600), (600, 1000),
    (1000, 3000), (3000, 6000), (6000, 12000), (12000, 14000),
    (14000, 16000), (16000, 18000)
        ]

class Equalizer(QObject):
    on_filtered = Signal()
    on_reset = Signal()

    def __init__(self, audio_player=None):
        super().__init__()

        self.window = None
        self.ui = Ui_sound_settings()
        self.audio_player = audio_player


    def show_settings(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui.setupUi(self.window)
            self.ui.apply_eq.clicked.connect(self.apply_settings)
            self.ui.reset_eq.clicked.connect(self.reset_settings)
            self.ui.volume_slider.setValue(100)
        self.window.show()
        self.window.raise_()
        self.window.activateWindow()

    def reset_settings(self):
        for (low, high) in bands:
            slider_name = f"eq_{low}"
            slider = getattr(self.ui, slider_name, None)
            slider.setValue(50)

        self.ui.volume_slider.setValue(100)
        self.on_reset.emit()
        self.update_filters()

    def apply_settings(self):
        self.update_filters()
        self.on_filtered.emit()

    def update_filters(self):
        if self.audio_player.current_track is None:
            return

        source = self.audio_player.current_track['source']
        audio, sr = sf.read(source, dtype='float32')
        nyq = 0.5 * sr

        filtered = np.zeros_like(audio)

        for i, (low, high) in enumerate(bands):
            _l = low / nyq
            _h = high / nyq

            slider_name = f"eq_{low}"
            slider = getattr(self.ui, slider_name, None)

            if not slider:
                continue

            gain = slider.value() / 50

            sos = signal.butter(4, [_l, _h], 'bandpass', output='sos')

            if audio.ndim == 1:
                filtered += signal.sosfilt(sos, audio) * gain
            else:
                for ch in range(audio.shape[1]):
                    filtered[:, ch] += signal.sosfilt(sos, audio[:, ch]) * gain

        max_val = np.max(np.abs(filtered))
        if max_val > 0:
            filtered /= max_val

        filtered *= self.ui.volume_slider.value() / 100
        try:
            sf.write('equalized.wav', filtered, sr)
        except Exception as e:
            print(e)








