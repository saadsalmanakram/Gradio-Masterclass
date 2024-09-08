import gradio as gr

css = """
.tooltip {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 5px;
    padding: 5px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 0.3s;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
"""

with gr.Blocks(css=css) as demo:
    gr.HTML("""
        <div class="tooltip">Hover over me
            <span class="tooltiptext">Tooltip text</span>
        </div>
    """)
    
demo.launch()
