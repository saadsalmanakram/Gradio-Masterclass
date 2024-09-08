import gradio as gr

css = """
.custom-cursor {cursor: url('https://example.com/cursor.png'), auto;}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(placeholder="Hover to see custom cursor", elem_classes="custom-cursor")
    
demo.launch()
