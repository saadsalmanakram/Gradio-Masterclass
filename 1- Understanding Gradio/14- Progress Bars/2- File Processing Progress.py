import gradio as gr
import time

def process_file(file, progress=gr.Progress()):
    progress(0, desc="Uploading")
    time.sleep(1)
    progress(0.2, desc="Processing File")
    time.sleep(1)
    progress(1, desc="Finished")
    return f"{file.name} processed."

demo = gr.Interface(process_file, gr.File(), gr.Textbox())

demo.launch()
