import sys
import json

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from public.ui_py import Ui_MainWindow
from components.track_card import TrackCard
from src.features.append_json import append_json
from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash
from src.features.read_json import read_json


class AudioPlayer(QMainWindow):
    def __init__(self):
        super(AudioPlayer, self).__init__()

        # SET UP
        self._tracks_hash = set()

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.cardList.setAlignment(Qt.AlignTop)

        # EVENT LISTENERS
        self.main_ui.addTrackButton.clicked.connect(self.add_track)

        # FIRST RENDER
        self.render_card_list()

    def clear_card_list(self):
        while self.main_ui.cardList.count():
            child = self.main_ui.cardList.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def render_card_list(self):
        data = read_json()

        self._tracks_hash = set()
        self.clear_card_list()

        for track in data:
            if track['hash'] in self._tracks_hash:
                return

            self._tracks_hash.add(track['hash'])

            track_card = TrackCard(
                track_id=track['track_id'],
                title=track['title'],
                artist=track['artist']
            )
            track_card.on_delete.connect(self.delete_track)

            self.main_ui.cardList.addWidget(track_card)

    def add_track(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите аудиофайлы",
            "",
            "Аудиофайлы (*.mp3 *.ogg *.flac *.wav)"
        )

        if not file_paths:
            return

        for fp in file_paths:
            audio_hash = get_content_hash(fp)

            if audio_hash in self._tracks_hash:
                return

            metadata = extract_metadata(fp)
            metadata['hash'] = audio_hash

            append_json(metadata)
            self.render_card_list()

    def delete_track(self, track_id: int):
        print('track_id', track_id)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()

    sys.exit(app.exec())

