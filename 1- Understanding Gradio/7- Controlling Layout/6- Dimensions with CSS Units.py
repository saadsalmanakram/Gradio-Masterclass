import gradio as gr

with gr.Blocks() as demo:
    text_input = gr.Textbox(width="40vw", placeholder="Type something...")

demo.launch()
