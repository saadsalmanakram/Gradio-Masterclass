import gradio as gr

def count_files(message, history):
    num_files = len(message["files"])
    return f"You uploaded {num_files} files"

demo = gr.ChatInterface(fn=count_files, examples=[{"text": "Hello", "files": []}], title="File Counter Bot", multimodal=True)
demo.launch()
