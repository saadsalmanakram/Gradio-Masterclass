import gradio as gr

def square(number):
    return number ** 2

iface = gr.Interface(
    fn=square,
    inputs=gr.Slider(minimum=0, maximum=10, step=1),
    outputs=gr.Textbox()
)

iface.launch(share=True)