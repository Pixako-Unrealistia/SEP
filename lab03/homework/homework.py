# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homework.ui'
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
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 388)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.setTime = QPushButton(Form)
        self.setTime.setObjectName(u"setTime")
        self.setTime.setGeometry(QRect(230, 120, 75, 24))
        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(70, 150, 141, 31))
        self.resetTime = QPushButton(Form)
        self.resetTime.setObjectName(u"resetTime")
        self.resetTime.setGeometry(QRect(230, 150, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 321, 41))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.oneMin = QPushButton(Form)
        self.oneMin.setObjectName(u"oneMin")
        self.oneMin.setGeometry(QRect(20, 240, 75, 24))
        self.fiveMin = QPushButton(Form)
        self.fiveMin.setObjectName(u"fiveMin")
        self.fiveMin.setGeometry(QRect(120, 240, 75, 24))
        self.tenMin = QPushButton(Form)
        self.tenMin.setObjectName(u"tenMin")
        self.tenMin.setGeometry(QRect(220, 240, 75, 24))
        self.snooze = QPushButton(Form)
        self.snooze.setObjectName(u"snooze")
        self.snooze.setGeometry(QRect(230, 190, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.setTime.setText(QCoreApplication.translate("Form", u"Set Time", None))
        self.resetTime.setText(QCoreApplication.translate("Form", u"Reset Timer", None))
        self.label.setText(QCoreApplication.translate("Form", u"Set timer", None))
        self.oneMin.setText(QCoreApplication.translate("Form", u"1 minutes", None))
        self.fiveMin.setText(QCoreApplication.translate("Form", u"5 minutes", None))
        self.tenMin.setText(QCoreApplication.translate("Form", u"10 minutes", None))
        self.snooze.setText(QCoreApplication.translate("Form", u"Snooze", None))
    # retranslateUi

class Ui_alert(object):
    def setupUi(self, alert):
        if not alert.objectName():
            alert.setObjectName(u"alert")
        alert.resize(231, 77)
        self.label = QLabel(alert)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 131, 16))
        self.okay = QPushButton(alert)
        self.okay.setObjectName(u"okay")
        self.okay.setGeometry(QRect(20, 40, 75, 24))
        self.pushButton_2 = QPushButton(alert)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 40, 75, 24))

        self.retranslateUi(alert)

        QMetaObject.connectSlotsByName(alert)
    # setupUi

    def retranslateUi(self, alert):
        alert.setWindowTitle(QCoreApplication.translate("alert", u"Form", None))
        self.label.setText(QCoreApplication.translate("alert", u"Time's up!", None))
        self.okay.setText(QCoreApplication.translate("alert", u"Snooze", None))
        self.pushButton_2.setText(QCoreApplication.translate("alert", u"Okay", None))
    # retranslateUi
