import gradio as gr
import time

def upload_file(file, progress=gr.Progress()):
    progress(0, desc="Uploading File")
    time.sleep(1)
    progress(0.5, desc="Processing File")
    time.sleep(1)
    progress(1, desc="Upload Complete")
    return f"{file.name} uploaded successfully."

demo = gr.Interface(upload_file, gr.File(), gr.Textbox())

demo.launch()
