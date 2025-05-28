import json
import random
from pathlib import Path


class JSON:
    def __init__(self, path):
        self.path = Path(path)

        self.playlist_order = []

        self.restore_order()

    # проверка на существование
    def _check_existence(self):
        if not self.path.exists():
            with open(self.path, 'w'):
                pass

    # записать
    def _write(self, data):
        self._check_existence()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False, default=str)

    # загрузить
    def read(self):
        self._check_existence()
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                return {}

    # восстановить порядок
    def restore_order(self):
        # выглядит небезопасно
        _t = self.read()
        self.playlist_order = list(self.read().keys()) if _t else []

    # перемешать порядок
    def shuffle(self, current_hsh):
        random.shuffle(self.playlist_order)

        if current_hsh in self.playlist_order:
            self.playlist_order.remove(current_hsh)
            self.playlist_order.insert(0, current_hsh)


    # добавление в жсон
    def append(self, data):
        # запись новых данных
        self._write({**self.read(), **data})
        self.playlist_order.append(next(iter(data)))

    # удаление из жсон
    def delete_track(self, track_hash):
        _temp = self.read()

        if track_hash in _temp and track_hash in self.playlist_order:
            del _temp[track_hash]
            self.playlist_order.remove(track_hash)

        self._write(_temp)

    # получить трек по хэшу
    def get_track_by_hash(self, track_hash):

        if track_hash in self.playlist_order:
            return {track_hash: self.read()[track_hash]}
        else:
            return None



