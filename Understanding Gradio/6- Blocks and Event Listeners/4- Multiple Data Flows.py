# Temperature Converter with Multiple Data Flows

import gradio as gr

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

with gr.Blocks() as demo:
    celsius_input = gr.Number(label="Celsius")
    kelvin_input = gr.Number(label="Kelvin")
    c_to_k_button = gr.Button("Convert Celsius to Kelvin")
    k_to_c_button = gr.Button("Convert Kelvin to Celsius")
    
    c_to_k_button.click(fn=celsius_to_kelvin, inputs=celsius_input, outputs=kelvin_input)
    k_to_c_button.click(fn=kelvin_to_celsius, inputs=kelvin_input, outputs=celsius_input)

demo.launch()
