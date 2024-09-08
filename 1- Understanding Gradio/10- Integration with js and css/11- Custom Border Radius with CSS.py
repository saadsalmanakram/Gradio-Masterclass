import gradio as gr

css = """
.custom-border {border-radius: 15px; border: 2px solid #000;}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(placeholder="Rounded corners text box", elem_classes="custom-border")
    
demo.launch()
