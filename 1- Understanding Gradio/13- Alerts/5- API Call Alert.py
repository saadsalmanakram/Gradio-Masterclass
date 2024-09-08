def call_api(api_key):
    gr.Info("Initiating API call...")
    if not api_key:
        raise gr.Error("API key is missing!")
    if len(api_key) < 10:
        gr.Warning("API key seems too short, double-check it.")
    gr.Info("API call in progress.")
    # Simulate API call
    success = False
    if not success:
        raise gr.Error("API call failed, please try again later.")
