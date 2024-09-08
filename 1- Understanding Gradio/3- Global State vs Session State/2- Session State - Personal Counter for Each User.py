# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:18:08 2024

@author: saads
"""

# This example demonstrates using session state to maintain a separate counter for each user. Every user can click the button and maintain their own private counter.

import gradio as gr

def increment(session_counter):
    session_counter += 1
    return f"Your personal counter: {session_counter}", session_counter

demo = gr.Interface(
    fn=increment,
    inputs=[gr.State(0)],  # Initialize session state with a default value of 0
    outputs=["text", gr.State()]
)

demo.launch()
