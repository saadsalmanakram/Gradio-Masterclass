# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:52:33 2024

@author: saads
"""

# This example builds a basic chat application where a global chat history is visible to all users, but each user also has their own session-based private messages.

import gradio as gr

global_chat = []

def chat(message, personal_chat):
    global global_chat
    
    global_chat.append(f"Global: {message}")
    personal_chat.append(f"You: {message}")
    
    output = {
        "Global Chat": global_chat[-5:],  # Show last 5 global messages
        "Your Personal Chat": personal_chat[-5:]  # Show last 5 personal messages
    }
    
    return output, personal_chat

demo = gr.Interface(
    fn=chat,
    inputs=[gr.Textbox(placeholder="Type your message"), gr.State(value=[])],  # Personal chat session state
    outputs=[gr.JSON(), gr.State()]
)

demo.launch()
