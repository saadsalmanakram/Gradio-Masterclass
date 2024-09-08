# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:52:57 2024

@author: saads
"""

import random
import string
import gradio as gr

def save_audio_random_name(audio):
    random_string = ''.join(random.choices(string.ascii_letters, k=10)) + '.wav'
    with open(random_string, 'wb') as f:
        f.write(audio)
    print(f"Saved audio as {random_string}")

demo = gr.Interface(
    fn=save_audio_random_name, 
    inputs=gr.Audio(source="microphone", type="file"), 
    outputs=None, 
    title="Audio Saver"
)

demo.launch()
