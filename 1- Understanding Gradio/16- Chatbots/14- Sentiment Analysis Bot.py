from textblob import TextBlob
import gradio as gr

def sentiment_analysis(message, history):
    analysis = TextBlob(message)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative"
    return f"The sentiment of your message is {sentiment}."

gr.ChatInterface(sentiment_analysis).launch()
