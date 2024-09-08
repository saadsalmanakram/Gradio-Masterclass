import gradio as gr
import time

def process_files(files, progress=gr.Progress()):
    results = []
    for file in progress.tqdm(files, desc="Processing Files"):
        time.sleep(0.5)
        results.append(f"Processed {file.name}")
    return "\n".join(results)

demo = gr.Interface(process_files, gr.File(file_count="multiple"), gr.Textbox())

demo.launch()
