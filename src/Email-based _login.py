def login(email, password):
    if "@" not in email:
        return False
    return email == "admin@example.com" and password == "password123"
