def authenticate_user(username, password):
    gr.Info("Authenticating user...")
    if not username or not password:
        raise gr.Error("Username or password cannot be empty!")
    if username != "admin" or password != "password123":
        raise gr.Error("Invalid credentials, please try again.")
    gr.Info("Login successful.")
