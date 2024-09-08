import gradio as gr

js = """
function changeColor() {
    document.getElementById('interactive-box').style.backgroundColor = 'yellow';
}
"""

with gr.Blocks(js=js) as demo:
    gr.Button("Change Color", elem_id="change-color-btn", js="changeColor()")
    gr.Box(elem_id="interactive-box", style={"width": "100px", "height": "100px", "background-color": "lightgray"})
    
demo.launch()
