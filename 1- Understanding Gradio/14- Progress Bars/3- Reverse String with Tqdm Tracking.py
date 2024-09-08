import gradio as gr
import time

def reverse_string(word, progress=gr.Progress(track_tqdm=True)):
    new_string = ""
    for letter in word:
        time.sleep(0.1)
        new_string = letter + new_string
    return new_string

demo = gr.Interface(reverse_string, gr.Textbox(), gr.Textbox())

demo.launch()
