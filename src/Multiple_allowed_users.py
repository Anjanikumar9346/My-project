def login(username, password):
    allowed = {
        "admin": "password123",
        "user1": "abc123",
        "user2": "xyz789"
    }
    return allowed.get(username) == password
