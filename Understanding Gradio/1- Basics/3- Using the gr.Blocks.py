import gradio as gr

def reverse_text(text):
    return text[::-1]

with gr.Blocks() as demo:
    with gr.Row():
        text_input = gr.Textbox(label="Input Text")
        reverse_button = gr.Button("Reverse Text")
    output = gr.Textbox(label="Reversed Text")
    
    reverse_button.click(fn=reverse_text, inputs=text_input, outputs=output)

demo.launch(share=True)
