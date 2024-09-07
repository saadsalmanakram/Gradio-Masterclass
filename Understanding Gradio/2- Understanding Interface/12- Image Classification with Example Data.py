import gradio as gr
import numpy as np

def classify_image(image):
    # Dummy classification logic
    return "Cat" if np.mean(image) > 0.5 else "Dog"

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(),
    outputs="label",
    examples=[
        ["cat.jpg"],
        ["dog.jpg"]
    ],
    title="Image Classifier",
    description="Classify an image as either a Cat or a Dog."
)

demo.launch()
