# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert.ui'
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

