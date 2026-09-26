def login(username, password):
    if username == "student" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"


print(login("student", "1234"))