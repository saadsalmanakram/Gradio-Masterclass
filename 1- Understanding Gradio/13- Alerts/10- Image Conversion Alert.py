def convert_image(image):
    gr.Info("Converting image...")
    if image is None:
        raise gr.Error("No image uploaded for conversion.")
    if image.format != "PNG":
        gr.Warning("Non-PNG format detected, conversion might affect quality.")
    gr.Info("Image conversion successful.")
