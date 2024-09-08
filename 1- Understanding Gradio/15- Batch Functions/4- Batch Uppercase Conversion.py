# This function converts each input string to uppercase in a batch and returns the results.

import gradio as gr

def to_uppercase(texts):
    return [text.upper() for text in texts]

demo = gr.Interface(
    fn=to_uppercase, 
    inputs="textbox", 
    outputs="text",
    batch=True, 
    max_batch_size=10
)

demo.launch()
