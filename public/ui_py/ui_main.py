# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
from public.resources import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1491, 734)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainSection = QWidget(self.centralwidget)
        self.mainSection.setObjectName(u"mainSection")
        sizePolicy.setHeightForWidth(self.mainSection.sizePolicy().hasHeightForWidth())
        self.mainSection.setSizePolicy(sizePolicy)
        self.mainSection.setMinimumSize(QSize(0, 0))
        self.mainSection.setStyleSheet(u"background: qlineargradient(\n"
"    x1:0, y1:1, \n"
"    x2:1, y2:0, \n"
"    stop:0 #FF8080, \n"
"	 stop:0.5 white,\n"
" stop:0.5 white\n"
"    stop:1 #72E4AB\n"
");")
        self.verticalLayout = QVBoxLayout(self.mainSection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.whiteWrapper = QWidget(self.mainSection)
        self.whiteWrapper.setObjectName(u"whiteWrapper")
        sizePolicy.setHeightForWidth(self.whiteWrapper.sizePolicy().hasHeightForWidth())
        self.whiteWrapper.setSizePolicy(sizePolicy)
        self.whiteWrapper.setStyleSheet(u"background: rgba(255,255,255,150);")
        self.verticalLayout_2 = QVBoxLayout(self.whiteWrapper)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headSeaction = QWidget(self.whiteWrapper)
        self.headSeaction.setObjectName(u"headSeaction")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headSeaction.sizePolicy().hasHeightForWidth())
        self.headSeaction.setSizePolicy(sizePolicy1)
        self.headSeaction.setMinimumSize(QSize(0, 60))
        self.headSeaction.setMaximumSize(QSize(16777215, 34))
        self.headSeaction.setStyleSheet(u"background: transparent")
        self.horizontalLayout_5 = QHBoxLayout(self.headSeaction)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, 10, 10)
        self.showHideButton = QPushButton(self.headSeaction)
        self.showHideButton.setObjectName(u"showHideButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showHideButton.sizePolicy().hasHeightForWidth())
        self.showHideButton.setSizePolicy(sizePolicy2)
        self.showHideButton.setMinimumSize(QSize(40, 40))
        self.showHideButton.setMaximumSize(QSize(40, 40))
        self.showHideButton.setBaseSize(QSize(40, 40))
        self.showHideButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.showHideButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.showHideButton.setAutoFillBackground(False)
        self.showHideButton.setStyleSheet(u"background: rgba(255,255,255,150);\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/showHide.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showHideButton.setIcon(icon)
        self.showHideButton.setIconSize(QSize(20, 20))
        self.showHideButton.setFlat(True)

        self.horizontalLayout_5.addWidget(self.showHideButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.headSeaction, 0, Qt.AlignmentFlag.AlignTop)

        self.infoLayout = QWidget(self.whiteWrapper)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setAutoFillBackground(False)
        self.infoLayout.setStyleSheet(u"background: transparent")
        self.verticalLayout_7 = QVBoxLayout(self.infoLayout)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(self.infoLayout)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy3)
        self.imageLabel.setMinimumSize(QSize(0, 300))
        self.imageLabel.setMaximumSize(QSize(300, 300))
        self.imageLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet(u"border-radius: 100")
        self.imageLabel.setPixmap(QPixmap(u":/icons/icons/defaultImg.png"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imageLabel.setOpenExternalLinks(False)

        self.verticalLayout_7.addWidget(self.imageLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.infoGroup = QWidget(self.infoLayout)
        self.infoGroup.setObjectName(u"infoGroup")
        self.infoGroup.setStyleSheet(u"background: none")
        self.verticalLayout_8 = QVBoxLayout(self.infoGroup)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.infoGroup)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"background-color: transparent")
        self.titleLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLabel.setLineWidth(1)
        self.titleLabel.setMidLineWidth(1)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.titleLabel)

        self.authorLabel = QLabel(self.infoGroup)
        self.authorLabel.setObjectName(u"authorLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.authorLabel.setFont(font1)
        self.authorLabel.setStyleSheet(u"background-color: transparent")
        self.authorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.authorLabel.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.authorLabel)


        self.verticalLayout_7.addWidget(self.infoGroup)


        self.verticalLayout_2.addWidget(self.infoLayout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.featureBlock = QWidget(self.whiteWrapper)
        self.featureBlock.setObjectName(u"featureBlock")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.featureBlock.sizePolicy().hasHeightForWidth())
        self.featureBlock.setSizePolicy(sizePolicy4)
        self.featureBlock.setAutoFillBackground(False)
        self.featureBlock.setStyleSheet(u"background-color: white")
        self.verticalLayout_3 = QVBoxLayout(self.featureBlock)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.timeline = QSlider(self.featureBlock)
        self.timeline.setObjectName(u"timeline")
        self.timeline.setMinimumSize(QSize(0, 4))
        self.timeline.setMaximumSize(QSize(16777215, 4))
        self.timeline.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.timeline.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background: #e0e0e0;  /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    height: 4px;\n"
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
        self.timeline.setTracking(True)
        self.timeline.setOrientation(Qt.Orientation.Horizontal)
        self.timeline.setInvertedAppearance(False)
        self.timeline.setInvertedControls(False)

        self.verticalLayout_3.addWidget(self.timeline)

        self.featureLayout = QWidget(self.featureBlock)
        self.featureLayout.setObjectName(u"featureLayout")
        self.horizontalLayout_2 = QHBoxLayout(self.featureLayout)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.randomButton = QPushButton(self.featureLayout)
        self.randomButton.setObjectName(u"randomButton")
        self.randomButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.randomButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.randomButton.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/random.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.randomButton.setIcon(icon1)
        self.randomButton.setIconSize(QSize(20, 20))
        self.randomButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.randomButton)

        self.mainFeatureButtons = QWidget(self.featureLayout)
        self.mainFeatureButtons.setObjectName(u"mainFeatureButtons")
        self.horizontalLayout_4 = QHBoxLayout(self.mainFeatureButtons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.prevButton_2 = QPushButton(self.mainFeatureButtons)
        self.prevButton_2.setObjectName(u"prevButton_2")
        self.prevButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.prevButton_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.prevButton_2.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/prev.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevButton_2.setIcon(icon2)
        self.prevButton_2.setIconSize(QSize(20, 20))
        self.prevButton_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.prevButton_2)

        self.playButton_2 = QPushButton(self.mainFeatureButtons)
        self.playButton_2.setObjectName(u"playButton_2")
        self.playButton_2.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.playButton_2.sizePolicy().hasHeightForWidth())
        self.playButton_2.setSizePolicy(sizePolicy5)
        self.playButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButton_2.setMouseTracking(False)
        self.playButton_2.setTabletTracking(False)
        self.playButton_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.playButton_2.setAutoFillBackground(False)
        self.playButton_2.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playButton_2.setIcon(icon3)
        self.playButton_2.setIconSize(QSize(20, 20))
        self.playButton_2.setAutoDefault(False)
        self.playButton_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.playButton_2)

        self.nextButton = QPushButton(self.mainFeatureButtons)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.nextButton.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setIconSize(QSize(20, 20))
        self.nextButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.horizontalLayout_2.addWidget(self.mainFeatureButtons)

        self.pushButton = QPushButton(self.featureLayout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setTabletTracking(False)
        self.pushButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton.setStyleSheet(u"QPushButton:pressed {\n"
"    border: none;            \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cycle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.featureLayout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.featureBlock, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.whiteWrapper)


        self.horizontalLayout.addWidget(self.mainSection)

        self.playList = QWidget(self.centralwidget)
        self.playList.setObjectName(u"playList")
        self.playList.setStyleSheet(u"background: white")
        self.verticalLayout_4 = QVBoxLayout(self.playList)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.playList)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 725, 669))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: none")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cardList = QVBoxLayout()
        self.cardList.setObjectName(u"cardList")

        self.verticalLayout_5.addLayout(self.cardList)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.buttonLayout = QWidget(self.playList)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.verticalLayout_6 = QVBoxLayout(self.buttonLayout)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addTrackButton = QPushButton(self.buttonLayout)
        self.addTrackButton.setObjectName(u"addTrackButton")
        self.addTrackButton.setMinimumSize(QSize(250, 40))
        self.addTrackButton.setMaximumSize(QSize(250, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.addTrackButton.setFont(font2)
        self.addTrackButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addTrackButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.addTrackButton.setStyleSheet(u"background-color: black;\n"
"    color: white;\n"
"    border: none;")
        self.addTrackButton.setFlat(True)

        self.verticalLayout_6.addWidget(self.addTrackButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.buttonLayout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.playList)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.playButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.showHideButton.setText("")
        self.imageLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Summertime Sudness", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"Laba Del Ray", None))
        self.randomButton.setText("")
        self.prevButton_2.setText("")
        self.playButton_2.setText("")
        self.nextButton.setText("")
        self.pushButton.setText("")
        self.addTrackButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0435\u043a", None))
    # retranslateUi

