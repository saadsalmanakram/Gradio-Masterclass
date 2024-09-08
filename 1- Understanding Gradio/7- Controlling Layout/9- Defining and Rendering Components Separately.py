import gradio as gr

file_uploader = gr.File(label="Upload a file")

with gr.Blocks() as demo:
    file_uploader.render()
    gr.Examples(["example.txt", "sample.pdf"], file_uploader)

demo.launch()
