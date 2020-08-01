# Password-Hacker (By Jetbrains-Academy)


It is a simple project by the Jetbrains Academy(https://hyperskill.org/projects/80?track=2) under the Python Developer category, mainly focusses on leraning new concepts with a project. This is the python code for the "Time-based vulnerability" where the server communicates with JSON date type which contains "login" and "password" in it representing the login name and password respectively(it uses local machine itself as server) and has the vulnerabilities:
1. If the login name is not correct, it responds with message {"result": "Wrong login!"} in JSON type and if the login name is correct and the password is wrong, it responds with {"result": "Wrong password!"}
2. The server has a main vulnerability that: an eception occurs when the symbols you tried for the password match the beginning of the correct one. But the server does not tell you tell you that exception is seen, but simply responds with the same message {"result": "Wrong password!"} in JSON type.

We have to use the vulnerability(loophole) that catching an exception takes the computer a long time than usual.
