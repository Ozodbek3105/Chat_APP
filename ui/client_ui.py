# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientSCnNAj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)
import res_rc
import res_rc

class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(690, 653)
        Chat.setStyleSheet(u"#listWidget{\n"
"            background-image: url(:/images/images/background.jpg);\n"
"            background-position: center;\n"
"            background-repeat: no-repeat;\n"
"			 background-size: cover;\n"
"            border: none; /* Optional: Removes the border */\n"
"        }")
        self.gridLayout = QGridLayout(Chat)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.btn_send = QPushButton(Chat)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(13)
        self.btn_send.setFont(font)
        self.btn_send.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/images/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send.setIcon(icon)
        self.btn_send.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.btn_send, 2, 4, 1, 1)

        self.listWidget = QListWidget(Chat)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background-color: rgb(140, 215, 255);")
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setSpacing(10)

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 5)

        self.lbl_internet = QLabel(Chat)
        self.lbl_internet.setObjectName(u"lbl_internet")
        self.lbl_internet.setMaximumSize(QSize(20, 20))
        self.lbl_internet.setPixmap(QPixmap(u":/images/images/wifi_off.png"))
        self.lbl_internet.setScaledContents(True)
        self.lbl_internet.setMargin(0)
        self.lbl_internet.setIndent(-1)

        self.gridLayout.addWidget(self.lbl_internet, 2, 1, 1, 1)

        self.emoji_btn = QPushButton(Chat)
        self.emoji_btn.setObjectName(u"emoji_btn")
        self.emoji_btn.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/emoji.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/images/happiness.png", QSize(), QIcon.Normal, QIcon.On)
        self.emoji_btn.setIcon(icon1)
        self.emoji_btn.setIconSize(QSize(25, 25))
        self.emoji_btn.setCheckable(True)

        self.gridLayout.addWidget(self.emoji_btn, 2, 3, 1, 1)

        self.edit_text = QLineEdit(Chat)
        self.edit_text.setObjectName(u"edit_text")
        self.edit_text.setFont(font)

        self.gridLayout.addWidget(self.edit_text, 2, 2, 1, 1)

        self.widget = QWidget(Chat)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(88, 88, 88);\n"
"}\n"
"#listWidget_2{\n"
"	\n"
"	background-color: rgb(159, 159, 159);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.users_listWidget = QListWidget(self.widget)
        self.users_listWidget.setObjectName(u"users_listWidget")
        self.users_listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.users_listWidget, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))
        self.label_2.setPixmap(QPixmap(u":/images/images/chat (1).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 3, 1)

        self.label_4 = QLabel(Chat)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setStyleSheet(u"border-radius:20;\n"
"background-color: rgb(0, 0, 0);")
        self.label_4.setPixmap(QPixmap(u":/images/images/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.top_name_lbl = QLabel(Chat)
        self.top_name_lbl.setObjectName(u"top_name_lbl")
        self.top_name_lbl.setMinimumSize(QSize(40, 40))
        self.top_name_lbl.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"background-color: rgb(138, 218, 255);")
        self.top_name_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.top_name_lbl, 0, 1, 1, 3)


        self.retranslateUi(Chat)
        self.edit_text.returnPressed.connect(self.btn_send.click)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"Form", None))
        self.btn_send.setText("")
        self.lbl_internet.setText("")
        self.emoji_btn.setText("")
        self.edit_text.setPlaceholderText(QCoreApplication.translate("Chat", u"write message", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Chat", u"Chat ", None))
        self.label_4.setText("")
        self.top_name_lbl.setText(QCoreApplication.translate("Chat", u"Name", None))
    # retranslateUi

