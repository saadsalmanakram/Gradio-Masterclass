import gradio as gr

def calculate_bmi(height, weight):
    if height == 0:
        return "Height cannot be zero!"
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

demo = gr.Interface(
    fn=calculate_bmi,
    inputs=[gr.Number(label="Height (cm)", info="Enter your height in centimeters"), gr.Number(label="Weight (kg)", info="Enter your weight in kilograms")],
    outputs="text",
    title="BMI Calculator",
    description="Calculate your Body Mass Index (BMI) based on your height and weight."
)

demo.launch()
