import gradio as gr

def image_response(message, history):
    if "cat" in message.lower():
        return gr.Image("https://example.com/cat.jpg")
    else:
        return "I can only talk about cats."

gr.ChatInterface(
    image_response, 
    textbox=gr.Textbox(placeholder="Ask me about cats!", scale=7),
    chatbot=gr.Chatbot(placeholder="I can talk about cats."),
).launch()
