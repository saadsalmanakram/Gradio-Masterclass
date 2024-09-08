import gradio as gr

with gr.Blocks() as demo:
    with gr.Row(equal_height=False):
        checkbox = gr.Checkbox(label="Check me")
        number_input = gr.Number(label="Enter number")

demo.launch()
