import gradio as gr

def translate_text(text, target_language):
    if target_language == "French":
        return f"Translated to French: {text}"
    elif target_language == "Spanish":
        return f"Translated to Spanish: {text}"
    else:
        return f"Translated to German: {text}"

demo = gr.Interface(
    fn=translate_text,
    inputs=[gr.Textbox(label="Text to Translate"), gr.Dropdown(choices=["French", "Spanish", "German"], label="Target Language")],
    outputs="text",
    title="Text Translator",
    description="Translate text into different languages.",
)

demo.launch()
