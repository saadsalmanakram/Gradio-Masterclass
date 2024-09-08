# This example demonstrates how to create a text classification interface with a customizable input and output.

import gradio as gr

def classify_text(text):
    # A simple mock classification
    if "happy" in text.lower():
        return "Positive", 0.9
    else:
        return "Negative", 0.1

demo = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(label="Input Text", placeholder="Enter some text here...", lines=2),
    outputs=[gr.Label(label="Sentiment"), gr.Number(label="Confidence Score")],
    title="Text Sentiment Classifier",
    description="Classify the sentiment of your input text as Positive or Negative."
)

demo.launch()
