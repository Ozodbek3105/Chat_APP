# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_profileqZHWLT.ui'
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
    QSizePolicy, QWidget)
import res_rc
import res_rc

class Ui_User(object):
    def setupUi(self, User):
        if not User.objectName():
            User.setObjectName(u"User")
        User.resize(268, 61)
        self.gridLayout = QGridLayout(User)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.picture_lbl = QLabel(User)
        self.picture_lbl.setObjectName(u"picture_lbl")
        self.picture_lbl.setMinimumSize(QSize(40, 40))
        self.picture_lbl.setMaximumSize(QSize(40, 40))
        self.picture_lbl.setStyleSheet(u"border-radius:20;\n"
"background-color: rgb(0, 0, 0);")
        self.picture_lbl.setPixmap(QPixmap(u":/images/images/user.png"))
        self.picture_lbl.setScaledContents(True)
        self.picture_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.picture_lbl)

        self.name_lbl = QLabel(User)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 22pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.name_lbl)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(User)

        QMetaObject.connectSlotsByName(User)
    # setupUi

    def retranslateUi(self, User):
        User.setWindowTitle(QCoreApplication.translate("User", u"Form", None))
        self.picture_lbl.setText("")
        self.name_lbl.setText(QCoreApplication.translate("User", u"Ozodek", None))
    # retranslateUi

