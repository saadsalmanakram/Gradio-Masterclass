import gradio as gr

def concatenate_strings(str1, str2):
    return str1 + " " + str2

with gr.Blocks() as demo:
    with gr.Row():
        input1 = gr.Textbox(label="First String")
        input2 = gr.Textbox(label="Second String")
        output = gr.Textbox(label="Concatenated Result")
    
    btn = gr.Button("Concatenate")
    btn.click(fn=concatenate_strings, inputs=[input1, input2], outputs=output)

demo.launch(share=True)
