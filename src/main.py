import os
import sys
import miniaudio

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               QFileDialog, )
from PySide6.QtGui import QPixmap

from public.ui_py import Ui_MainWindow
from components.track_card import TrackCard
from src.classes.HandleJSON import HandleJSON
from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash
from src.features.prepare_image import prepare_image


class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
    # переменные
        self.db = HandleJSON('db.json')
        self.current_track_hash = None  # для аудио
        self._cards_cache = {}  # {хэш: TrackCard}

        self.device = miniaudio.PlaybackDevice()
        self.stream = None

    # ui
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.main_ui.artist.setText('')
        self.main_ui.title.setText('')
        self.main_ui.mainSection.update_image(QPixmap(':icons/icons/defaultGradient.png'))
        self.main_ui.cardList.setAlignment(Qt.AlignmentFlag.AlignTop)



    # обработчики
        self.main_ui.addTrackButton.clicked.connect(self.add_track)

    # первый рендер
        self.render_card_list()

    def toggle_play(self, track_hash: str):
        # выбранный трек - текущий?
        if self.current_track_hash == track_hash:
            if self.device.running:
                self.device.stop()
            else:
                self.device.start(self.stream)
        else:
            self.current_track_hash = track_hash

            track = self.db.get_track_by_hash(track_hash)
            if not track: return

            self._update_main_ui(track)
            self._reset_all_card_styles()
            self._set_card_style(track_hash, True)

            self.device.stop()
            self.stream = miniaudio.stream_file(track.get('source'))
            self.device.start(self.stream)



    def add_track(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите аудиофайлы",
            "",
            "Аудиофайлы (*.mp3 *.ogg *.flac *.wav)"
        )

        if not file_paths:
            return

        _current_track_before = self.current_track_hash

        for fp in file_paths:
            audio_hash = get_content_hash(fp)
            if audio_hash in self._cards_cache:
                continue

            metadata = extract_metadata(fp)
            metadata.update({
                'hash': audio_hash,
                'source': fp
            })
            self.db.append(metadata)

        self.render_card_list()

        # восстановление выделения текущего трека
        if _current_track_before and _current_track_before in self._cards_cache:
            self._set_card_style(_current_track_before, True)

    def delete_track(self, track_hash: str):
        if self.current_track_hash == track_hash:
            self.device.stop()
            self.stream = None
            self._update_main_ui(None)
            self.current_track_hash = None

        self.db.delete(track_hash)
        self._cards_cache.pop(track_hash, None)
        self.render_card_list()

    def render_card_list(self):
        self._cards_cache.clear()
        self._clear_card_list()

        for track in self.db.load():
            if track['hash'] in self._cards_cache:
                continue

            card = TrackCard(
                track_hash=track['hash'],
                title=track['title'],
                artist=track['artist'],
                image=track['cover'],
            )

            card.on_delete.connect(self.delete_track)
            card.on_play.connect(self.toggle_play)

            self.main_ui.cardList.addWidget(card)
            self._cards_cache[track['hash']] = card

    def _clear_card_list(self):
        while self.main_ui.cardList.count():
            item = self.main_ui.cardList.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

    def _update_main_ui(self, track: dict or None = None):
        _pixmap = QPixmap(
            prepare_image(track['cover'] if track else None)
        )
        self.main_ui.mainSection.update_image(_pixmap if track else QPixmap(':icons/icons/defaultGradient.png'))
        self.main_ui.image.setPixmap(_pixmap)

        self.main_ui.artist.setText(track.get('artist', 'Автор не найден') if track else '')
        self.main_ui.title.setText(track.get('title', 'Без названия') if track else '')

    def _reset_all_card_styles(self):
        for card in self._cards_cache.values():
            card.set_playing_style(False)

    def _set_card_style(self, track_hash: str, is_playing: bool):
        if track_hash in self._cards_cache:
            self._cards_cache[track_hash].set_playing_style(is_playing)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.setWindowTitle('Музыкальный проигрыватель ')
    window.show()
    sys.exit(app.exec())