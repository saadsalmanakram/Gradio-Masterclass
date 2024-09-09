import gradio as gr

def personalized_greeting(message, history):
    return f"Hello {message}! How can I assist you today?"

gr.ChatInterface(personalized_greeting).launch()
