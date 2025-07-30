def login(username, password):
    if not any(char in "!@#$%" for char in password):
        return False
    return username == "admin" and password == "pa$$word123"
