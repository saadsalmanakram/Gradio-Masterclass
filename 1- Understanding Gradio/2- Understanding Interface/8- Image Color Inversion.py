import numpy as np
import gradio as gr

def invert_colors(image):
    return 1 - image  # Invert the colors

demo = gr.Interface(
    fn=invert_colors,
    inputs=gr.Image(),
    outputs=gr.Image(),
    title="Image Color Inversion",
    description="Upload an image, and this app will invert its colors."
)

demo.launch()
