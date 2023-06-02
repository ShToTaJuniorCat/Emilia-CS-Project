# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Documents\test_ui\ui\reset_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResetPassword(object):
    def setupUi(self, ResetPassword):
        ResetPassword.setObjectName("ResetPassword")
        ResetPassword.resize(451, 851)
        self.centralwidget = QtWidgets.QWidget(ResetPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 801))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 181, 151))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 270, 221, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 111, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 430, 141, 31))
        self.label_5.setObjectName("label_5")
        self.submitResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitResetButton.setGeometry(QtCore.QRect(130, 610, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submitResetButton.setFont(font)
        self.submitResetButton.setStyleSheet("* {\n"
"    color: black;\n"
"    background-color: lightblue;\n"
"    border: 1px solid lightblue;\n"
"    border-radius: 20px;\n"
"}")
        self.submitResetButton.setObjectName("submitResetButton")
        self.errorMsg = QtWidgets.QLabel(self.centralwidget)
        self.errorMsg.setGeometry(QtCore.QRect(80, 530, 301, 51))
        self.errorMsg.setObjectName("errorMsg")
        self.codeBox = QtWidgets.QLineEdit(self.centralwidget)
        self.codeBox.setGeometry(QtCore.QRect(200, 390, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.codeBox.setFont(font)
        self.codeBox.setObjectName("codeBox")
        self.newPasswordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.newPasswordBox.setGeometry(QtCore.QRect(200, 430, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newPasswordBox.setFont(font)
        self.newPasswordBox.setObjectName("newPasswordBox")
        self.newPasswordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(110, 690, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("* { color: #0000ff }")
        self.loginButton.setAutoDefault(False)
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(True)
        self.loginButton.setObjectName("loginButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 470, 141, 31))
        self.label_6.setObjectName("label_6")
        self.confirmPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmPassword.setGeometry(QtCore.QRect(200, 470, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmPassword.setFont(font)
        self.confirmPassword.setObjectName("confirmPassword")
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ResetPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResetPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 26))
        self.menubar.setObjectName("menubar")
        ResetPassword.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResetPassword)
        self.statusbar.setObjectName("statusbar")
        ResetPassword.setStatusBar(self.statusbar)

        self.retranslateUi(ResetPassword)
        QtCore.QMetaObject.connectSlotsByName(ResetPassword)

    def retranslateUi(self, ResetPassword):
        _translate = QtCore.QCoreApplication.translate
        ResetPassword.setWindowTitle(_translate("ResetPassword", "MainWindow"))
        self.label.setText(_translate("ResetPassword", "<html><head/><body><p><img src=\":/resources/resources/background.png\"/></p></body></html>"))
        self.label_2.setText(_translate("ResetPassword", "<html><head/><body><p><img src=\":/resources/resources/icon.png\"/></p></body></html>"))
        self.label_3.setText(_translate("ResetPassword", "<html><head/><body><p><span style=\" font-size:18pt;\">Reset Password</span></p></body></html>"))
        self.label_4.setText(_translate("ResetPassword", "<html><head/><body><p><span style=\" font-size:12pt;\">E-Mail code:</span></p></body></html>"))
        self.label_5.setText(_translate("ResetPassword", "<html><head/><body><p><span style=\" font-size:12pt;\">New Password:</span></p></body></html>"))
        self.submitResetButton.setText(_translate("ResetPassword", "Reset Password"))
        self.errorMsg.setText(_translate("ResetPassword", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.loginButton.setText(_translate("ResetPassword", "Back to Login"))
        self.loginButton.setProperty("click", _translate("ResetPassword", "ConfPageClicked"))
        self.label_6.setText(_translate("ResetPassword", "<html><head/><body><p><span style=\" font-size:12pt;\">Confirm pw:</span></p></body></html>"))
import resource_rc