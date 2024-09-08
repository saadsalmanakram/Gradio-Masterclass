# This function calculates the length of each input text in a batch and returns the lengths.

import gradio as gr

def get_text_lengths(texts):
    return [len(text) for text in texts]

demo = gr.Interface(
    fn=get_text_lengths, 
    inputs="textbox", 
    outputs="text",
    batch=True, 
    max_batch_size=10
)

demo.launch()
