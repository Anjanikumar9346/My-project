attempts = {}

def login(username, password):
    global attempts
    if username not in attempts:
        attempts[username] = 0

    if attempts[username] >= 3:
        return "Account locked"

    if username == "admin" and password == "password123":
        return True

    attempts[username] += 1
    return False
