import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        label = gr.Label("Adjust the value:")
        slider = gr.Slider(minimum=0, maximum=100, step=1)

demo.launch()
