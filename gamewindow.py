# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoGamercxapX.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from inventory import Inventory
from mapview import (MapView,MapLabel)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(600, 589)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window.sizePolicy().hasHeightForWidth())
        Window.setSizePolicy(sizePolicy)
        Window.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(16)
        Window.setFont(font)
        Window.setWindowOpacity(-4.000000000000000)
        Window.setToolTipDuration(-6)
        self.horizontalLayout = QHBoxLayout(Window)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Tabs = QStackedWidget(Window)
        self.Tabs.setObjectName(u"Tabs")
        self.MainMenu = QWidget()
        self.MainMenu.setObjectName(u"MainMenu")
        self.MainMenu.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.MainMenu)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.Game_Label = QLabel(self.MainMenu)
        self.Game_Label.setObjectName(u"Game_Label")
        font1 = QFont()
        font1.setFamilies([u"Fira Sans Condensed SemiBold"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.Game_Label.setFont(font1)
        self.Game_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.Game_Label.setMargin(40)
        self.Game_Label.setIndent(-1)
        self.Game_Label.setOpenExternalLinks(False)

        self.verticalLayout_2.addWidget(self.Game_Label)

        self.NewGame = QPushButton(self.MainMenu)
        self.NewGame.setObjectName(u"NewGame")
        font2 = QFont()
        font2.setFamilies([u"Fira Sans"])
        font2.setPointSize(16)
        self.NewGame.setFont(font2)
        self.NewGame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.NewGame)

        self.LoadGame = QPushButton(self.MainMenu)
        self.LoadGame.setObjectName(u"LoadGame")
        self.LoadGame.setEnabled(False)
        self.LoadGame.setFont(font2)
        self.LoadGame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LoadGame.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.LoadGame)

        self.Options = QPushButton(self.MainMenu)
        self.Options.setObjectName(u"Options")
        self.Options.setFont(font2)
        self.Options.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Options)

        self.Quit = QPushButton(self.MainMenu)
        self.Quit.setObjectName(u"Quit")
        self.Quit.setFont(font2)
        self.Quit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Quit)

        self.Empty = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.Empty)

        self.DevBtn = QPushButton(self.MainMenu)
        self.DevBtn.setObjectName(u"DevBtn")

        self.verticalLayout_2.addWidget(self.DevBtn)

        self.Tabs.addWidget(self.MainMenu)
        self.OptionsMenu = QWidget()
        self.OptionsMenu.setObjectName(u"OptionsMenu")
        self.verticalLayout = QVBoxLayout(self.OptionsMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Menu_Title = QHBoxLayout()
        self.Menu_Title.setObjectName(u"Menu_Title")
        self.Options_Label = QLabel(self.OptionsMenu)
        self.Options_Label.setObjectName(u"Options_Label")
        sizePolicy.setHeightForWidth(self.Options_Label.sizePolicy().hasHeightForWidth())
        self.Options_Label.setSizePolicy(sizePolicy)
        self.Options_Label.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Fira Sans"])
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setKerning(False)
        self.Options_Label.setFont(font3)
        self.Options_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.Menu_Title.addWidget(self.Options_Label)


        self.verticalLayout.addLayout(self.Menu_Title)

        self.Settings = QFormLayout()
        self.Settings.setObjectName(u"Settings")
        self.TextSpeed_SpinBox = QSpinBox(self.OptionsMenu)
        self.TextSpeed_SpinBox.setObjectName(u"TextSpeed_SpinBox")
        self.TextSpeed_SpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TextSpeed_SpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.TextSpeed_SpinBox.setMinimum(1)
        self.TextSpeed_SpinBox.setMaximum(10)
        self.TextSpeed_SpinBox.setValue(5)

        self.Settings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TextSpeed_SpinBox)

        self.TextSpeed_Label = QLabel(self.OptionsMenu)
        self.TextSpeed_Label.setObjectName(u"TextSpeed_Label")

        self.Settings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.TextSpeed_Label)


        self.verticalLayout.addLayout(self.Settings)

        self.LeaveOptions = QPushButton(self.OptionsMenu)
        self.LeaveOptions.setObjectName(u"LeaveOptions")
        self.LeaveOptions.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"Fira Sans"])
        font4.setPointSize(14)
        self.LeaveOptions.setFont(font4)
        self.LeaveOptions.setAutoDefault(False)
        self.LeaveOptions.setFlat(False)

        self.verticalLayout.addWidget(self.LeaveOptions)

        self.Empty_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.Empty_2)

        self.Tabs.addWidget(self.OptionsMenu)
        self.GamePlay = QWidget()
        self.GamePlay.setObjectName(u"GamePlay")
        self.TextLog = QTextBrowser(self.GamePlay)
        self.TextLog.setObjectName(u"TextLog")
        self.TextLog.setGeometry(QRect(0, 271, 591, 251))
        self.SaveAndQuit = QPushButton(self.GamePlay)
        self.SaveAndQuit.setObjectName(u"SaveAndQuit")
        self.SaveAndQuit.setGeometry(QRect(180, 220, 226, 46))
        self.InventoryBtn = QPushButton(self.GamePlay)
        self.InventoryBtn.setObjectName(u"InventoryBtn")
        self.InventoryBtn.setGeometry(QRect(20, 528, 180, 30))
        self.MapMenuButton = QPushButton(self.GamePlay)
        self.MapMenuButton.setObjectName(u"MapMenuButton")
        self.MapMenuButton.setGeometry(QRect(380, 528, 180, 30))
        self.idfk = QPushButton(self.GamePlay)
        self.idfk.setObjectName(u"idfk")
        self.idfk.setGeometry(QRect(214, 528, 150, 30))
        self.Tabs.addWidget(self.GamePlay)
        self.Inventory = Inventory()
        self.Inventory.setObjectName(u"Inventory")
        self.Tabs.addWidget(self.Inventory)
        self.Map = MapView()
        self.Map.setObjectName(u"Map")
        self.MapLabel = MapLabel(self.Map)
        self.MapLabel.setObjectName(u"MapLabel")
        self.MapLabel.setGeometry(QRect(0, 10, 590, 20))
        self.MapLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MapLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MapLabel.raise_()
        self.MapLabel.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.Tabs.addWidget(self.Map)

        self.horizontalLayout.addWidget(self.Tabs)

        QWidget.setTabOrder(self.Quit, self.LoadGame)
        QWidget.setTabOrder(self.LoadGame, self.Options)
        QWidget.setTabOrder(self.Options, self.NewGame)

        self.retranslateUi(Window)

        self.Tabs.setCurrentIndex(0)
        self.Options.setDefault(False)
        self.LeaveOptions.setDefault(False)


        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Game Window", None))
        self.Game_Label.setText(QCoreApplication.translate("Window", u"Py Explorer", None))
        self.NewGame.setText(QCoreApplication.translate("Window", u"New Game", None))
        self.LoadGame.setText(QCoreApplication.translate("Window", u"Load Game", None))
        self.Options.setText(QCoreApplication.translate("Window", u"Options", None))
        self.Quit.setText(QCoreApplication.translate("Window", u"Quit", None))
        self.DevBtn.setText(QCoreApplication.translate("Window", u"Test Button", None))
        self.Options_Label.setText(QCoreApplication.translate("Window", u"Options Menu", None))
        self.TextSpeed_Label.setText(QCoreApplication.translate("Window", u"Text Speed:", None))
        self.LeaveOptions.setText(QCoreApplication.translate("Window", u"Save and Exit", None))
        self.SaveAndQuit.setText(QCoreApplication.translate("Window", u"Return to Main Menu", None))
        self.InventoryBtn.setText(QCoreApplication.translate("Window", u"Inventory", None))
        self.MapMenuButton.setText(QCoreApplication.translate("Window", u"Map", None))
        self.idfk.setText(QCoreApplication.translate("Window", u"idk", None))
        self.MapLabel.setText(QCoreApplication.translate("Window",u"Error",None))
    # retranslateUi

