import json
import random
from pathlib import Path


class JSON:
    def __init__(self, path):
        self.path = Path(path)

        self.data = {}
        self.playlist_order = []

        self._read()
        self.restore_order()

    # проверка на существование
    def _check_existence(self):
        if not self.path.exists():
            with open(self.path, 'w'):
                pass

    # записать
    def _write(self):
        self._check_existence()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False, default=str)

    # загрузить
    def _read(self):
        self._check_existence()
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                self.data = json.load(f)
            except json.decoder.JSONDecodeError:
                self.data = {}

    # восстановить порядок
    def restore_order(self):
        self.playlist_order = list(self.data.keys())

    # перемешать порядок
    def shuffle(self, current_hsh):
        random.shuffle(self.playlist_order)

        if current_hsh in self.playlist_order:
            self.playlist_order.remove(current_hsh)
            self.playlist_order.insert(0, current_hsh)


    # добавление в жсон
    def append(self, data):
        self.data.update(data)
        self.playlist_order.append(next(iter(data)))

        # запись новых данных
        self._write()
        # обновление
        self._read()

    # удаление из жсон
    def delete(self, track_hash):
        self._read()

        if track_hash in self.data and track_hash in self.playlist_order:
            del self.data[track_hash]
            self.playlist_order.remove(track_hash)

        self._write()

    # получить трек по хэшу
    def get_track_by_hash(self, track_hash):
        self._read()

        if track_hash in self.data:
            return {track_hash: self.data[track_hash]}
        else:
            return None



