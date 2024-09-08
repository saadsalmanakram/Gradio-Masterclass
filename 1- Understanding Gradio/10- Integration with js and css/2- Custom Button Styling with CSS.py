import gradio as gr

css = """
#custom-button {background-color: green; color: white; border-radius: 10px;}
"""

with gr.Blocks(css=css) as demo:
    gr.Button("Click Me", elem_id="custom-button")
    
demo.launch()
