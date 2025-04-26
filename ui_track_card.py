# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_track_card.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_TrackCard(object):
    def setupUi(self, TrackCard):
        if not TrackCard.objectName():
            TrackCard.setObjectName(u"TrackCard")
        TrackCard.resize(606, 173)
        TrackCard.setStyleSheet(u"background: white")
        self.horizontalLayout = QHBoxLayout(TrackCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.trackImage = QLabel(TrackCard)
        self.trackImage.setObjectName(u"trackImage")
        self.trackImage.setMinimumSize(QSize(50, 50))
        self.trackImage.setMaximumSize(QSize(50, 50))
        self.trackImage.setStyleSheet(u"background: grey\n"
"")

        self.horizontalLayout.addWidget(self.trackImage)

        self.infoBlock = QWidget(TrackCard)
        self.infoBlock.setObjectName(u"infoBlock")
        self.infoBlock.setMinimumSize(QSize(0, 50))
        self.infoBlock.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout = QVBoxLayout(self.infoBlock)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.infoBlock)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.author = QLabel(self.infoBlock)
        self.author.setObjectName(u"author")
        self.author.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.author.setWordWrap(True)

        self.verticalLayout.addWidget(self.author, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.infoBlock)

        self.pushButton = QPushButton(TrackCard)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"border: none")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(TrackCard)

        QMetaObject.connectSlotsByName(TrackCard)
    # setupUi

    def retranslateUi(self, TrackCard):
        TrackCard.setWindowTitle(QCoreApplication.translate("TrackCard", u"Form", None))
        self.trackImage.setText("")
        self.title.setText(QCoreApplication.translate("TrackCard", u"\u0411\u0435\u0437 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f", None))
        self.author.setText(QCoreApplication.translate("TrackCard", u"\u0410\u0432\u0442\u043e\u0440 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d", None))
        self.pushButton.setText("")
    # retranslateUi

