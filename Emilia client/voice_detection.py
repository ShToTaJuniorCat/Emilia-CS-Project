# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Documents\test_ui\ui\voice_detecting.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoiceDetection(object):
    def setupUi(self, VoiceDetection):
        VoiceDetection.setObjectName("VoiceDetection")
        VoiceDetection.resize(450, 761)
        self.centralwidget = QtWidgets.QWidget(VoiceDetection)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, 0, 461, 801))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 191, 161))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 270, 121, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 430, 421, 131))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 351, 91))
        self.label_5.setObjectName("label_5")
        self.pleaseWaitLabel = QtWidgets.QLabel(self.centralwidget)
        self.pleaseWaitLabel.setGeometry(QtCore.QRect(160, 610, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pleaseWaitLabel.setFont(font)
        self.pleaseWaitLabel.setObjectName("pleaseWaitLabel")
        VoiceDetection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VoiceDetection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        VoiceDetection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VoiceDetection)
        self.statusbar.setObjectName("statusbar")
        VoiceDetection.setStatusBar(self.statusbar)

        self.retranslateUi(VoiceDetection)
        QtCore.QMetaObject.connectSlotsByName(VoiceDetection)

    def retranslateUi(self, VoiceDetection):
        _translate = QtCore.QCoreApplication.translate
        VoiceDetection.setWindowTitle(_translate("VoiceDetection", "MainWindow"))
        self.label.setText(_translate("VoiceDetection", "<html><head/><body><p><img src=\":/resources/resources/background.png\"/></p></body></html>"))
        self.label_2.setText(_translate("VoiceDetection", "<html><head/><body><p><img src=\":/resources/resources/icon.png\"/></p></body></html>"))
        self.label_3.setText(_translate("VoiceDetection", "<html><head/><body><p><span style=\" font-size:14pt;\">Detecting...</span></p></body></html>"))
        self.label_4.setText(_translate("VoiceDetection", "<html><head/><body><p><img src=\":/resources/resources/voice_detection.png\"/></p></body></html>"))
        self.label_5.setText(_translate("VoiceDetection", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Detected: </span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.pleaseWaitLabel.setText(_translate("VoiceDetection", "Please wait..."))
import resource_rc