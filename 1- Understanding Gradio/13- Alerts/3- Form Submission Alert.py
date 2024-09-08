def submit_form(name, email):
    gr.Info("Submitting form...")
    if not name:
        gr.Warning("Name field is empty, using default 'Anonymous'.")
        name = "Anonymous"
    if "@" not in email:
        raise gr.Error("Invalid email address. Please enter a valid email.")
    gr.Info("Form submitted successfully.")
