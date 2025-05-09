import json
from pathlib import Path


class JSON:
    def __init__(self, path):
        self.path = Path(path)
        self.data = {}
        self.playlist_order = []

    def _check_existence(self):
        if not self.path.exists():
            with open(self.path, 'w'):
                pass

    # проверка, запись в жсон
    def _save(self):
        self._check_existence()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False, default=str)

    # загрузить
    def load(self):
        self._check_existence()
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                t = json.load(f)
                self.playlist_order = []
                for key in t:
                    self.playlist_order.append(key)
                return t
            except json.decoder.JSONDecodeError:
                self.playlist_order = []
                return {}

    # добавление в жсон
    def append(self, data):
        self.data = self.load()
        self.data.update(data)
        self._save()

    # удаление из жсон
    def delete(self, track_hash):
        self.data = self.load()
        _t = {}
        for _track in self.data:
            if _track != track_hash:
                _t.update({_track: self.data[_track]})
        self.data = _t
        self._save()

    def get_track_by_hash(self, track_hash):
        self.data = self.load()
        for _track in self.data:
            if _track == track_hash:
                return {_track: self.data[_track]}
        return None


