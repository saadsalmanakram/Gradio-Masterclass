# This example demonstrates how to use a pre-existing Gradio Blocks app (a sentiment analysis app) like a function within another app.

import gradio as gr
from transformers import pipeline

# Define the sentiment analysis function
sentiment_pipe = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    return sentiment_pipe(text)[0]["label"]

# Create a Gradio Blocks app for sentiment analysis
with gr.Blocks() as sentiment_demo:
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Text Input")
            analyze_btn = gr.Button("Analyze Sentiment")
        with gr.Column():
            sentiment_output = gr.Textbox(label="Sentiment")

    analyze_btn.click(analyze_sentiment, inputs=text_input, outputs=sentiment_output)
    gr.Examples(["I love Gradio!", "This is terrible."], inputs=[text_input])

sentiment_demo.launch()
