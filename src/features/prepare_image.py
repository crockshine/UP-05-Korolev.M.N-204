import ast
from PySide6.QtGui import QPixmap


def prepare_image(img: str or None):
    """
    :param img: строка байтов или ничего
    :return: кортеж - обложка и задний фон
    """
    cover = QPixmap()
    bg = QPixmap()

    if img is None:
        cover.load(':icons/icons/defaultImg.png')
        bg.load(':icons/icons/defaultGradient.png')
    else:
        try:
            _img = ast.literal_eval(str(img))
            cover.loadFromData(_img)
            bg.loadFromData(_img)
        except Exception as e:
            print('исключение', e)
            cover.load(':icons/icons/defaultImg.png')
            bg.load(':icons/icons/defaultGradient.png')

    return [cover, bg]