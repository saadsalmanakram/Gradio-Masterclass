import numpy as np
import gradio as gr
from PIL import Image, ImageEnhance

def enhance_image(image, intensity):
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(intensity)
    return enhanced_image

demo = gr.Interface(
    fn=enhance_image,
    inputs=[gr.Image(type="pil"), gr.Slider(minimum=0.1, maximum=3, step=0.1, value=1, label="Intensity")],
    outputs="image",
    title="Image Contrast Enhancer",
    description="Adjust the contrast of your image using the slider."
)

demo.launch()
