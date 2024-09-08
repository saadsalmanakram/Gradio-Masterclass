import gradio as gr

js = """
function animateScroll() {
    var container = document.querySelector('.gradio-container');
    container.scrollTo({top: 100, behavior: 'smooth'});
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(animateScroll, 1000);
});
"""

with gr.Blocks(js=js) as demo:
    gr.Textbox(placeholder="This text box is at the top of a scrollable container...")
    
demo.launch()
