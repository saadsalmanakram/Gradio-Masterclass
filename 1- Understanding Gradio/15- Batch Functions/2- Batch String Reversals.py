# This function reverses each input string in a batch and returns the reversed strings.

import gradio as gr

def reverse_strings(strings):
    return [s[::-1] for s in strings]

demo = gr.Interface(
    fn=reverse_strings, 
    inputs="textbox", 
    outputs="text",
    batch=True, 
    max_batch_size=10
)

demo.launch()
