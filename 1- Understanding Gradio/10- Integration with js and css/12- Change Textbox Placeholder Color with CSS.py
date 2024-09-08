import gradio as gr

css = """
.custom-placeholder::-webkit-input-placeholder {color: red;}
.custom-placeholder::-moz-placeholder {color: red;}
.custom-placeholder:-ms-input-placeholder {color: red;}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(placeholder="Red placeholder text", elem_classes="custom-placeholder")
    
demo.launch()
