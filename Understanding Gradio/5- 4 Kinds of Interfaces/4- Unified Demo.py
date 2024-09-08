# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:55:30 2024

@author: saads
"""


# This demo takes a user’s text input, reverses it, and returns the reversed text as output in the same textbox.

import gradio as gr

def reverse_text(text):
    return text[::-1]

textbox = gr.Textbox(label="Type something")

demo = gr.Interface(
    fn=reverse_text, 
    inputs=textbox, 
    outputs=textbox, 
    title="Text Reverser"
)

demo.launch()
