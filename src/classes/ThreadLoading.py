import time

from PySide6.QtCore import QThread, Signal
from time import sleep

from src.features.extract_metadata import extract_metadata
from src.features.get_content_hash import get_content_hash


class ThreadLoading(QThread):
    ready_track = Signal(dict)
    data_received = Signal(list)

    def __init__(self, db=None):
        super().__init__()
        self.db = db
        self.filepaths = []

        self.data_received.connect(self.add_files)

    def run(self):
        for i, fp in enumerate(self.filepaths):

            audio_hash = get_content_hash(fp)

            if audio_hash in self.db.playlist_order:
                continue

            metadata = extract_metadata(fp)

            track = {audio_hash: metadata}

            self.ready_track.emit(track)
            self.db.add_track(hash_= audio_hash, title=metadata["title"], artist=metadata["artist"], cover=metadata["cover"], filepath=fp)


    def add_files(self, filepaths):
        self.filepaths = filepaths
        self.start()

    def stop(self):
        self.wait()