# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_windowmZHilr.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MessagePage(object):
    def setupUi(self, MessagePage):
        if not MessagePage.objectName():
            MessagePage.setObjectName(u"MessagePage")
        MessagePage.resize(400, 60)
        MessagePage.setMinimumSize(QSize(0, 60))
        MessagePage.setMaximumSize(QSize(16777215, 444444))
        MessagePage.setStyleSheet(u"background-color: rgb(202, 240, 190);\n"
"background-radius:10;")
        self.gridLayout = QGridLayout(MessagePage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_label = QLabel(MessagePage)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 20))
        self.name_label.setStyleSheet(u"font: 900 11pt \"Segoe UI Black\";\n"
"padding-left:6;")

        self.verticalLayout.addWidget(self.name_label)

        self.message_label = QLabel(MessagePage)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMinimumSize(QSize(0, 31))
        self.message_label.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"padding-left:7;\n"
"")

        self.verticalLayout.addWidget(self.message_label)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MessagePage)

        QMetaObject.connectSlotsByName(MessagePage)
    # setupUi

    def retranslateUi(self, MessagePage):
        MessagePage.setWindowTitle(QCoreApplication.translate("MessagePage", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("MessagePage", u"Name", None))
        self.message_label.setText(QCoreApplication.translate("MessagePage", u"Xabar", None))
    # retranslateUi

