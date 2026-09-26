def login(username, password):
    if username == "student" and password == "1234":
        return "Welcome, student!"
    else:
        return "Authentication failed"


print(login("student", "1234"))