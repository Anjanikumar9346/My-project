def login(username, password):
    if not username.startswith("user"):
        return False
    return password == "securepass"
