# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_profileWWmwdv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(268, 61)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.picture_lbl = QLabel(Form)
        self.picture_lbl.setObjectName(u"picture_lbl")
        self.picture_lbl.setMinimumSize(QSize(40, 40))
        self.picture_lbl.setMaximumSize(QSize(40, 40))
        self.picture_lbl.setStyleSheet(u"border-radius:20;\n"
"background-color: rgb(0, 0, 0);")
        self.picture_lbl.setPixmap(QPixmap(u":/images/images/user.png"))
        self.picture_lbl.setScaledContents(True)
        self.picture_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.picture_lbl)

        self.name_lbl = QLabel(Form)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setStyleSheet(u"\n"
"font: 700 22pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.name_lbl)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.picture_lbl.setText("")
        self.name_lbl.setText(QCoreApplication.translate("Form", u"Ozodek", None))
    # retranslateUi

