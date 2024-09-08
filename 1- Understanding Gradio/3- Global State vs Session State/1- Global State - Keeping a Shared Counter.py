# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





# In this example, a global counter variable is shared between all users. Every time someone clicks the button, the counter increases by one for all users.


import gradio as gr

# Global counter shared across all users
counter = 0

def increment():
    global counter  # Access the global counter
    counter += 1
    return f"Current counter value: {counter}"

demo = gr.Interface(
    fn=increment,
    inputs=None,
    outputs="text"
)

demo.launch()
