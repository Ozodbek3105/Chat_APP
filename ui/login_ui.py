# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pagePyaAkC.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(430, 200)
        LoginPage.setMaximumSize(QSize(430, 200))
        LoginPage.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(LoginPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_lineEdit = QLineEdit(LoginPage)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 40))
        self.name_lineEdit.setStyleSheet(u"border-radius:10;\n"
"background-color: rgb(222, 222, 222);\n"
"padding-left:5;")

        self.gridLayout.addWidget(self.name_lineEdit, 3, 0, 1, 2)

        self.label_2 = QLabel(LoginPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"padding-left:5;")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label = QLabel(LoginPage)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.line = QFrame(LoginPage)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.login_btn = QPushButton(LoginPage)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(200, 30))
        self.login_btn.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"background-color: rgb(155, 212, 255);\n"
"border:none;\n"
"border-radius:8;")
        self.login_btn.setAutoDefault(True)

        self.gridLayout.addWidget(self.login_btn, 4, 0, 1, 2)


        self.retranslateUi(LoginPage)

        self.login_btn.setDefault(True)


        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Form", None))
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginPage", u"username", None))
        self.label_2.setText(QCoreApplication.translate("LoginPage", u"Username", None))
        self.label.setText(QCoreApplication.translate("LoginPage", u"                   Log in Chat", None))
        self.login_btn.setText(QCoreApplication.translate("LoginPage", u"Log in", None))
    # retranslateUi

