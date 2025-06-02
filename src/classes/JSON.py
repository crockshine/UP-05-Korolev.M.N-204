import json
import random
from pathlib import Path

from PySide6.QtCore import Signal, QObject

from src.errors.Errors import Errors


class JSON(QObject):
    on_clear = Signal()

    def __init__(self, audio_player, path):
        super().__init__()
        self.path = Path(path)
        self.playlist_order = []
        self.restore_order()
        self.audio_player = audio_player

    def _check_existence(self):
        if not self.path.exists():
            with open(self.path, 'w') as f:
                json.dump([], f)


    def _write(self, data):
        self._check_existence()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False, default=str)


    def read(self):
        self._check_existence()
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if self._validate_playlist(data):
                    return data
                else:
                    raise
            except (json.decoder.JSONDecodeError, Exception):
                self.audio_player.errors.show_JSON_erorr_dialog()
                self.on_clear.emit()
                return []

    def clear_JSON(self):
        self._write([])
        self.playlist_order = []

    def restore_order(self):
        playlist = self.read()
        self.playlist_order = [track["hash"] for track in playlist]

    def update_path(self, hash_, new_path):
        t = self.read()

        _updated = False
        for track in t:
            if track["hash"] == hash_:
                track["source"] = new_path
                _updated = True
                break

        if _updated:
            self._write(t)




    def shuffle(self, current_hsh):
        random.shuffle(self.playlist_order)
        if current_hsh in self.playlist_order:
            self.playlist_order.remove(current_hsh)
            self.playlist_order.insert(0, current_hsh)


    def append(self, data):
        playlist = self.read()
        track_hash = data.get("hash")

        # хотябы один дубликат
        if any(track.get("hash") == track_hash for track in playlist):
            return

        playlist.append(data)
        self._write(playlist)
        self.playlist_order.append(track_hash)


    def delete_track(self, track_hash):
        playlist = self.read()
        updated_playlist = [track for track in playlist if track.get("hash") != track_hash]
        self._write(updated_playlist)

        if track_hash in self.playlist_order:
            self.playlist_order.remove(track_hash)


    def get_track_by_hash(self, track_hash):
        playlist = self.read()
        for track in playlist:
            if track.get("hash") == track_hash:
                return track
        return None


    def _validate_track_data(self, data) -> bool:
        required_keys = {"artist", "title", "source", "cover", "hash"}

        if not all(key in data for key in required_keys):
            return False
        if not isinstance(data["artist"], str):
            return False
        if not isinstance(data["title"], str):
            return False
        if not isinstance(data["source"], str):
            return False
        if not isinstance(data["hash"], str) or len(data["hash"]) != 128:
            return False
        if data["cover"] is not None and not isinstance(data["cover"], str):
            return False

        return True


    def _validate_playlist(self, playlist) -> bool:
        if not isinstance(playlist, list):
            return False

        hashes = []
        for track in playlist:
            if not isinstance(track, dict):
                return False
            if not self._validate_track_data(track):
                return False
            hashes.append(track["hash"])

        if len(hashes) != len(set(hashes)):
            return False

        return True
