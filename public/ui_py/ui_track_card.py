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
from public.resources import res_rc

class Ui_TrackCardWrapper(object):
    def setupUi(self, TrackCardWrapper):
        if not TrackCardWrapper.objectName():
            TrackCardWrapper.setObjectName(u"TrackCardWrapper")
        TrackCardWrapper.resize(636, 120)
        TrackCardWrapper.setMinimumSize(QSize(0, 0))
        TrackCardWrapper.setMaximumSize(QSize(16777215, 120))
        TrackCardWrapper.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        TrackCardWrapper.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(TrackCardWrapper)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TrackCard = QWidget(TrackCardWrapper)
        self.TrackCard.setObjectName(u"TrackCard")
        self.TrackCard.setMaximumSize(QSize(16777215, 16777215))
        self.TrackCard.setStyleSheet(u"border-bottom: 1px solid rgba(0,0,0,50);\n"
"background: white\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.TrackCard)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.trackImage = QLabel(self.TrackCard)
        self.trackImage.setObjectName(u"trackImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackImage.sizePolicy().hasHeightForWidth())
        self.trackImage.setSizePolicy(sizePolicy)
        self.trackImage.setMinimumSize(QSize(45, 45))
        self.trackImage.setMaximumSize(QSize(45, 45))
        self.trackImage.setStyleSheet(u"border: none")
        self.trackImage.setPixmap(QPixmap(u":/icons/icons/defaultImg.png"))
        self.trackImage.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.trackImage, 0, Qt.AlignmentFlag.AlignVCenter)

        self.infoBlock = QWidget(self.TrackCard)
        self.infoBlock.setObjectName(u"infoBlock")
        self.infoBlock.setMinimumSize(QSize(0, 50))
        self.infoBlock.setMaximumSize(QSize(16777215, 16777215))
        self.infoBlock.setStyleSheet(u"border: none;\n"
"border-radius: 0;\n"
"color: black;\n"
"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.infoBlock)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.infoBlock)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.artist = QLabel(self.infoBlock)
        self.artist.setObjectName(u"artist")
        font1 = QFont()
        font1.setPointSize(13)
        self.artist.setFont(font1)
        self.artist.setStyleSheet(u"")
        self.artist.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.artist.setWordWrap(True)

        self.verticalLayout.addWidget(self.artist, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.infoBlock, 0, Qt.AlignmentFlag.AlignVCenter)

        self.delete_button = QPushButton(self.TrackCard)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(40, 40))
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setStyleSheet(u"border: none;\n"
"background: transparent")
        icon = QIcon()
        icon.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_button.setIcon(icon)
        self.delete_button.setIconSize(QSize(20, 20))
        self.delete_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.delete_button, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.TrackCard, 0, Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(TrackCardWrapper)

        QMetaObject.connectSlotsByName(TrackCardWrapper)
    # setupUi

    def retranslateUi(self, TrackCardWrapper):
        TrackCardWrapper.setWindowTitle(QCoreApplication.translate("TrackCardWrapper", u"Form", None))
        self.trackImage.setText("")
        self.title.setText(QCoreApplication.translate("TrackCardWrapper", u"\u0411\u0435\u0437 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f", None))
        self.artist.setText(QCoreApplication.translate("TrackCardWrapper", u"\u0410\u0432\u0442\u043e\u0440 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d", None))
        self.delete_button.setText("")
    # retranslateUi

