# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Documents\test_ui\ui\sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpPage(object):
    def setupUi(self, SignUpPage):
        SignUpPage.setObjectName("SignUpPage")
        SignUpPage.resize(445, 842)
        self.centralwidget = QtWidgets.QWidget(SignUpPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 461, 791))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 181, 161))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 270, 111, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 410, 71, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 101, 31))
        self.label_6.setObjectName("label_6")
        self.submitSignUp = QtWidgets.QPushButton(self.centralwidget)
        self.submitSignUp.setGeometry(QtCore.QRect(160, 640, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.submitSignUp.setFont(font)
        self.submitSignUp.setToolTip("")
        self.submitSignUp.setStyleSheet("* {\n"
"    color: black;\n"
"    background-color: lightblue;\n"
"    border: 1px solid lightblue;\n"
"    border-radius: 20px;\n"
"}")
        self.submitSignUp.setObjectName("submitSignUp")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(70, 560, 311, 61))
        self.errorLabel.setObjectName("errorLabel")
        self.usernameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameBox.setGeometry(QtCore.QRect(180, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameBox.setFont(font)
        self.usernameBox.setObjectName("usernameBox")
        self.emailBox = QtWidgets.QLineEdit(self.centralwidget)
        self.emailBox.setGeometry(QtCore.QRect(180, 410, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailBox.setFont(font)
        self.emailBox.setObjectName("emailBox")
        self.passwordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordBox.setGeometry(QtCore.QRect(180, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordBox.setFont(font)
        self.passwordBox.setObjectName("passwordBox")
        self.passwordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(110, 700, 241, 61))
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 490, 121, 31))
        self.label_7.setObjectName("label_7")
        self.confirmPasswordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmPasswordBox.setGeometry(QtCore.QRect(180, 490, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmPasswordBox.setFont(font)
        self.confirmPasswordBox.setObjectName("confirmPasswordBox")
        self.confirmPasswordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 370, 21, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 450, 21, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(150, 490, 21, 21))
        self.label_11.setObjectName("label_11")
        SignUpPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignUpPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 26))
        self.menubar.setObjectName("menubar")
        SignUpPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignUpPage)
        self.statusbar.setObjectName("statusbar")
        SignUpPage.setStatusBar(self.statusbar)

        self.retranslateUi(SignUpPage)
        QtCore.QMetaObject.connectSlotsByName(SignUpPage)

    def retranslateUi(self, SignUpPage):
        _translate = QtCore.QCoreApplication.translate
        SignUpPage.setWindowTitle(_translate("SignUpPage", "MainWindow"))
        self.label.setText(_translate("SignUpPage", "<html><head/><body><p><img src=\":/resources/resources/background.png\"/></p></body></html>"))
        self.label_2.setText(_translate("SignUpPage", "<html><head/><body><p><img src=\":/resources/resources/icon.png\"/></p></body></html>"))
        self.label_3.setText(_translate("SignUpPage", "<html><head/><body><p><span style=\" font-size:18pt;\">Sign Up</span></p></body></html>"))
        self.label_4.setText(_translate("SignUpPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("SignUpPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Email</span></p></body></html>"))
        self.label_6.setText(_translate("SignUpPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Password</span></p></body></html>"))
        self.submitSignUp.setText(_translate("SignUpPage", "Submit"))
        self.errorLabel.setText(_translate("SignUpPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.loginButton.setText(_translate("SignUpPage", "Or Login"))
        self.loginButton.setProperty("click", _translate("SignUpPage", "ConfPageClicked"))
        self.label_7.setText(_translate("SignUpPage", "<html><head/><body><p><span style=\" font-size:14pt;\">Confirm pw</span></p></body></html>"))
        self.label_9.setToolTip(_translate("SignUpPage", "<html><head/><body><p>Between 3-40 characters.</p></body></html>"))
        self.label_9.setWhatsThis(_translate("SignUpPage", "<html><head/><body><p><br/></p></body></html>"))
        self.label_9.setText(_translate("SignUpPage", "<html><head/><body><p><img src=\":/resources/resources/help.png\"/></p></body></html>"))
        self.label_10.setToolTip(_translate("SignUpPage", "<html><head/><body><p>8 characters or more, at least 1: number, upper, lower.</p></body></html>"))
        self.label_10.setWhatsThis(_translate("SignUpPage", "<html><head/><body><p><br/></p></body></html>"))
        self.label_10.setText(_translate("SignUpPage", "<html><head/><body><p><img src=\":/resources/resources/help.png\"/></p></body></html>"))
        self.label_11.setToolTip(_translate("SignUpPage", "<html><head/><body><p>Retype your password.</p></body></html>"))
        self.label_11.setWhatsThis(_translate("SignUpPage", "<html><head/><body><p><br/></p></body></html>"))
        self.label_11.setText(_translate("SignUpPage", "<html><head/><body><p><img src=\":/resources/resources/help.png\"/></p></body></html>"))
import resource_rc
