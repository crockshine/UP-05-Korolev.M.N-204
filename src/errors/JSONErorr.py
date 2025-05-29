from PySide6.QtWidgets import QMessageBox


def show_JSON_erorr_dialog():
    msg_box = QMessageBox()

    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setWindowTitle("Ошибка")
    msg_box.setText("Ошибка хранения данных")
    msg_box.setInformativeText("Файл, для хранения данных поврежден. Увы, плейлист придется очистить.")

    msg_box.addButton("Ок", QMessageBox.ButtonRole.AcceptRole)

    msg_box.exec()
