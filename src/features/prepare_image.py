import ast
from PySide6.QtGui import QPixmap


def prepare_image(img: str or None):
    """
    :param img: строка байтов или ничего
    :return: кортеж - обложка и задний фон
    """
    cover = QPixmap()
    bg = QPixmap()

    if img is not None:
        cover.loadFromData(img)
        bg.loadFromData(img)
    else:
        cover.load(':icons/icons/defaultImg.png')
        bg.load(':icons/icons/defaultGradient.png')

    return [cover, bg]