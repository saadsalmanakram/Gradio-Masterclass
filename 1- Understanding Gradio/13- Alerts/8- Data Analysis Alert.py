def analyze_data(dataset):
    gr.Info("Starting data analysis...")
    if dataset is None:
        raise gr.Error("Dataset is missing.")
    if len(dataset) < 100:
        gr.Warning("Small dataset detected, results may not be reliable.")
    gr.Info("Data analysis completed.")
