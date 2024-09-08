# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:51:09 2024

@author: saads
"""

# This demo displays random quotes, generated every time the user clicks a button.

import random
import gradio as gr

def generate_quote():
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "You are never too old to set another goal or to dream a new dream."
    ]
    return random.choice(quotes)

demo = gr.Interface(
    fn=generate_quote, 
    inputs=None, 
    outputs=gr.Textbox(label="Random Quote"), 
    title="Random Quote Generator"
)

demo.launch()
