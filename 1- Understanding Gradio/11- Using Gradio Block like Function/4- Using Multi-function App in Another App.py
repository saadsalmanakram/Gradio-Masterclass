import gradio as gr

# Load the multi-function translation app
translator_app = gr.load(name="spaces/your-username/multi-function-translator")

# Define a function to use a specific function from the loaded app
def translate_text(text, language):
    if language == "French":
        return translator_app(text, api_name="translate-to-french")[0]["translation_text"]
    elif language == "Spanish":
        return translator_app(text, api_name="translate-to-spanish")[0]["translation_text"]
    else:
        return "Language not supported."

# Create a new Gradio Blocks app that uses the loaded app
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input Text")
            language = gr.Dropdown(choices=["French", "Spanish"], label="Language")
            translate_btn = gr.Button("Translate")
        with gr.Column():
            translation_output = gr.Textbox(label="Translation")

    translate_btn.click(translate_text, inputs=[input_text, language], outputs=translation_output)
    gr.Examples([("Hello, how are you?", "French"), ("What time is it?", "Spanish")], inputs=[input_text, language])

demo.launch()
