import gradio as gr

def respond_to_query(query):
    return f"You asked: {query}"

chatbot = gr.ChatInterface(fn=respond_to_query)
chatbot.launch()

#Obv this model wont respond as there is no model given to the interface