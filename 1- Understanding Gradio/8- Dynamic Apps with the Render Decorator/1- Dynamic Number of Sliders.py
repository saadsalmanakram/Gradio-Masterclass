# This example creates a variable number of sliders based on user input. Each slider is used to adjust a single value, and the final output displays the average value of all sliders.

import gradio as gr

with gr.Blocks() as demo:
    num_sliders = gr.State(1)  # Start with 1 slider
    add_slider_btn = gr.Button("Add Slider")
    remove_slider_btn = gr.Button("Remove Slider")
    
    @gr.render(inputs=num_sliders)
    def render_sliders(count):
        sliders = []
        for i in range(count):
            slider = gr.Slider(minimum=0, maximum=100, label=f"Slider {i}", key=f"slider-{i}")
            sliders.append(slider)
        
        def calculate_average(*values):
            return sum(values) / len(values) if values else 0
        
        average_btn = gr.Button("Calculate Average")
        output = gr.Number(label="Average Value")
        average_btn.click(calculate_average, inputs=set(sliders), outputs=output)

    add_slider_btn.click(lambda x: x + 1, num_sliders, num_sliders)
    remove_slider_btn.click(lambda x: max(x - 1, 1), num_sliders, num_sliders)

demo.launch()
