import ast
from PySide6.QtGui import QPixmap


def prepare_image(img: str or None):
    """
    :param img: строка байтов или ничего
    :return: кортеж - обложка и задний фон
    """
    cover = QPixmap()
    bg = QPixmap()
    try:
        if img is None:
            cover.load(':icons/icons/defaultImg.png')
            bg.load(':icons/icons/defaultGradient.png')
        else:
            _img = ast.literal_eval(str(img))

            if not cover.loadFromData(_img):
                raise ValueError()
            if not bg.loadFromData(_img):
                raise ValueError()

    except Exception as e:
        print('исключение', e)
        cover.load(':icons/icons/defaultImg.png')
        bg.load(':icons/icons/defaultGradient.png')

    return [cover, bg]