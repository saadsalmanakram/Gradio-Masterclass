import gradio as gr
import time

def translate_text(text, progress=gr.Progress()):
    progress(0, desc="Translating")
    time.sleep(2)
    progress(1, desc="Completed")
    return f"Translated: {text[::-1]}"

demo = gr.Interface(translate_text, gr.Textbox(), gr.Textbox())

demo.launch()
