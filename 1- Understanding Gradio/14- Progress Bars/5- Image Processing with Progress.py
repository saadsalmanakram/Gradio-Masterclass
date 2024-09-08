import gradio as gr
import time

def process_image(image, progress=gr.Progress()):
    progress(0, desc="Processing Image")
    time.sleep(1)
    progress(0.5, desc="Enhancing Image")
    time.sleep(1)
    progress(1, desc="Finished")
    return image

demo = gr.Interface(process_image, gr.Image(), gr.Image())

demo.launch()
