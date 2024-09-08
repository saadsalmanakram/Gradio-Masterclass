# Doubling a Number with Interactivity Control

import gradio as gr

def double(number):
    return number * 2

with gr.Blocks() as demo:
    number_input = gr.Number(label="Input Number")
    result_output = gr.Number(label="Doubled Number", interactive=True)
    double_button = gr.Button("Double It")
    double_button.click(fn=double, inputs=number_input, outputs=result_output)

demo.launch()
