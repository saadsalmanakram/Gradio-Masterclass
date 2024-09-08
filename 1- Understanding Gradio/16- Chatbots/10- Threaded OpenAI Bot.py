import openai
import gradio as gr
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
threads = {}

def predict(message, history, request: gr.Request):
    if request.session_hash in threads:
        thread = threads[request.session_hash]
    else:
        threads[request.session_hash] = client.beta.threads.create()
        
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    
    ...

gr.ChatInterface(predict).launch()
