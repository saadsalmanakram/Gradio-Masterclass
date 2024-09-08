import gradio as gr

def audio_response(message, history):
    if message.strip():
        return gr.Audio("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav")
    else:
        return "Please provide the name of an artist."

gr.ChatInterface(
    audio_response, 
    textbox=gr.Textbox(placeholder="Which artist's music do you want to listen to?", scale=7),
    chatbot=gr.Chatbot(placeholder="Play music by any artist!"),
).launch()
