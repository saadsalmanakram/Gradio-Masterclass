import gradio as gr
from PIL import Image, ImageFilter

def apply_filter(image, filter_type):
    if filter_type == "BLUR":
        return image.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        return image.filter(ImageFilter.CONTOUR)
    return image

interface = gr.Interface(
    fn=apply_filter,
    inputs=[
        gr.Image(type="pil"),
        gr.Dropdown(choices=["BLUR", "CONTOUR"], label="Filter Type")
    ],
    outputs=gr.Image(type="pil")
)

interface.launch(share=True)