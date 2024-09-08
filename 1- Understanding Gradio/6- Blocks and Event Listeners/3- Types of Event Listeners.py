# Using different event listeners

import gradio as gr

def capitalize_text(text):
    return text.upper()

with gr.Blocks() as demo:
    text_input = gr.Textbox(label="Enter text")
    text_output = gr.Textbox(label="Capitalized text")
    text_input.change(fn=capitalize_text, inputs=text_input, outputs=text_output)

demo.launch()
