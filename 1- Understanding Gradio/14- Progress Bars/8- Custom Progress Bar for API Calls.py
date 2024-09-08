import gradio as gr
import time

def call_api(progress=gr.Progress()):
    progress(0, desc="Connecting to API")
    time.sleep(2)
    progress(0.7, desc="Fetching Data")
    time.sleep(1)
    progress(1, desc="API Call Complete")
    return "API Call Successful!"

demo = gr.Interface(call_api, inputs=None, outputs="text")

demo.launch()
