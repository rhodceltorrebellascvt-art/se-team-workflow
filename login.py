def login(username, password):
    if username == "student" and password == "1234":
        return "Authentication passed"
    else:
        return "Authentication failed"