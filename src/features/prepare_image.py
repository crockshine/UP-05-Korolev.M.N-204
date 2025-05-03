import ast
from PySide6.QtGui import QPixmap


def prepare_image(img: str or None):
    pixmap = QPixmap()

    try:
        pixmap.loadFromData(ast.literal_eval(img))
    except Exception as e:
        print(e)
        pixmap.load(':icons/icons/defaultImg.png')

    return pixmap