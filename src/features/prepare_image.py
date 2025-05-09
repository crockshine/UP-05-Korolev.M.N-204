import ast
from PySide6.QtGui import QPixmap


def prepare_image(img: str or None):
    cover = QPixmap()
    bg = QPixmap()

    try:
        _img = ast.literal_eval(img)
        cover.loadFromData(_img)
        bg.loadFromData(_img)
    except Exception as e:
        print(e)
        cover.load(':icons/icons/defaultImg.png')
        bg.load(':icons/icons/defaultGradient.png')


    return [cover, bg]