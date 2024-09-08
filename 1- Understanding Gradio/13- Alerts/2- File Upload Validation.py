def upload_file(file):
    gr.Info("Starting file upload...")
    if file is None:
        raise gr.Error("No file selected. Please upload a valid file.")
    if not file.name.endswith((".jpg", ".png", ".jpeg")):
        raise gr.Warning("File format not supported. Please upload a valid image.")
    gr.Info("File uploaded successfully.")
