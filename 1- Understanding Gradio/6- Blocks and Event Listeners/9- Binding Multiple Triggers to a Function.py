# Submitting a Form

import gradio as gr

def submit_form(name, age):
    return f"Name: {name}, Age: {age}"

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Name")
    age_input = gr.Number(label="Age")
    output_text = gr.Textbox(label="Output")
    submit_button = gr.Button("Submit")
    
    @gr.on(triggers=[name_input.submit, age_input.submit, submit_button.click], inputs=[name_input, age_input], outputs=output_text)
    def display_info(name, age):
        return submit_form(name, age)

demo.launch()
