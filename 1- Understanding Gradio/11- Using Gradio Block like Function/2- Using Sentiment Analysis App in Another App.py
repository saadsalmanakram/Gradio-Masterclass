import gradio as gr

# Load the sentiment analysis app
sentiment_analyzer = gr.load(name="spaces/your-username/sentiment-analysis")

# Define another function that uses the sentiment analysis app
def process_and_analyze(text):
    sentiment = sentiment_analyzer(text)
    return f"The sentiment is: {sentiment}"

# Create a new Gradio Blocks app that uses the loaded app
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input Text")
            process_btn = gr.Button("Process and Analyze")
        with gr.Column():
            result_output = gr.Textbox(label="Result")

    process_btn.click(process_and_analyze, inputs=input_text, outputs=result_output)
    gr.Examples(["I am excited about learning new things!", "I am feeling a bit down today."], inputs=[input_text])

demo.launch()
