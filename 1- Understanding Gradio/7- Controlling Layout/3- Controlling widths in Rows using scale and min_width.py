import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        btn_small = gr.Button("Small Button", scale=1, min_width=100)
        btn_medium = gr.Button("Medium Button", scale=2, min_width=150)
        btn_large = gr.Button("Large Button", scale=3, min_width=200)

demo.launch()
