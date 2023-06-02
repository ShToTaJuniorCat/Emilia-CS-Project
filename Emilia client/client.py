import sys

import constants
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_gui import Ui_LandingPage
from configurations import Ui_ConfigPage
from login import Ui_LoginPage
from reset_password import Ui_ResetPassword
from sign_up import Ui_SignUpPage
from forgot_password import Ui_ForgotPassword
from output import Ui_Output
from voice_detection import Ui_VoiceDetection
from main import start_user_input
from speech_recognition import Recording
from pynput.keyboard import Listener, HotKey, Key
from threading import Thread
from pyttsx3 import init
from constants import configurations
from json import loads, dumps
from socket import socket
from hashlib import sha256


class CurrentWindow:
    def __init__(self, window):
        self.window = window


class MainWindow(QMainWindow, Ui_LandingPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.configPageButton.clicked.connect(main_config_button_clicked)
        self.loginButton.clicked.connect(login_button_clicked)
        self.signUpButton.clicked.connect(sign_up_button_clicked)
        self.logOutButton.clicked.connect(log_out_button_clicked)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def toggle_connect_buttons(self, show):
        if show:
            self.loginButton.show()
            self.signUpButton.show()
            self.logOutButton.hide()
        else:
            self.loginButton.hide()
            self.signUpButton.hide()
            self.logOutButton.show()


class ConfigWindow(QMainWindow, Ui_ConfigPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.mainMenuButton.clicked.connect(main_menu_button_clicked)
        self.applySettings.clicked.connect(self.update_settings)
        self.apply_current_settings()


    def update_settings(self):
        voice = self.outputVoiceList.selectedItems()
        if len(voice) != 0:
            voice = configurations.VOICE_DICT.setdefault(voice[0].text(), configurations.VOICE_DEFAULT)
        else:
            voice = configurations.VOICE_DICT = configurations.VOICE_DEFAULT

        speed = self.SpeechSpeedList.selectedItems()
        if len(speed) != 0:
            speed = configurations.SPEED_DICT.setdefault(speed[0].text(), configurations.SPEED_DEFAULT)
        else:
            speed = configurations.SPEED_DICT = configurations.SPEED_DEFAULT

        key = self.ActivationKeyList.selectedItems()
        if len(key) != 0:
            key = configurations.KEY_DICT.setdefault(key[0].text(), configurations.KEY_DEFAULT)
        else:
            key = configurations.KEY_DICT = configurations.KEY_DEFAULT

        apps = self.AppList.toPlainText()

        settings = {
            'voice': voice,
            'speed': speed,
            'key': key,
            'apps': apps
        }

        configurations.SETTINGS = settings
        update_voice()
        key_changed()

        try:
            with open(configurations.JSON_FILENAME, "w") as file:
                file.write(dumps(settings))
        except Exception as e:
            print(e)


    def apply_current_settings(self):
        current = get_config()

        self.outputVoiceList.setCurrentItem(self.outputVoiceList.item(current['voice']))
        self.SpeechSpeedList.setCurrentItem(self.SpeechSpeedList.item(current['speed']))
        self.ActivationKeyList.setCurrentItem(self.ActivationKeyList.item(current['key']))
        self.AppList.setText(current['apps'])


    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()


class VoiceDetectionWindow(QMainWindow, Ui_VoiceDetection):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)

    def toggle_visibility(self):
        visible = self.isVisible()

        if visible:
            self.hide()
        else:
            self.show()

    def pleaseWait(self, show):
        if show:
            self.pleaseWaitLabel.show()
        else:
            self.pleaseWaitLabel.hide()


class LoginWindow(QMainWindow, Ui_LoginPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.submitLogin.clicked.connect(self.submit_button_clicked)
        self.signUpButton.clicked.connect(sign_up_button_clicked)
        self.forgotPasswordButton.clicked.connect(forgot_password_button_clicked)

    def toggle_visibility(self):
        visible = self.isVisible()

        if visible:
            self.hide()
        else:
            self.show()

    def submit_button_clicked(self):
        self.errorMsgLabel.setText(
            "<html><head/><body><p style=\"text-align: center;\"><span style=\" font-size:12pt; color:#00ff00;\">"
            "Thinking..."
            "</span></p></body></html>")

        username = self.usernameBox.text()
        password = hash_str(self.passwordBox.text())

        cmd_dict = {
            "username": username,
            "password": password,
            "cmd": "l"
        }

        string_dict = dumps(cmd_dict)
        client_socket.send((str(len(string_dict)).zfill(3) + string_dict).encode("UTF-8"))

        encoded_server_response = client_socket.recv(1024)
        decoded_server_response = encoded_server_response.decode("UTF-8")
        server_response = loads(decoded_server_response)
        EnvVariables.connected = server_response[0]

        self.errorMsgLabel.setText(
            f"<html><head/><body><p style=\"text-align: center;\"><span style=\" font-size:12pt; color:#ff0000;\">"
                                   f"{server_response[1]}"
                                   f"</span></p></body></html>")

        if EnvVariables.connected:
            EnvVariables.username = username
            EnvVariables.main_win.toggle_connect_buttons(False)
            EnvVariables.current_screen.toggle_visibility()
            EnvVariables.main_win.toggle_visibility()
            EnvVariables.current_screen = EnvVariables.main_win



class SignUpWindow(QMainWindow, Ui_SignUpPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.submitSignUp.clicked.connect(self.submit_button_clicked)
        self.loginButton.clicked.connect(login_button_clicked)

    def toggle_visibility(self):
        visible = self.isVisible()

        if visible:
            self.hide()
        else:
            self.show()

    def submit_button_clicked(self):
        username = self.usernameBox.text()
        email = self.emailBox.text()
        password = self.passwordBox.text()
        confirm_password = self.confirmPasswordBox.text()

        if len(username) > 40:
            errorMsg = "Username too long!"
        elif len(username) < 3:
            errorMsg = "Username too short!"
        elif len(password) < 8:
            errorMsg = "Password too short!"
        elif not is_strong(password):
            errorMsg = "Password must contain at least 1:<br>number, upper, lower."
        elif password != confirm_password:
            errorMsg = "Passwords do not match!"
        else:
            cmd_dict = {
                "username": username,
                "email": email,
                "password": hash_str(password),
                "type": configurations.VOICE_DEFAULT,
                "speed": configurations.SPEED_DEFAULT,
                "key": configurations.KEY_DEFAULT,
                "apps": configurations.APPS_DEFAULT,
                "cmd": "r"
            }

            string_dict = dumps(cmd_dict)
            client_socket.send((str(len(string_dict)).zfill(3) + string_dict).encode("UTF-8"))

            encoded_server_response = client_socket.recv(1024)
            decoded_server_response = encoded_server_response.decode("UTF-8")
            server_response = loads(decoded_server_response)
            EnvVariables.connected = server_response[0]
            errorMsg = server_response[1]

        self.errorLabel.setText(
            f"<html><head/><body><p style=\"text-align: center;\"><span style=\" font-size:12pt; color: {'#00ff00' if EnvVariables.connected else '#ff0000'};\">"
            f"{errorMsg}"
            f"</span></p></body></html>")

        if EnvVariables.connected:
            EnvVariables.username = username
            EnvVariables.main_win.toggle_connect_buttons(False)
            EnvVariables.current_screen.toggle_visibility()
            EnvVariables.main_win.toggle_visibility()
            EnvVariables.current_screen = EnvVariables.main_win


class ForgotPasswordWindow(QMainWindow, Ui_ForgotPassword):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.loginPageButton.clicked.connect(login_button_clicked)
        self.sendCodeButton.clicked.connect(self.send_code_button_clicked)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def send_code_button_clicked(self):
        email = self.emailBox.text()

        cmd_dict = {
            "email": email,
            "cmd": "s"
        }

        string_dict = dumps(cmd_dict)
        client_socket.send((str(len(string_dict)).zfill(3) + string_dict).encode("UTF-8"))

        encoded_server_response = client_socket.recv(1024)
        decoded_server_response = encoded_server_response.decode("UTF-8")
        server_response = loads(decoded_server_response)

        errorMsg = server_response[1]

        self.errorMsgBox.setText(
            f"<html><head/><body><p style=\"text-align: center;\"><span style=\" font-size:12pt; color: {'#00ff00' if server_response[0] else '#ff0000'};\">"
            f"{errorMsg}"
            f"</span></p></body></html>")

        if server_response[0]:
            EnvVariables.reset_password_win.toggle_visibility()
            EnvVariables.current_screen.toggle_visibility()
            EnvVariables.current_screen = EnvVariables.reset_password_win


class ResetPasswordWindow(QMainWindow, Ui_ResetPassword):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(453,790)
        self.submitResetButton.clicked.connect(self.reset_password_button_clicked)
        self.loginButton.clicked.connect(login_button_clicked)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def reset_password_button_clicked(self):
        code = self.codeBox.text()
        new_password = self.newPasswordBox.text()
        confirm_password = self.confirmPassword.text()
        passed = False

        if len(new_password) < 8:
            errorMsg = "Password too short!"
        elif not is_strong(new_password):
            errorMsg = "Password must contain at least 1:<br>number, upper, lower."
        elif new_password != confirm_password:
            errorMsg = "Passwords do not match!"
        else:
            cmd_dict = {
                "code": code,
                "new_password": hash_str(new_password),
                "cmd": "e"
            }

            string_dict = dumps(cmd_dict)
            client_socket.send((str(len(string_dict)).zfill(3) + string_dict).encode("UTF-8"))

            encoded_server_response = client_socket.recv(1024)
            decoded_server_response = encoded_server_response.decode("UTF-8")
            server_response = loads(decoded_server_response)
            passed = server_response[0]

            errorMsg = server_response[1]

        self.errorMsg.setText(
            f"<html><head/><body><p style=\"text-align: center;\"><span style=\" font-size:12pt; color: {'green' if passed else '#ff0000'};\">"
            f"{errorMsg}"
            f"</span></p></body></html>")

            # if server_response[0]:
            #     EnvVariables.reset_password_win.toggle_visibility()
            #     EnvVariables.current_screen.toggle_visibility()
            #     EnvVariables.current_screen = EnvVariables.reset_password_win


def hash_str(string):
    return sha256(bytes(string, encoding="utf-8")).hexdigest()


def get_config():
    with open(configurations.JSON_FILENAME, "r") as conf:
        return loads(conf.read(), strict=False)


def update_voice():
    EnvVariables.engine.setProperty('rate', configurations.CALC_SPEED(configurations.SETTINGS["speed"]))

    """
    This is actually really funny.
    The voice in index 0 is male, and in index 1 is female,
    which is the opposite of what I thought.
    So, instead of changing the whole logic of things here,
    I perform some arithmatics to change 1 into 0 and vice versa:
    bool(not bool(voice))
    """
    EnvVariables.engine.setProperty('voice', EnvVariables.engine.getProperty('voices')[bool(not bool(
        configurations.SETTINGS["voice"] - 1))].id)


def forgot_password_button_clicked():
    EnvVariables.current_screen.toggle_visibility()
    EnvVariables.forgot_pass_win.toggle_visibility()
    EnvVariables.current_screen = EnvVariables.forgot_pass_win


def log_out_button_clicked():
    EnvVariables.main_win.toggle_connect_buttons(True)
    EnvVariables.connected = False
    EnvVariables.username = ""


def login_button_clicked():
    EnvVariables.current_screen.toggle_visibility()
    EnvVariables.login_win.toggle_visibility()
    EnvVariables.current_screen = EnvVariables.login_win


def sign_up_button_clicked():
    EnvVariables.current_screen.toggle_visibility()
    EnvVariables.sign_up_win.toggle_visibility()
    EnvVariables.current_screen = EnvVariables.sign_up_win


def main_config_button_clicked():
    EnvVariables.current_screen.toggle_visibility()
    EnvVariables.conf_win.toggle_visibility()
    EnvVariables.current_screen = EnvVariables.conf_win


def main_menu_button_clicked():
    EnvVariables.current_screen.toggle_visibility()
    EnvVariables.main_win.toggle_visibility()
    EnvVariables.current_screen = EnvVariables.main_win


def is_strong(password):
    return all([not password.islower(), not password.isupper(), not password.isalpha()])


def key_triggered():
    try:
        EnvVariables.current_screen.toggle_visibility()
        EnvVariables.voice_win.pleaseWait(True)
        EnvVariables.voice_win.toggle_visibility()
        EnvVariables.current_window = EnvVariables.voice_win
        emilia_response = start_user_input(recorder)
        EnvVariables.voice_win.pleaseWait(False)
        print(emilia_response)

        EnvVariables.engine.say(emilia_response)
        EnvVariables.engine.runAndWait()

    except Exception as e:
        print(f"EXCEPTION: {e}")

    try:
        EnvVariables.voice_win.toggle_visibility()
        EnvVariables.main_win.toggle_visibility()
        EnvVariables.current_window = EnvVariables.main_win
    except Exception as e:
        print(e)


def key_changed():
    try:
        global key_trigger
        key_trigger.stop()
        key_listener = Thread(target=bind_key)
        key_listener.start()
    except Exception as e:
        print(e)


def bind_key():
    def for_canonical(f):
        return lambda k: f(key_trigger.canonical(k))

    hotkey = HotKey(
        HotKey.parse(configurations.KEY_NUM_TO_CODE[get_config()["key"]]), key_triggered)

    global key_trigger
    with Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as key_trigger:
        key_trigger.join()


class EnvVariables:
    # TTS
    engine = init()

    # GUI
    current_screen = None
    app_main = QApplication(sys.argv)
    main_win = MainWindow()
    conf_win = ConfigWindow()
    login_win = LoginWindow()
    sign_up_win = SignUpWindow()
    voice_win = VoiceDetectionWindow()
    forgot_pass_win = ForgotPasswordWindow()
    reset_password_win = ResetPasswordWindow()

    # Registration & Login
    connected = False
    username = ""


if __name__ == "__main__":
    """
    Possible commands:
        "get time",
        "previous song",
        "next song",
        "pause music",
        "resume music",
        "shuffle on",
        "shuffle off",
        "open {app}",
        "play {song}",
        "queue {song},
        
    """

    # # Connect to server
    client_socket = socket()
    client_socket.connect(("127.0.0.1", 9000))

    EnvVariables.voice_win.show()
    EnvVariables.voice_win.hide()

    try:
        EnvVariables.main_win.toggle_visibility()
        EnvVariables.current_screen = EnvVariables.main_win

        recorder = Recording()

        key_listener = Thread(target=bind_key)
        key_listener.start()

        sys.exit(EnvVariables.app_main.exec())
    except Exception as e:
        print(e)
