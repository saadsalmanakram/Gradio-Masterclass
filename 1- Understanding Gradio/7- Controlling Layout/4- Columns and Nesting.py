import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=200):
            text_input = gr.Textbox(label="Enter text")
            dropdown = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="Select an option")
        with gr.Column(scale=2, min_width=300):
            image = gr.Image("path_to_image.jpg")
            submit_button = gr.Button("Submit")

demo.launch()
