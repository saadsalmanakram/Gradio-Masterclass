import gradio as gr
from transformers import pipeline

# Load translation pipelines
french_translator = pipeline("translation", model="t5-base", tokenizer="t5-base")
spanish_translator = pipeline("translation", model="t5-base", tokenizer="t5-base")

def translate_to_french(text):
    return french_translator(text, target_lang="fr")[0]["translation_text"]

def translate_to_spanish(text):
    return spanish_translator(text, target_lang="es")[0]["translation_text"]

# Create a Gradio Blocks app with multiple functions
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input Text")
            french_btn = gr.Button("Translate to French")
            spanish_btn = gr.Button("Translate to Spanish")
        with gr.Column():
            french_output = gr.Textbox(label="French Translation")
            spanish_output = gr.Textbox(label="Spanish Translation")

    french_btn.click(translate_to_french, inputs=input_text, outputs=french_output, api_name="translate-to-french")
    spanish_btn.click(translate_to_spanish, inputs=input_text, outputs=spanish_output, api_name="translate-to-spanish")

demo.launch()
