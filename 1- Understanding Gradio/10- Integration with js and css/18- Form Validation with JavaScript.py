import gradio as gr

js = """
function validateForm() {
    var nameInput = document.getElementById('name');
    var emailInput = document.getElementById('email');
    
    if (nameInput.value === '' || emailInput.value === '') {
        alert('All fields are required!');
        return false;
    }
    return true;
}

document.getElementById('submit-btn').onclick = validateForm;
"""

with gr.Blocks(js=js) as demo:
    gr.Textbox(placeholder="Name", elem_id="name")
    gr.Textbox(placeholder="Email", elem_id="email")
    gr.Button("Submit", elem_id="submit-btn")
    
demo.launch()
