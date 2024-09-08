import gradio as gr

def echo(message, history):
    return message

gr.ChatInterface(echo).launch()
