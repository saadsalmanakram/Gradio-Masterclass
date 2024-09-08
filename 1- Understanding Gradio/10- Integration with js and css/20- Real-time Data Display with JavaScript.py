import gradio as gr

js = """
function updateTime() {
    var timeDisplay = document.getElementById('time-display');
    var now = new Date();
    timeDisplay.textContent = now.toLocaleTimeString();
}

setInterval(updateTime, 1000);
"""

with gr.Blocks(js=js) as demo:
    gr.HTML('<div id="time-display"></div>')
    
demo.launch()
