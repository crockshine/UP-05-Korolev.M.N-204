import json
import random
import time
from pathlib import Path
import sqlite3

db_path = 'music.db'
db_name = 'Playlist'
fields = ["hash_", "title", "artist", "cover", "filepath"]
expected_schema = [
    {"name": "hash_", "type": "TEXT", "notnull": 1},
    {"name": "title", "type": "TEXT", "notnull": 1},
    {"name": "artist", "type": "TEXT", "notnull": 1},
    {"name": "cover", "type": "BLOB", "notnull": 0},
    {"name": "filepath", "type": "TEXT", "notnull": 1},
]

class JSON:
    def __init__(self):
        self._init_db()

        self.playlist_order = []
        self.get_playlist_order()

    # TODO создание бд, если ошибка - пересоздать, ,получение по хэшу, удаление по хэшу,

    def _init_db(self):
        with sqlite3.connect(db_path) as connection:
            # создание таблицы
            self._create_table(connection)

            # проверка целостности таблицы
            if not self._check_integrity(connection):
                self._restore_table(connection)

            connection.execute("CREATE INDEX IF NOT EXISTS idx_hash ON Playlist (hash_)")

    def _check_integrity(self, connection):
        cursor = connection.cursor()
        try:
            # проверка существования таблицы
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (db_name,))
            if not cursor.fetchone():
                print('таблицы нет')
                return False

            # проверка типов данных
            cursor.execute(f"PRAGMA table_info({db_name})")
            actual_columns = cursor.fetchall()

            for expected, actual in zip(expected_schema, actual_columns):
                _, name, col_type, notnull, _, _ = actual
                if (
                        name != expected["name"]
                        or col_type.upper() != expected["type"]
                        or notnull != expected["notnull"]
                ):
                    print('несоответсвие типов данных')
                    return False



            return True
        except sqlite3.OperationalError:
            print('ошибка чтения')
            return False


    def _restore_table(self, connection):
        cursor = connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS Playlist''')
        self._create_table(connection)


    def _create_table(self, connection):
        cursor = connection.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Playlist
                       (
                           hash_
                           TEXT
                           PRIMARY
                           KEY
                           NOT NULL
                           ,
                           title
                           TEXT
                           NOT
                           NULL,
                           artist
                           TEXT
                           NOT
                           NULL,
                           cover
                           BLOB,
                           filepath
                           TEXT
                           NOT
                           NULL
                           UNIQUE
                       )
                       ''')


    def get_playlist_order(self):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if not self._check_integrity(connection):
                self._restore_table(connection)

            try:
                cursor.execute('SELECT hash_ FROM Playlist')
                self.playlist_order = list(map(lambda x: x[0], cursor.fetchall()))
            except sqlite3.OperationalError:
                self.playlist_order = []


    def get_all_tracks(self):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if not self._check_integrity(connection):
                self._restore_table(connection)

            try:
                cursor.execute("SELECT * FROM Playlist")
                return cursor.fetchall()
            except sqlite3.IntegrityError:
                self._restore_table(connection)
                return []

    def add_track(self, hash_, title, artist, cover, filepath):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if not self._check_integrity(connection):
                self._restore_table(connection)

            try:
                cursor.execute("INSERT INTO Playlist (hash_, title, artist, cover, filepath) VALUES(?, ?, ?, ?, ?)",
                               (hash_, title, artist, cover, filepath))
                self.playlist_order.append(hash_)
                return True
            except sqlite3.IntegrityError:
                self._restore_table(connection)
                return self.add_track(hash_, title, artist, cover, filepath)

    def delete_track(self, hash_):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if not self._check_integrity(connection):
                self._restore_table(connection)

            try:

                cursor.execute("DELETE FROM Playlist WHERE hash_ = ?",(hash_,))
                self.playlist_order.remove(hash_)


                return True
            except sqlite3.IntegrityError:
                self._restore_table(connection)
                return False


    def get_track_by_hash(self, track_hash):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM Playlist WHERE hash_=?", (track_hash,))
                hash_, title, artist, cover, filepath   = cursor.fetchone()
                return {'hash': hash_, 'title': title, 'artist': artist, 'cover': cover, 'filepath': filepath}
            except sqlite3.OperationalError:
                # не удалось взять трек
                return None


    def shuffle(self, current_hsh):
        random.shuffle(self.playlist_order)

        if current_hsh in self.playlist_order:
            self.playlist_order.remove(current_hsh)
            self.playlist_order.insert(0, current_hsh)










