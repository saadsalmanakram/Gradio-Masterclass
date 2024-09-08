# Automatic Sum Calculation

import gradio as gr

with gr.Blocks() as demo:
    number_a = gr.Number(label="Number A")
    number_b = gr.Number(label="Number B")
    sum_output = gr.Number(lambda a, b: a + b, inputs=[number_a, number_b], label="Sum")

demo.launch()
