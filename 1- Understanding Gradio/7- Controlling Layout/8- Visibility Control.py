import gradio as gr

with gr.Blocks() as demo:
    name_box = gr.Textbox(label="Name")
    age_box = gr.Number(label="Age")
    show_summary_btn = gr.Button("Show Summary")

    with gr.Column(visible=False) as summary_col:
        summary_text = gr.Textbox(label="Summary")

    def show_summary(name, age):
        return {
            summary_col: gr.Column(visible=True),
            summary_text: f"Name: {name}, Age: {age}"
        }

    show_summary_btn.click(show_summary, [name_box, age_box], [summary_col, summary_text])

demo.launch()
