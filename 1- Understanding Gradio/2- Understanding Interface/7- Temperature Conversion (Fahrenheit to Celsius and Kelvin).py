import gradio as gr

def convert_temperature(temp_fahrenheit):
    celsius = (temp_fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    return round(celsius, 2), round(kelvin, 2)

demo = gr.Interface(
    fn=convert_temperature,
    inputs=gr.Number(label="Temperature in Fahrenheit"),
    outputs=["number", "number"],
    title="Temperature Converter",
    description="Convert Fahrenheit to Celsius and Kelvin."
)

demo.launch()
