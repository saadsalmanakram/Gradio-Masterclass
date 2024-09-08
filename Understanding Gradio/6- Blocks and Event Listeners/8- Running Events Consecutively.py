# Data Processing Pipeline

import gradio as gr
import time

def load_data(file):
    time.sleep(1)  # Simulate loading time
    return "Data loaded from " + file.name

def process_data(data):
    time.sleep(1)  # Simulate processing time
    return data + " and processed"

with gr.Blocks() as demo:
    file_input = gr.File(label="Upload File")
    status_output = gr.Textbox(label="Status")
    start_button = gr.Button("Start Processing")
    
    start_button.click(fn=load_data, inputs=file_input, outputs=status_output).then(
        fn=process_data, inputs=status_output, outputs=status_output
    )

demo.launch()
