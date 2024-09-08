import gradio as gr

shortcut_js = """
<script>
function handleKeyboardShortcuts(e) {
    if (e.key === 'a' && e.altKey) {
        document.getElementById('shortcut-button').click();
    }
}
document.addEventListener('keydown', handleKeyboardShortcuts);
</script>
"""

with gr.Blocks(head=shortcut_js) as demo:
    gr.Button("Shortcut Activated", elem_id="shortcut-button", value="Clicked!")
    
demo.launch()
