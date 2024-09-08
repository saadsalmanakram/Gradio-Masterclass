import gradio as gr

js = """
function switchTheme() {
    var body = document.body;
    if (body.classList.contains('dark-theme')) {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
    } else {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var button = document.createElement('button');
    button.innerText = 'Switch Theme';
    button.onclick = switchTheme;
    document.querySelector('.gradio-container').appendChild(button);
});
"""

css = """
.dark-theme {background-color: black; color: white;}
.light-theme {background-color: white; color: black;}
"""

with gr.Blocks(css=css, js=js) as demo:
    gr.Textbox(placeholder="Theme will change after clicking the button...")
    
demo.launch()
