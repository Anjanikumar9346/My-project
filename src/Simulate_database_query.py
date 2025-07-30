def login(username, password):
    mock_db = [("admin", "password123"), ("user", "pass456")]
    return (username, password) in mock_db
