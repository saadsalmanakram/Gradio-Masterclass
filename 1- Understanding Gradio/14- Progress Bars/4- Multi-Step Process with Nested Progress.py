import gradio as gr
import time

def multi_step_process(n, progress=gr.Progress()):
    progress(0, desc="Starting Process")
    for i in progress.tqdm(range(n), desc="Step 1"):
        time.sleep(0.2)
    progress(0.5, desc="Step 2")
    time.sleep(2)
    progress(1, desc="Completed")
    return "Process Complete!"

demo = gr.Interface(multi_step_process, gr.Number(value=5), gr.Textbox())

demo.launch()
