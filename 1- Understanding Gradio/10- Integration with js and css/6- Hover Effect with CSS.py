import gradio as gr

css = """
.button-hover:hover {background-color: orange; color: black;}
"""

with gr.Blocks(css=css) as demo:
    gr.Button("Hover Over Me", elem_classes="button-hover")
    
demo.launch()
