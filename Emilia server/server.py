import socket
import select
import json
import sqlite3
from hashlib import sha256
from re import fullmatch, compile
from random import choice
import smtplib, ssl
from email.mime.text import MIMEText
import base64
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Users (
			ID integer PRIMARY KEY AUTOINCREMENT,
			username text NOT NULL,
			email text NOT NULL,
			password text NOT NULL,
			voiceType integer NOT NULL,
			voiceSpeed integer NOT NULL,
			activationKey integer NOT NULL,
			appList text,
			resetCode text
			)""")


def get_g_service(service="gmail",ver="v1",scopes=['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send'
    ]):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("gmail_client_secret.json", scopes)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    return build(service, ver, credentials=creds)


def create_message(sender, to, subject, message_text):
  message = MIMEText(message_text, "html")
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject

  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(sender,to,subject,message_text,user_id='me'):
  msg = create_message(sender,to,subject,message_text)
  try:
    service = get_g_service()
    message = (service.users().messages().send(userId=user_id, body=msg)
               .execute())

    return message
  except ValueError as e:
    print('An error occurred: %s' % e)


def get_random_string(length):
    # choose from all lowercase letter
    characters = list("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "0123456789")
    return ''.join(choice(characters) for i in range(length))


def isEmailValid(email):
    """
    Returns True if the email is valid, False otherwise.
    :param email: Email to check
    :return: bool
    """
    email_regex = compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return fullmatch(email_regex, email)


def hash_str(string):
    return sha256(bytes(string, encoding="utf-8")).hexdigest()


def print_users():
    c.execute("SELECT * FROM Users")
    result_list = c.fetchall()
    for user in result_list:
        print(user)


def does_user_exist(username):  # כשלקוח מבקש להירשם ולהתחבר
    placeholders = """SELECT * FROM Users WHERE username = ?"""
    c.execute(placeholders, (username,))
    user = c.fetchall()

    return user != []


def username_match_password(username, password):
    placeholders = "SELECT password FROM Users WHERE username = ?"

    c.execute(placeholders, (username,))
    user = c.fetchall()

    if user != []:
        return password == user[0][0]
    else:
        raise ValueError(f"Username {username} not found!")


def reset_password(data):
    code = data["code"]
    new_password = data["new_password"]

    placeholders = "SELECT username FROM Users WHERE resetCode = ?"

    c.execute(placeholders, (code,))
    user = c.fetchall()

    if user == []:
        return False, "Invalid code!"

    placeholders = "UPDATE Users SET password = ?, resetCode = NULL WHERE resetCode = ?"

    c.execute(placeholders, (new_password, code))
    conn.commit()

    return True, "Password change successful!"


def update_config(data):
    username = data["username"]
    password = data["password"]

    try:
        if not username_match_password(username, password):
            return False, "Username doesn't match password!"
    except ValueError:
        return False, f"Username {username} not found!"

    voice_type = data["type"]
    speed = data["speed"]
    key = data["key"]
    apps = data["apps"]
    placeholders = "UPDATE Users SET voiceType = ?, voiceSpeed = ?, activationKey = ?, appList = ? WHERE username = ?"

    c.execute(placeholders, (voice_type, speed, key, apps, username))
    conn.commit()

    return True, "Config changes successful!"


def sign_up(data):  # Registeration function
    username = data["username"]
    email = data["email"]
    password = data["password"]

    if not isEmailValid(email):
        return False, "Please enter a valid email!"
    elif len(username) > 40:
        return False, "Username too long!"

    if not does_user_exist(username):
        voice_type = data["type"]
        speed = data["speed"]
        key = data["key"]
        apps = data["apps"]
        placeholders = """INSERT INTO Users (username, email, password, voiceType, voiceSpeed, activationKey, appList) VALUES (?,?,?,?,?,?,?)"""
        c.execute(placeholders, (username, email, password, voice_type, speed, key, apps))
        conn.commit()
        return True, "Registeration successful!"
    else:
        return False, "Username taken!"


def login(data):  # Login function
    username = data["username"]
    password = data["password"]

    try:
        if not username_match_password(username, password):
            return False, "Username doesn't match password!"
    except ValueError:
        return False, f"User doesn't exist!"

    return True, "Login successful!"


def send_code(data):
    email = data["email"]

    placeholders = "SELECT email FROM Users WHERE email = ?"

    c.execute(placeholders, (email,))
    sql_data = c.fetchall()

    if sql_data == []:
        return False, "Email not found"

    # Send password reset code
    code = get_random_string(6)
    msg = f"<p>Greetings,<br>" \
          f"We got a password reset code request to the user connected to this email.<br>" \
          f"Your reset code is:<br>" \
          f"<h2>{code}</h2><br>" \
          f"If you did not ask for this code, please ignore this email - your account is safe." \
          f"</p>"
    send_message("emilia.csproj@gmail.com", email, "Emilia Password Reset Code", msg, user_id='me')

    placeholders = "UPDATE Users SET resetCode = ? WHERE email = ?"

    c.execute(placeholders, (code, email))
    conn.commit()

    return True, "Code sent!"


def execute_waiting_commands(w_list):
    for command in commands_to_execute:
        (client_socket, client_data) = command
        client_cmd = client_data["cmd"]
        ok_flag = False
        resp = ''
        cmd_to_func = {
            'r': sign_up,
            'l': login,
            'c': update_config,
            'e': reset_password,
            's': send_code
        }

        ok_flag, resp = cmd_to_func[client_cmd](client_data)

        if client_socket in w_list:
            # print("Sent: " + json.dumps((ok_flag, resp)))
            client_socket.send(json.dumps((ok_flag, resp)).encode("UTF-8"))
        commands_to_execute.remove(command)


server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 9000))
server_socket.listen()
print("Server up and running")
open_client_sockets = []
commands_to_execute = []


while True:
    rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])

    for current_socket in rlist:
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
        else:
            length = current_socket.recv(3).decode("UTF-8")

            if length == "":
                open_client_sockets.remove(current_socket)
            else:
                msg = current_socket.recv(int(length)).decode("UTF-8")
                data = json.loads(msg)
                commands_to_execute.append((current_socket, data))

    execute_waiting_commands(wlist)
