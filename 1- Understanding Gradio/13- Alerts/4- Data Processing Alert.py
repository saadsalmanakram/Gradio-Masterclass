def process_data(data):
    gr.Info("Processing data...")
    if data is None:
        raise gr.Error("No data found to process.")
    if len(data) < 10:
        gr.Warning("Data size is very small. Consider adding more samples.")
    gr.Info("Data processing completed.")
