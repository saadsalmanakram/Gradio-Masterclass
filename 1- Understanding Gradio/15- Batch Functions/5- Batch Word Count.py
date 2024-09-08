# This function counts the number of words in each input string in a batch and returns the word counts.

import gradio as gr

def count_words(texts):
    return [len(text.split()) for text in texts]

demo = gr.Interface(
    fn=count_words, 
    inputs="textbox", 
    outputs="number",
    batch=True, 
    max_batch_size=10
)

demo.launch()
