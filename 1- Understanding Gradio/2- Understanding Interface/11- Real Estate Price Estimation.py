import gradio as gr

def estimate_price(location, size, bedrooms, bathrooms):
    base_price = 100000
    price = base_price + (size * 1500) + (bedrooms * 20000) + (bathrooms * 10000)
    if location == "Urban":
        price *= 1.2
    elif location == "Rural":
        price *= 0.8
    return round(price, 2)

demo = gr.Interface(
    fn=estimate_price,
    inputs=[
        gr.Dropdown(choices=["Urban", "Suburban", "Rural"], label="Location"),
        gr.Number(label="Size (in sq ft)"),
        gr.Slider(label="Number of Bedrooms", minimum=1, maximum=5),
        gr.Slider(label="Number of Bathrooms", minimum=1, maximum=4)
    ],
    outputs="number",
    title="Real Estate Price Estimator",
    description="Estimate the price of a property based on its location, size, and features."
)

demo.launch()
