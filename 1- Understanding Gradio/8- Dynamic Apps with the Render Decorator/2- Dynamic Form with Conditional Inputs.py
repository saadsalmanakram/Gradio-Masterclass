# This example creates a dynamic form where the number of text inputs depends on the user's choice. The form also includes a submit button that collects the input values.

import gradio as gr

with gr.Blocks() as demo:
    num_inputs = gr.State(1)  # Start with 1 text input
    input_type = gr.Radio(["Short Text", "Long Text"], value="Short Text")
    
    @gr.render(inputs=[num_inputs, input_type])
    def render_form(count, form_type):
        inputs = []
        for i in range(count):
            if form_type == "Short Text":
                text_input = gr.Textbox(label=f"Input {i}", key=f"text-{i}")
            else:
                text_input = gr.Textbox(label=f"Input {i}", lines=3, key=f"long-text-{i}")
            inputs.append(text_input)
        
        def collect_inputs(*values):
            return ", ".join(values)
        
        submit_btn = gr.Button("Submit")
        output = gr.Textbox(label="Collected Inputs")
        submit_btn.click(collect_inputs, inputs=set(inputs), outputs=output)

    add_input_btn = gr.Button("Add Input")
    remove_input_btn = gr.Button("Remove Input")
    add_input_btn.click(lambda x: x + 1, num_inputs, num_inputs)
    remove_input_btn.click(lambda x: max(x - 1, 1), num_inputs, num_inputs)

demo.launch()
