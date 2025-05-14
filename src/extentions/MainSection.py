from PySide6.QtGui import QPixmap, QPainter, Qt, QImage
from PySide6.QtWidgets import QWidget, QGraphicsBlurEffect, QGraphicsScene, QGraphicsPixmapItem


# Класс, который переопределяет стандартное заполнение заднего фона виджета mainSection
class MainSection(QWidget):
    def __init__(self,
                 parent=None,
                 ):
        super().__init__(parent)

        self.background = None

        self.blur_radius = 50
        self.scale_factor = 1
        self.cached_blur = None

    def update_image(self, pixmap):
        self.background = pixmap
        self.cached_blur = None
        self.update()

    def paintEvent(self, event):
        if not self.background.isNull():
            painter = QPainter(self)

            # 1. Подготовка изображения с размытием (с кэшированием)
            if self.cached_blur is None or self.cached_blur.size() != self.background.size():
                self.cached_blur = self.apply_blur(self.background.toImage(), self.blur_radius)

            # 2. Рассчет масштабирования с эффектом cover + center
            widget_ratio = self.width() / self.height()
            pixmap_ratio = self.cached_blur.width() / self.cached_blur.height()

            # Учитываем scale_factor при расчетах
            target_width = self.width() * self.scale_factor
            target_height = self.height() * self.scale_factor

            if pixmap_ratio > widget_ratio:
                scaled_height = target_height
                scaled_width = self.cached_blur.width() * (scaled_height / self.cached_blur.height())
                x = (self.width() - scaled_width) // 2
                y = (self.height() - scaled_height) // 2
            else:
                scaled_width = target_width
                scaled_height = self.cached_blur.height() * (scaled_width / self.cached_blur.width())
                x = (self.width() - scaled_width) // 2
                y = (self.height() - scaled_height) // 2

            # 3. Отрисовка с плавным масштабированием
            painter.drawPixmap(
                x, y, scaled_width, scaled_height,
                self.cached_blur.scaled(
                    scaled_width, scaled_height,
                    Qt.AspectRatioMode.IgnoreAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

    def apply_blur(self, image, radius):
        """Применяет эффект размытия к изображению"""
        if radius <= 0:
            return QPixmap.fromImage(image)

        result = QImage(image.size(), QImage.Format_ARGB32)
        result.fill(Qt.transparent)

        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(radius)

        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        item.setGraphicsEffect(blur)
        scene.addItem(item)

        painter = QPainter(result)
        scene.render(painter)
        painter.end()

        return QPixmap.fromImage(result)