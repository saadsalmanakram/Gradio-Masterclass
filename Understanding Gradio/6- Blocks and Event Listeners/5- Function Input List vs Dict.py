# Calculating Area and Perimeter

import gradio as gr

def calculate_area(length, width):
    return length * width

def calculate_perimeter(inputs):
    return 2 * (inputs[length_input] + inputs[width_input])

with gr.Blocks() as demo:
    length_input = gr.Number(label="Length")
    width_input = gr.Number(label="Width")
    area_output = gr.Number(label="Area")
    perimeter_output = gr.Number(label="Perimeter")
    area_button = gr.Button("Calculate Area")
    perimeter_button = gr.Button("Calculate Perimeter")
    
    # Using list of inputs
    area_button.click(fn=calculate_area, inputs=[length_input, width_input], outputs=area_output)
    
    # Using dict of inputs
    perimeter_button.click(fn=calculate_perimeter, inputs={length_input, width_input}, outputs=perimeter_output)

demo.launch()

