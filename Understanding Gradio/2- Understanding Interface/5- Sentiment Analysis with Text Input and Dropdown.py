import gradio as gr

def analyze_sentiment(text, model_choice):
    if model_choice == "Simple Model":
        return "Positive" if "good" in text else "Negative"
    else:
        return "Advanced Positive" if "excellent" in text else "Advanced Negative"

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=["text", gr.Dropdown(choices=["Simple Model", "Advanced Model"], label="Model Choice")],
    outputs="text",
    title="Sentiment Analysis Demo",
    description="Analyze the sentiment of a given text using either a simple or advanced model.",
)

demo.launch()
