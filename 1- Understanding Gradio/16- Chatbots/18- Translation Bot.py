from googletrans import Translator
import gradio as gr

translator = Translator()

def translate_bot(message, history):
    translation = translator.translate(message, dest='es')  # Translate to Spanish
    return f"Translation: {translation.text}"

gr.ChatInterface(translate_bot).launch()
