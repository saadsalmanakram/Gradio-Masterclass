import gradio as gr

def transform_text(text):
    return text.upper()

interface = gr.Interface(
    fn=transform_text,
    inputs=gr.Textbox(label="Input Text"),
    outputs=gr.Textbox(label="Transformed Text")
)

interface.launch(share=True)