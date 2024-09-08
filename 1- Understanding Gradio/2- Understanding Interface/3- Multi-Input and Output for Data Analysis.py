# In this example, a function takes multiple inputs (text, number, and boolean) and returns multiple outputs (text and number).


import gradio as gr

def analyze_data(name, is_active, score):
    status = "Active" if is_active else "Inactive"
    analysis = f"{name} is currently {status}. Score: {score}"
    return analysis, score * 10

demo = gr.Interface(
    fn=analyze_data,
    inputs=[gr.Textbox(label="Name"), gr.Checkbox(label="Is Active"), gr.Slider(minimum=0, maximum=100, step=1, label="Score")],
    outputs=[gr.Textbox(label="Analysis"), gr.Number(label="Adjusted Score")],
    title="Data Analysis Tool",
    description="Analyze data based on name, activity status, and score."
)

demo.launch()
