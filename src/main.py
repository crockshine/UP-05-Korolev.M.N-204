import os
import sys
import miniaudio
from typing import Optional, Dict

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               QFileDialog, QWidget)
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
        self._setup_variables()
        self._setup_ui()
        self._add_event_listeners()
        self.render_card_list()

    def _setup_variables(self):
        self.db = HandleJSON('db.json')
        self.current_track_hash = None
        self._tracks_hash = set()
        self._cards_cache = {}  # Кэш карточек для быстрого доступа

        self.device = miniaudio.PlaybackDevice()
        self.stream = None

    def _setup_ui(self):
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.artist.setText('')
        self.main_ui.title.setText('')
        self.main_ui.cardList.setAlignment(Qt.AlignmentFlag.AlignTop)

    def _add_event_listeners(self):
        self.main_ui.addTrackButton.clicked.connect(self.add_track)

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
            self.stream = miniaudio.stream_file(track['source'])
            self.device.start(self.stream)

    def _update_main_ui(self, track: dict or None = None):
        pixmap = QPixmap(prepare_image(track['cover']))
        self.main_ui.image.setPixmap(pixmap)

        self.main_ui.artist.setText(track.get('artist', 'Автор не найден') if track else '')
        self.main_ui.title.setText(track.get('title', 'Без названия') if track else '')

    def _reset_all_card_styles(self):
        for card in self._cards_cache.values():
            card.set_playing_style(False)

    def _set_card_style(self, track_hash: str, is_playing: bool):
        if track_hash in self._cards_cache:
            self._cards_cache[track_hash].set_playing_style(is_playing)

    def add_track(self):
        """Добавление новых треков"""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите аудиофайлы",
            "",
            "Аудиофайлы (*.mp3 *.ogg *.flac *.wav)"
        )

        if not file_paths:
            return

        current_track_before = self.current_track_hash

        for fp in file_paths:
            audio_hash = get_content_hash(fp)
            if audio_hash in self._tracks_hash:
                continue

            metadata = extract_metadata(fp)
            metadata.update({
                'hash': audio_hash,
                'source': fp
            })
            self.db.append(metadata)

        self.render_card_list()

        # Восстановление выделения текущего трека
        if current_track_before and current_track_before in self._cards_cache:
            self._set_card_style(current_track_before, True)

    def delete_track(self, track_hash: str):
        """Удаление трека"""
        if self.current_track_hash == track_hash:
            self.device.stop()
            self.stream = None
            self._update_main_ui(None)
            self.current_track_hash = None

        self.db.delete(track_hash)
        self._cards_cache.pop(track_hash, None)
        self.render_card_list()

    def render_card_list(self):
        """Отрисовка списка треков"""
        self._tracks_hash = set()
        self.clear_card_list()

        for track in self.db.load():
            if track['hash'] in self._tracks_hash:
                continue

            self._tracks_hash.add(track['hash'])

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

    def clear_card_list(self):
        """Очистка списка треков"""
        while self.main_ui.cardList.count():
            item = self.main_ui.cardList.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec())