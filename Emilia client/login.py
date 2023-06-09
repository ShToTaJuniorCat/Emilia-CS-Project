# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Documents\test_ui\ui\login_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(449, 842)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 451, 811))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 181, 161))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 280, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 380, 101, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 450, 101, 31))
        self.label_5.setStyleSheet("* {\n"
"    color: black;\n"
"    border-radius: 20%;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.submitLogin = QtWidgets.QPushButton(self.centralwidget)
        self.submitLogin.setGeometry(QtCore.QRect(150, 610, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.submitLogin.setFont(font)
        self.submitLogin.setToolTip("")
        self.submitLogin.setStyleSheet("* {\n"
"    color: black;\n"
"    background-color: lightblue;\n"
"    border: 1px solid lightblue;\n"
"    border-radius: 20px;\n"
"}")
        self.submitLogin.setObjectName("submitLogin")
        self.errorMsgLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorMsgLabel.setGeometry(QtCore.QRect(60, 510, 321, 31))
        self.errorMsgLabel.setObjectName("errorMsgLabel")
        self.usernameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameBox.setGeometry(QtCore.QRect(160, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameBox.setFont(font)
        self.usernameBox.setObjectName("usernameBox")
        self.passwordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordBox.setGeometry(QtCore.QRect(160, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordBox.setFont(font)
        self.passwordBox.setObjectName("passwordBox")
        self.passwordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(100, 690, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.signUpButton.setFont(font)
        self.signUpButton.setStyleSheet("* { color: #0000ff }")
        self.signUpButton.setAutoDefault(False)
        self.signUpButton.setDefault(False)
        self.signUpButton.setFlat(True)
        self.signUpButton.setObjectName("signUpButton")
        self.forgotPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(130, 550, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.forgotPasswordButton.setFont(font)
        self.forgotPasswordButton.setStyleSheet("* { color: #0000ff }")
        self.forgotPasswordButton.setAutoDefault(False)
        self.forgotPasswordButton.setDefault(False)
        self.forgotPasswordButton.setFlat(True)
        self.forgotPasswordButton.setObjectName("forgotPasswordButton")
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 26))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.label.setText(_translate("LoginPage", "<html><head/><body><p><img src=\":/resources/resources/background.png\"/></p></body></html>"))
        self.label_2.setText(_translate("LoginPage", "<html><head/><body><p><img src=\":/resources/resources/icon.png\"/></p></body></html>"))
        self.label_3.setText(_translate("LoginPage", "<html><head/><body><p><span style=\" font-size:18pt;\">Login</span></p></body></html>"))
        self.label_4.setText(_translate("LoginPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("LoginPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Password</span></p></body></html>"))
        self.submitLogin.setText(_translate("LoginPage", "Submit"))
        self.errorMsgLabel.setText(_translate("LoginPage", "<html><head/><body><p><br/></p></body></html>"))
        self.signUpButton.setText(_translate("LoginPage", "Or Sign Up"))
        self.signUpButton.setProperty("click", _translate("LoginPage", "ConfPageClicked"))
        self.forgotPasswordButton.setText(_translate("LoginPage", "Forgot password?"))
        self.forgotPasswordButton.setProperty("click", _translate("LoginPage", "ConfPageClicked"))
import resource_rc
