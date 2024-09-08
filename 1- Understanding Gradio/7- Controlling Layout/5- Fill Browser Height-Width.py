import gradio as gr

with gr.Blocks(fill_height=True) as demo:
    with gr.Row():
        video_player = gr.Video("path_to_video.mp4", scale=1)
        text_area = gr.Textbox(scale=0.5, placeholder="Enter text here...")

demo.launch()
