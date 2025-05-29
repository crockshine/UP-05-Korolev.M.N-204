from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox, QFileDialog

from src.classes.JSON import JSON

class CannotFindTrack(QObject):
    on_delete = Signal(str)
    def __init__(self, db = None):
        super(CannotFindTrack, self).__init__()
        self.db = db

    def show_cannot_find_dialog(self, title, track_hash):
        msg_box = QMessageBox()


        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(f"{title} не найден")
        msg_box.setInformativeText("Аудиофайл не существует по указанному пути или его данные повреждены.")

        change_path_btn = msg_box.addButton("Изменить путь", QMessageBox.ButtonRole.AcceptRole)
        remove_btn = msg_box.addButton("Удалить", QMessageBox.ButtonRole.DestructiveRole)
        msg_box.addButton(QMessageBox.StandardButton.Cancel)

        msg_box.exec()

        if msg_box.clickedButton() == change_path_btn:
            print("Изменить путь")
            file_path, _ = QFileDialog.getOpenFileName(
                None,
                "Выберите аудиофайл",
                "",
                "Аудиофайл (*.mp3 *.ogg *.flac *.wav)"
            )

            if not file_path:
                return

            self.db.update_path(track_hash, file_path)
        elif msg_box.clickedButton() == remove_btn:
            print("Удалить из плейлиста")
            self.on_delete.emit(track_hash)
        else:
            print("Отмена")


    def show_JSON_erorr_dialog(self):
        msg_box = QMessageBox()

        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText("Ошибка хранения данных")
        msg_box.setInformativeText("Файл, для хранения данных поврежден. Увы, плейлист придется очистить.")

        msg_box.addButton("Ок", QMessageBox.ButtonRole.AcceptRole)

        msg_box.exec()