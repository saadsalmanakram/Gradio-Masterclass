import gradio as gr

def multiply(x, y):
    return x * y

app = gr.Interface(
    fn=multiply,
    inputs=[gr.Number(), gr.Number()],
    outputs=gr.Textbox()
)

app.launch(inline=True)  # Runs the app directly in the browser
