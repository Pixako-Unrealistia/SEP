# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.inc_button = QPushButton(Form)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(250, 70, 75, 24))
        self.dec_button = QPushButton(Form)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(250, 180, 75, 24))
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(60, 80, 131, 121))
        font = QFont()
        font.setPointSize(22)
        self.num_label.setFont(font)
        self.reset_button = QPushButton(Form)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(250, 250, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

