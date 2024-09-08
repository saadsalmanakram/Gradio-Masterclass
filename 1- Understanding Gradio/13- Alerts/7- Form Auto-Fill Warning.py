def autofill_form(address):
    gr.Info("Auto-filling form...")
    if not address:
        raise gr.Error("Address field cannot be empty.")
    if len(address) < 10:
        gr.Warning("Address seems too short, please verify.")
    gr.Info("Form auto-filled successfully.")
