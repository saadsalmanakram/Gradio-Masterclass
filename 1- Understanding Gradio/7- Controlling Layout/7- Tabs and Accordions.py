import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("Choose a tab to input data or use the accordion for more options.")
    
    with gr.Tab("Text Input 1"):
        text_input1 = gr.Textbox(placeholder="Input in Tab 1")
    
    with gr.Tab("Text Input 2"):
        text_input2 = gr.Textbox(placeholder="Input in Tab 2")
    
    with gr.Accordion("Additional Options", open=False):
        additional_option = gr.Checkbox(label="Option")

demo.launch()
