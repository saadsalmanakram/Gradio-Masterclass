import gradio as gr
import time

def analyze_text(text, progress=gr.Progress()):
    progress(0, desc="Analyzing Text")
    word_count = len(text.split())
    for _ in progress.tqdm(range(word_count), desc="Analyzing Words"):
        time.sleep(0.1)
    progress(1, desc="Finished")
    return f"Word Count: {word_count}"

demo = gr.Interface(analyze_text, gr.Textbox(), gr.Textbox())

demo.launch()
