# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:09:33 2024

@author: saads
"""

# This demo uses an input to adjust the brightness of an image and outputs the modified image.

import numpy as np
import gradio as gr

def adjust_brightness(image, brightness_level):
    return np.clip(image * brightness_level, 0, 255)

demo = gr.Interface(
    fn=adjust_brightness, 
    inputs=[gr.Image(), gr.Slider(0.1, 2, value=1, label="Brightness Level")], 
    outputs="image", 
    title="Brightness Adjuster"
)

demo.launch()
