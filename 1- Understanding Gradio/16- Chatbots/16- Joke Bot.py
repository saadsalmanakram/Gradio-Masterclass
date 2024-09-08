import gradio as gr

def joke_bot(message, history):
    jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!",
             "What do you call fake spaghetti? An impasta!",
             "Why don't scientists trust atoms? Because they make up everything!"]
    return random.choice(jokes)

gr.ChatInterface(joke_bot).launch()
