import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(), gr.Slider(minimum=1, maximum=5)],
    outputs=gr.Textbox(),
)

demo.launch(share=True)

