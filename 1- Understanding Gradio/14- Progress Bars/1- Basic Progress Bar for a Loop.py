import gradio as gr
import time

def count_down(n, progress=gr.Progress()):
    progress(0, desc="Starting Countdown")
    for i in progress.tqdm(range(n), desc="Counting Down"):
        time.sleep(0.5)
    return "Countdown Complete!"

demo = gr.Interface(count_down, gr.Number(value=10), gr.Textbox())

demo.launch()
