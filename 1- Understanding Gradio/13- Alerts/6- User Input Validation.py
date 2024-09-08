def validate_input(age, country):
    gr.Info("Validating user input...")
    if not isinstance(age, int):
        raise gr.Error("Age must be an integer.")
    if country.lower() not in ["usa", "canada", "uk"]:
        gr.Warning(f"{country} is not in the list of supported countries.")
    gr.Info("Input validation complete.")
