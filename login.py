def login(username, password):
    if username == "student" and password == "1234":
        return "Welcome, student!"
    else:
        return "Invalid username or password"
