# Returning Multiple Outputs

import gradio as gr

def math_operations(number):
    return [number ** 2, number ** 0.5]

def math_operations_dict(number):
    return {square_output: number ** 2, sqrt_output: number ** 0.5}

with gr.Blocks() as demo:
    number_input = gr.Number(label="Enter a number")
    square_output = gr.Number(label="Square")
    sqrt_output = gr.Number(label="Square Root")
    list_button = gr.Button("Calculate (List Return)")
    dict_button = gr.Button("Calculate (Dict Return)")
    
    # Return as list
    list_button.click(fn=math_operations, inputs=number_input, outputs=[square_output, sqrt_output])
    
    # Return as dict
    dict_button.click(fn=math_operations_dict, inputs=number_input, outputs=[square_output, sqrt_output])

demo.launch()
