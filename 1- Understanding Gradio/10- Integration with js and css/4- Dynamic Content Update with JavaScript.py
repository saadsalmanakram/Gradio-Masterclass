import gradio as gr

js = """
function updateContent() {
    document.getElementById('dynamic-content').textContent = 'Updated Content!';
}
"""

with gr.Blocks(js=js) as demo:
    gr.Button("Update Content", elem_id="update-btn", js="updateContent()")
    gr.Textbox(value="Initial Content", elem_id="dynamic-content")
    
demo.launch()
