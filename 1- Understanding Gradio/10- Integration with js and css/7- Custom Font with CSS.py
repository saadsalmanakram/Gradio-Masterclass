import gradio as gr

css = """
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
.custom-font {font-family: 'Roboto', sans-serif;}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(value="This is Roboto font", elem_classes="custom-font")
    
demo.launch()
