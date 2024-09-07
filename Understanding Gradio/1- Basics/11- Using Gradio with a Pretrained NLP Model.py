import gradio as gr
from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    return generator(prompt, max_length=50)[0]['generated_text']

interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(label="Enter Prompt"),
    outputs=gr.Textbox(label="Generated Text")
)

interface.launch(share=True)
