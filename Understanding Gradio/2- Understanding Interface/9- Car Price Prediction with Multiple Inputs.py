import gradio as gr

def predict_car_price(make, year, mileage, fuel_type):
    # Simple car price estimation logic
    base_price = 20000
    price = base_price - (2024 - year) * 1000 - mileage * 0.05
    if fuel_type == "Diesel":
        price -= 1500
    return max(price, 1000)

demo = gr.Interface(
    fn=predict_car_price,
    inputs=[
        gr.Textbox(label="Car Make"),
        gr.Slider(label="Year", minimum=2000, maximum=2024),
        gr.Number(label="Mileage (in km)"),
        gr.Radio(choices=["Petrol", "Diesel", "Electric"], label="Fuel Type")
    ],
    outputs="number",
    title="Car Price Predictor",
    description="Estimate the price of a used car based on its make, year, mileage, and fuel type."
)

demo.launch()
