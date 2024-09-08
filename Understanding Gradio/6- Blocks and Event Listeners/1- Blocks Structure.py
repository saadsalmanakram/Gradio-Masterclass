import gradio as gr

def cube(number):
    return number ** 3

with gr.Blocks() as demo:
    number_input = gr.Number(label="Enter a number")
    cube_output = gr.Number(label="Cube of the number")
    calculate_button = gr.Button("Calculate Cube")
    calculate_button.click(fn=cube, inputs=number_input, outputs=cube_output)

demo.launch()
