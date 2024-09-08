import gradio as gr

css = """
.form-container {display: flex; flex-direction: column; gap: 10px;}
"""

with gr.Blocks(css=css) as demo:
    with gr.Row(elem_classes="form-container"):
        gr.Textbox(placeholder="First Name")
        gr.Textbox(placeholder="Last Name")
        gr.Button("Submit")
    
demo.launch()
