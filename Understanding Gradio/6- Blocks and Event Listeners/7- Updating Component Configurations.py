# Dynamic Dropdown Menu

import gradio as gr

def update_dropdown(category):
    if category == "Fruits":
        return gr.Dropdown(choices=["Apple", "Banana", "Cherry"], label="Items")
    elif category == "Vegetables":
        return gr.Dropdown(choices=["Carrot", "Lettuce", "Tomato"], label="Items")
    else:
        return gr.Dropdown(choices=[], label="Items", visible=False)

with gr.Blocks() as demo:
    category_choice = gr.Radio(choices=["Fruits", "Vegetables", "None"], label="Select Category")
    items_dropdown = gr.Dropdown(label="Items")
    category_choice.change(fn=update_dropdown, inputs=category_choice, outputs=items_dropdown)

demo.launch()

