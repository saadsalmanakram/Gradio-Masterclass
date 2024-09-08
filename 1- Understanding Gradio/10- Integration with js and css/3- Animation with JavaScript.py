import gradio as gr

js = """
function animateWelcome() {
    var welcomeText = document.createElement('h1');
    welcomeText.textContent = 'Welcome to the Demo!';
    welcomeText.style.fontSize = '2em';
    welcomeText.style.textAlign = 'center';
    welcomeText.style.opacity = '0';
    document.querySelector('.gradio-container').appendChild(welcomeText);

    let opacity = 0;
    const interval = setInterval(() => {
        opacity += 0.1;
        welcomeText.style.opacity = opacity;
        if (opacity >= 1) clearInterval(interval);
    }, 100);
}
animateWelcome();
"""

with gr.Blocks(js=js) as demo:
    gr.Textbox(placeholder="Type something...")
    
demo.launch()
