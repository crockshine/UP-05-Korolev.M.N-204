# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_sound_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)
from public.resources import res_rc

class Ui_sound_settings(object):
    def setupUi(self, sound_settings):
        if not sound_settings.objectName():
            sound_settings.setObjectName(u"sound_settings")
        sound_settings.resize(400, 300)
        sound_settings.setMinimumSize(QSize(400, 300))
        sound_settings.setMaximumSize(QSize(400, 300))
        self.centralwidget = QWidget(sound_settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 300))
        self.centralwidget.setMaximumSize(QSize(400, 300))
        self.centralwidget.setStyleSheet(u"background-color: white; color: black")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.equalizer = QWidget(self.centralwidget)
        self.equalizer.setObjectName(u"equalizer")
        self.horizontalLayout_3 = QHBoxLayout(self.equalizer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_12 = QLabel(self.equalizer)
        self.title_12.setObjectName(u"title_12")
        self.title_12.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_12.setFont(font)
        self.title_12.setStyleSheet(u"background-color: transparent")
        self.title_12.setFrameShadow(QFrame.Shadow.Raised)
        self.title_12.setLineWidth(1)
        self.title_12.setMidLineWidth(1)
        self.title_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_12.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.title_12)

        self.reset_eq = QPushButton(self.equalizer)
        self.reset_eq.setObjectName(u"reset_eq")
        self.reset_eq.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_eq.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reset_eq.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/reset.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset_eq.setIcon(icon)
        self.reset_eq.setIconSize(QSize(20, 20))
        self.reset_eq.setFlat(True)

        self.horizontalLayout_3.addWidget(self.reset_eq, 0, Qt.AlignmentFlag.AlignRight)

        self.apply_eq = QPushButton(self.equalizer)
        self.apply_eq.setObjectName(u"apply_eq")
        self.apply_eq.setMinimumSize(QSize(100, 30))
        self.apply_eq.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.apply_eq.setFont(font1)
        self.apply_eq.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apply_eq.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.apply_eq.setStyleSheet(u"background-color: black;\n"
"    color: white;\n"
"    border: none;")
        self.apply_eq.setFlat(True)

        self.horizontalLayout_3.addWidget(self.apply_eq)


        self.verticalLayout_11.addWidget(self.equalizer)

        self.slider_container = QWidget(self.centralwidget)
        self.slider_container.setObjectName(u"slider_container")
        self.horizontalLayout_2 = QHBoxLayout(self.slider_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cont_60 = QWidget(self.slider_container)
        self.cont_60.setObjectName(u"cont_60")
        self.verticalLayout = QVBoxLayout(self.cont_60)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.eq_60 = QSlider(self.cont_60)
        self.eq_60.setObjectName(u"eq_60")
        self.eq_60.setMinimumSize(QSize(6, 6))
        self.eq_60.setMaximumSize(QSize(6, 16777215))
        self.eq_60.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_60.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_60.setMaximum(100)
        self.eq_60.setValue(50)
        self.eq_60.setTracking(True)
        self.eq_60.setOrientation(Qt.Orientation.Vertical)
        self.eq_60.setInvertedAppearance(False)
        self.eq_60.setInvertedControls(True)

        self.verticalLayout.addWidget(self.eq_60, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_2 = QLabel(self.cont_60)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.title_2.setFont(font2)
        self.title_2.setStyleSheet(u"background-color: transparent")
        self.title_2.setFrameShadow(QFrame.Shadow.Raised)
        self.title_2.setLineWidth(1)
        self.title_2.setMidLineWidth(1)
        self.title_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.title_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_60)

        self.cont_170 = QWidget(self.slider_container)
        self.cont_170.setObjectName(u"cont_170")
        self.verticalLayout_2 = QVBoxLayout(self.cont_170)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.eq_170 = QSlider(self.cont_170)
        self.eq_170.setObjectName(u"eq_170")
        self.eq_170.setMinimumSize(QSize(6, 6))
        self.eq_170.setMaximumSize(QSize(6, 16777215))
        self.eq_170.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_170.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_170.setMaximum(100)
        self.eq_170.setValue(50)
        self.eq_170.setTracking(True)
        self.eq_170.setOrientation(Qt.Orientation.Vertical)
        self.eq_170.setInvertedAppearance(False)
        self.eq_170.setInvertedControls(True)

        self.verticalLayout_2.addWidget(self.eq_170, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_3 = QLabel(self.cont_170)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setMaximumSize(QSize(16777215, 16777215))
        self.title_3.setFont(font2)
        self.title_3.setStyleSheet(u"background-color: transparent")
        self.title_3.setFrameShadow(QFrame.Shadow.Raised)
        self.title_3.setLineWidth(1)
        self.title_3.setMidLineWidth(1)
        self.title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.title_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_170)

        self.cont_310 = QWidget(self.slider_container)
        self.cont_310.setObjectName(u"cont_310")
        self.verticalLayout_3 = QVBoxLayout(self.cont_310)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.eq_310 = QSlider(self.cont_310)
        self.eq_310.setObjectName(u"eq_310")
        self.eq_310.setMinimumSize(QSize(6, 6))
        self.eq_310.setMaximumSize(QSize(6, 16777215))
        self.eq_310.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_310.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_310.setMaximum(100)
        self.eq_310.setValue(50)
        self.eq_310.setTracking(True)
        self.eq_310.setOrientation(Qt.Orientation.Vertical)
        self.eq_310.setInvertedAppearance(False)
        self.eq_310.setInvertedControls(True)

        self.verticalLayout_3.addWidget(self.eq_310, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_4 = QLabel(self.cont_310)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setMaximumSize(QSize(16777215, 16777215))
        self.title_4.setFont(font2)
        self.title_4.setStyleSheet(u"background-color: transparent")
        self.title_4.setFrameShadow(QFrame.Shadow.Raised)
        self.title_4.setLineWidth(1)
        self.title_4.setMidLineWidth(1)
        self.title_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.title_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_310)

        self.cont_600 = QWidget(self.slider_container)
        self.cont_600.setObjectName(u"cont_600")
        self.verticalLayout_4 = QVBoxLayout(self.cont_600)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.eq_600 = QSlider(self.cont_600)
        self.eq_600.setObjectName(u"eq_600")
        self.eq_600.setMinimumSize(QSize(6, 6))
        self.eq_600.setMaximumSize(QSize(6, 16777215))
        self.eq_600.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_600.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_600.setMaximum(100)
        self.eq_600.setValue(50)
        self.eq_600.setTracking(True)
        self.eq_600.setOrientation(Qt.Orientation.Vertical)
        self.eq_600.setInvertedAppearance(False)
        self.eq_600.setInvertedControls(True)

        self.verticalLayout_4.addWidget(self.eq_600, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_5 = QLabel(self.cont_600)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setMaximumSize(QSize(16777215, 16777215))
        self.title_5.setFont(font2)
        self.title_5.setStyleSheet(u"background-color: transparent")
        self.title_5.setFrameShadow(QFrame.Shadow.Raised)
        self.title_5.setLineWidth(1)
        self.title_5.setMidLineWidth(1)
        self.title_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.title_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_600)

        self.cont_1k = QWidget(self.slider_container)
        self.cont_1k.setObjectName(u"cont_1k")
        self.verticalLayout_5 = QVBoxLayout(self.cont_1k)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.eq_1000 = QSlider(self.cont_1k)
        self.eq_1000.setObjectName(u"eq_1000")
        self.eq_1000.setMinimumSize(QSize(6, 6))
        self.eq_1000.setMaximumSize(QSize(6, 16777215))
        self.eq_1000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_1000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_1000.setMaximum(100)
        self.eq_1000.setValue(50)
        self.eq_1000.setTracking(True)
        self.eq_1000.setOrientation(Qt.Orientation.Vertical)
        self.eq_1000.setInvertedAppearance(False)
        self.eq_1000.setInvertedControls(True)

        self.verticalLayout_5.addWidget(self.eq_1000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_6 = QLabel(self.cont_1k)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setMaximumSize(QSize(16777215, 16777215))
        self.title_6.setFont(font2)
        self.title_6.setStyleSheet(u"background-color: transparent")
        self.title_6.setFrameShadow(QFrame.Shadow.Raised)
        self.title_6.setLineWidth(1)
        self.title_6.setMidLineWidth(1)
        self.title_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_6.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.title_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_1k)

        self.cont_3k = QWidget(self.slider_container)
        self.cont_3k.setObjectName(u"cont_3k")
        self.verticalLayout_6 = QVBoxLayout(self.cont_3k)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.eq_3000 = QSlider(self.cont_3k)
        self.eq_3000.setObjectName(u"eq_3000")
        self.eq_3000.setMinimumSize(QSize(6, 6))
        self.eq_3000.setMaximumSize(QSize(6, 16777215))
        self.eq_3000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_3000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_3000.setMaximum(100)
        self.eq_3000.setValue(50)
        self.eq_3000.setTracking(True)
        self.eq_3000.setOrientation(Qt.Orientation.Vertical)
        self.eq_3000.setInvertedAppearance(False)
        self.eq_3000.setInvertedControls(True)

        self.verticalLayout_6.addWidget(self.eq_3000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_7 = QLabel(self.cont_3k)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setMaximumSize(QSize(16777215, 16777215))
        self.title_7.setFont(font2)
        self.title_7.setStyleSheet(u"background-color: transparent")
        self.title_7.setFrameShadow(QFrame.Shadow.Raised)
        self.title_7.setLineWidth(1)
        self.title_7.setMidLineWidth(1)
        self.title_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_7.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.title_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_3k)

        self.cont_6k = QWidget(self.slider_container)
        self.cont_6k.setObjectName(u"cont_6k")
        self.verticalLayout_7 = QVBoxLayout(self.cont_6k)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.eq_6000 = QSlider(self.cont_6k)
        self.eq_6000.setObjectName(u"eq_6000")
        self.eq_6000.setMinimumSize(QSize(6, 6))
        self.eq_6000.setMaximumSize(QSize(6, 16777215))
        self.eq_6000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_6000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_6000.setMaximum(100)
        self.eq_6000.setValue(50)
        self.eq_6000.setTracking(True)
        self.eq_6000.setOrientation(Qt.Orientation.Vertical)
        self.eq_6000.setInvertedAppearance(False)
        self.eq_6000.setInvertedControls(True)

        self.verticalLayout_7.addWidget(self.eq_6000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_8 = QLabel(self.cont_6k)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setMaximumSize(QSize(16777215, 16777215))
        self.title_8.setFont(font2)
        self.title_8.setStyleSheet(u"background-color: transparent")
        self.title_8.setFrameShadow(QFrame.Shadow.Raised)
        self.title_8.setLineWidth(1)
        self.title_8.setMidLineWidth(1)
        self.title_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.title_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_6k)

        self.cont_12k = QWidget(self.slider_container)
        self.cont_12k.setObjectName(u"cont_12k")
        self.verticalLayout_8 = QVBoxLayout(self.cont_12k)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.eq_12000 = QSlider(self.cont_12k)
        self.eq_12000.setObjectName(u"eq_12000")
        self.eq_12000.setMinimumSize(QSize(6, 6))
        self.eq_12000.setMaximumSize(QSize(6, 16777215))
        self.eq_12000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_12000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_12000.setMaximum(100)
        self.eq_12000.setValue(50)
        self.eq_12000.setTracking(True)
        self.eq_12000.setOrientation(Qt.Orientation.Vertical)
        self.eq_12000.setInvertedAppearance(False)
        self.eq_12000.setInvertedControls(True)

        self.verticalLayout_8.addWidget(self.eq_12000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_9 = QLabel(self.cont_12k)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setMaximumSize(QSize(16777215, 16777215))
        self.title_9.setFont(font2)
        self.title_9.setStyleSheet(u"background-color: transparent")
        self.title_9.setFrameShadow(QFrame.Shadow.Raised)
        self.title_9.setLineWidth(1)
        self.title_9.setMidLineWidth(1)
        self.title_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_9.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.title_9, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_12k)

        self.cont_14k = QWidget(self.slider_container)
        self.cont_14k.setObjectName(u"cont_14k")
        self.verticalLayout_9 = QVBoxLayout(self.cont_14k)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.eq_14000 = QSlider(self.cont_14k)
        self.eq_14000.setObjectName(u"eq_14000")
        self.eq_14000.setMinimumSize(QSize(6, 6))
        self.eq_14000.setMaximumSize(QSize(6, 16777215))
        self.eq_14000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_14000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_14000.setMaximum(100)
        self.eq_14000.setValue(50)
        self.eq_14000.setTracking(True)
        self.eq_14000.setOrientation(Qt.Orientation.Vertical)
        self.eq_14000.setInvertedAppearance(False)
        self.eq_14000.setInvertedControls(True)

        self.verticalLayout_9.addWidget(self.eq_14000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_10 = QLabel(self.cont_14k)
        self.title_10.setObjectName(u"title_10")
        self.title_10.setMaximumSize(QSize(16777215, 16777215))
        self.title_10.setFont(font2)
        self.title_10.setStyleSheet(u"background-color: transparent")
        self.title_10.setFrameShadow(QFrame.Shadow.Raised)
        self.title_10.setLineWidth(1)
        self.title_10.setMidLineWidth(1)
        self.title_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_10.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.title_10, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_14k)

        self.cont_16k = QWidget(self.slider_container)
        self.cont_16k.setObjectName(u"cont_16k")
        self.verticalLayout_10 = QVBoxLayout(self.cont_16k)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.eq_16000 = QSlider(self.cont_16k)
        self.eq_16000.setObjectName(u"eq_16000")
        self.eq_16000.setMinimumSize(QSize(6, 6))
        self.eq_16000.setMaximumSize(QSize(6, 16777215))
        self.eq_16000.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eq_16000.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: black;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    weight: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #e0e0e0;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.eq_16000.setMaximum(100)
        self.eq_16000.setValue(50)
        self.eq_16000.setTracking(True)
        self.eq_16000.setOrientation(Qt.Orientation.Vertical)
        self.eq_16000.setInvertedAppearance(False)
        self.eq_16000.setInvertedControls(True)

        self.verticalLayout_10.addWidget(self.eq_16000, 0, Qt.AlignmentFlag.AlignHCenter)

        self.title_11 = QLabel(self.cont_16k)
        self.title_11.setObjectName(u"title_11")
        self.title_11.setMaximumSize(QSize(16777215, 16777215))
        self.title_11.setFont(font2)
        self.title_11.setStyleSheet(u"background-color: transparent")
        self.title_11.setFrameShadow(QFrame.Shadow.Raised)
        self.title_11.setLineWidth(1)
        self.title_11.setMidLineWidth(1)
        self.title_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_11.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.title_11, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.cont_16k)


        self.verticalLayout_11.addWidget(self.slider_container)

        self.volume = QWidget(self.centralwidget)
        self.volume.setObjectName(u"volume")
        self.horizontalLayout = QHBoxLayout(self.volume)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.volume)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: transparent")
        self.title.setFrameShadow(QFrame.Shadow.Raised)
        self.title.setLineWidth(1)
        self.title.setMidLineWidth(1)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)

        self.horizontalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_11.addWidget(self.volume)

        self.volume_slider = QSlider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMinimumSize(QSize(0, 6))
        self.volume_slider.setMaximumSize(QSize(16777215, 6))
        self.volume_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.volume_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background: #e0e0e0;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    height: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;    /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 0px;          /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n"
"    margin: -8px 0;\n"
"}")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(80)
        self.volume_slider.setTracking(True)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)
        self.volume_slider.setInvertedAppearance(False)
        self.volume_slider.setInvertedControls(False)

        self.verticalLayout_11.addWidget(self.volume_slider)

        sound_settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(sound_settings)

        QMetaObject.connectSlotsByName(sound_settings)
    # setupUi

    def retranslateUi(self, sound_settings):
        sound_settings.setWindowTitle(QCoreApplication.translate("sound_settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0437\u0432\u0443\u043a\u0430", None))
        self.title_12.setText(QCoreApplication.translate("sound_settings", u"\u042d\u043a\u0432\u0430\u043b\u0430\u0439\u0437\u0435\u0440", None))
        self.reset_eq.setText("")
        self.apply_eq.setText(QCoreApplication.translate("sound_settings", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.title_2.setText(QCoreApplication.translate("sound_settings", u"60", None))
        self.title_3.setText(QCoreApplication.translate("sound_settings", u"170", None))
        self.title_4.setText(QCoreApplication.translate("sound_settings", u"310", None))
        self.title_5.setText(QCoreApplication.translate("sound_settings", u"600", None))
        self.title_6.setText(QCoreApplication.translate("sound_settings", u"1k", None))
        self.title_7.setText(QCoreApplication.translate("sound_settings", u"3k", None))
        self.title_8.setText(QCoreApplication.translate("sound_settings", u"6k", None))
        self.title_9.setText(QCoreApplication.translate("sound_settings", u"12k", None))
        self.title_10.setText(QCoreApplication.translate("sound_settings", u"14k", None))
        self.title_11.setText(QCoreApplication.translate("sound_settings", u"16k", None))
        self.title.setText(QCoreApplication.translate("sound_settings", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c", None))
    # retranslateUi

