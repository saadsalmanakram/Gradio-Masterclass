# This example uses an accordion to hide additional inputs, keeping the interface clean.

import gradio as gr

def create_summary(text, length, detailed=False):
    summary = text[:length] + ("..." if len(text) > length else "")
    if detailed:
        summary += f" (Length: {len(text)})"
    return summary

demo = gr.Interface(
    fn=create_summary,
    inputs=[
        gr.Textbox(label="Input Text", placeholder="Enter text here..."),
        gr.Slider(minimum=50, maximum=500, step=10, value=100, label="Summary Length"),
    ],
    outputs="text",
    additional_inputs=[
        gr.Checkbox(label="Show Detailed Summary")
    ],
    title="Text Summary Creator",
    description="Generate a summary of the provided text with adjustable length and optional detail."
)

demo.launch()
