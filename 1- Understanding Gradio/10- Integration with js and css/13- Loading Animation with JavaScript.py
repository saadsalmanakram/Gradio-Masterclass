import gradio as gr

js = """
function showLoading() {
    var loading = document.createElement('div');
    loading.id = 'loading-animation';
    loading.style.position = 'absolute';
    loading.style.top = '50%';
    loading.style.left = '50%';
    loading.style.transform = 'translate(-50%, -50%)';
    loading.style.fontSize = '2em';
    loading.style.color = 'blue';
    loading.innerText = 'Loading...';
    
    document.querySelector('.gradio-container').appendChild(loading);
    
    setTimeout(() => {
        loading.remove();
    }, 3000);
}
showLoading();
"""

with gr.Blocks(js=js) as demo:
    gr.Textbox(placeholder="Waiting for loading animation...")
    
demo.launch()
