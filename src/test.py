import sys
import numpy as np
import miniaudio
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel, QFileDialog, QWidget
)
from PySide6.QtCore import Qt, QTimer
import pyo


class AudioPlayer:
    def __init__(self):
        self.server = pyo.Server().boot()
        self.server.start()
        self.sound = None
        self.volume = 0.7
        self.equalizer_bands = []
        self.current_file = None

    def load_file(self, file_path):
        """Загружает аудиофайл и создает эквалайзер"""
        self.current_file = file_path
        decoded = miniaudio.decode_file(file_path)

        # Конвертируем в моно, если стерео (для упрощения)
        if decoded.nchannels == 2:
            samples = np.frombuffer(decoded.samples, dtype=np.int16).reshape(-1, 2)
            mono_samples = samples.mean(axis=1).astype(np.int16)
        else:
            mono_samples = np.frombuffer(decoded.samples, dtype=np.int16)

        # Нормализуем и конвертируем в float32 для pyo
        samples_float = mono_samples / 32768.0
        self.sound = pyo.DataTable(size=len(samples_float), init=samples_float)
        self.player = pyo.TableRead(self.sound, freq=self.sound.getRate(), loop=False)

        # Создаем 5-полосный эквалайзер
        self.setup_equalizer()
        self.update_volume()

    def setup_equalizer(self):
        """Инициализирует полосы эквалайзера"""
        freq_bands = [80, 250, 1000, 4000, 8000]  # Частоты для 5 полос
        self.equalizer_bands = []

        for freq in freq_bands:
            band = pyo.IRWinSinc(
                self.player,
                freq=freq,
                bw=0.5,
                type=2,  # Bandpass
            )
            self.equalizer_bands.append(band)

        # Смешиваем все полосы
        self.mixer = pyo.Mixer(outs=1, chnls=1)
        for i, band in enumerate(self.equalizer_bands):
            self.mixer.addInput(i, band)
            self.mixer.setAmp(i, 0, 1.0)  # Начальный gain = 1.0

        self.mixer.out()

    def set_eq_gain(self, band_idx, gain):
        """Устанавливает gain для полосы эквалайзера"""
        if 0 <= band_idx < len(self.equalizer_bands):
            self.mixer.setAmp(band_idx, 0, gain)

    def set_volume(self, volume):
        """Устанавливает громкость (0.0 - 1.0)"""
        self.volume = volume
        self.update_volume()

    def update_volume(self):
        """Применяет громкость к выходному сигналу"""
        if hasattr(self, 'mixer'):
            self.mixer.setMul(self.volume)

    def play(self):
        """Запускает воспроизведение"""
        if self.sound:
            self.player.out()

    def stop(self):
        """Останавливает воспроизведение"""
        if hasattr(self, 'player'):
            self.player.stop()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Player with Equalizer")
        self.setGeometry(100, 100, 500, 400)

        self.player = AudioPlayer()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Кнопки управления
        self.btn_open = QPushButton("Open File")
        self.btn_open.clicked.connect(self.open_file)

        self.btn_play = QPushButton("Play")
        self.btn_play.clicked.connect(self.player.play)

        self.btn_stop = QPushButton("Stop")
        self.btn_stop.clicked.connect(self.player.stop)

        # Слайдер громкости
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.label_volume = QLabel("Volume: 70%")

        # Слайдеры эквалайзера (5 полос)
        self.eq_sliders = []
        self.eq_labels = []
        eq_freqs = ["80Hz", "250Hz", "1kHz", "4kHz", "8kHz"]

        for i, freq in enumerate(eq_freqs):
            slider = QSlider(Qt.Vertical)
            slider.setRange(-20, 20)  # -20dB to +20dB
            slider.setValue(0)
            slider.valueChanged.connect(lambda val, idx=i: self.set_eq_gain(idx, val))

            label = QLabel(freq)

            eq_layout = QVBoxLayout()
            eq_layout.addWidget(slider)
            eq_layout.addWidget(label, alignment=Qt.AlignCenter)

            self.eq_sliders.append(slider)
            self.eq_labels.append(label)

        # Группируем слайдеры эквалайзера
        eq_group_layout = QHBoxLayout()
        for slider_layout in [self.eq_sliders[i] for i in range(5)]:
            eq_group_layout.addWidget(slider_layout)

        # Размещаем элементы
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.btn_open)
        control_layout.addWidget(self.btn_play)
        control_layout.addWidget(self.btn_stop)

        layout.addLayout(control_layout)
        layout.addWidget(QLabel("Volume:"))
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.label_volume)
        layout.addWidget(QLabel("Equalizer:"))
        layout.addLayout(eq_group_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Audio File",
            "",
            "Audio Files (*.mp3 *.wav *.flac *.ogg)"
        )
        if file_path:
            self.player.load_file(file_path)

    def set_volume(self, value):
        volume = value / 100.0
        self.player.set_volume(volume)
        self.label_volume.setText(f"Volume: {value}%")

    def set_eq_gain(self, band_idx, db_value):
        """Преобразует dB в линейный gain и применяет к полосе"""
        gain = 10 ** (db_value / 20.0)  # dB to linear
        self.player.set_eq_gain(band_idx, gain)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())