import gradio as gr

def process_file(file):
    content = file.read().decode("utf-8")
    return content.upper()

interface = gr.Interface(
    fn=process_file,
    inputs=gr.File(label="Upload Text File"),
    outputs=gr.Textbox(label="Processed Content")
)

interface.launch()
