# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:54:37 2024

@author: saads
"""

# In this example, a temperature converter automatically updates the conversion result when the user enters a temperature or changes the unit. The interface recalculates continuously without the need for a submit button, thanks to live=True.


import gradio as gr

def temperature_converter(temp, from_unit, to_unit):
    if from_unit == to_unit:
        return temp
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return temp * 9/5 + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (temp - 32) * 5/9

demo = gr.Interface(
    temperature_converter,
    [
        "number",
        gr.Dropdown(["Celsius", "Fahrenheit"], label="From Unit"),
        gr.Dropdown(["Celsius", "Fahrenheit"], label="To Unit")
    ],
    "number",
    live=True
)

demo.launch()
