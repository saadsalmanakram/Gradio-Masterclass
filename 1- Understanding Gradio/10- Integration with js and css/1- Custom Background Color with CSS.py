import gradio as gr

css = """
.gradio-container {background-color: lightblue;}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(placeholder="Enter text here...")
    
demo.launch()
