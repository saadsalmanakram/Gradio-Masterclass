# This function calculates the square of each input number in a batch and returns the results.

import gradio as gr

def compute_squares(numbers):
    return [x**2 for x in numbers]

demo = gr.Interface(
    fn=compute_squares, 
    inputs="number", 
    outputs="number",
    batch=True, 
    max_batch_size=10
)

demo.launch()
