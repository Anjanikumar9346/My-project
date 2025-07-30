def login(username, password):
    return username.strip() == "admin" and password.strip() == "password123"
