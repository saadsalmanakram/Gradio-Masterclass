# This example shows how to use gr.Timer() to update a textbox with the current temperature and a random weather condition periodically.

import gradio as gr
import random
import time

def get_temperature():
    return round(random.uniform(15.0, 30.0), 1)

def get_weather_condition():
    conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy"]
    return random.choice(conditions)

with gr.Blocks() as demo:
    timer = gr.Timer(2)
    temperature = gr.Number(label="Temperature (°C)")
    weather = gr.Textbox(label="Weather Condition")

    timer.tick(lambda: get_temperature(), outputs=temperature)
    weather.update(lambda: get_weather_condition(), every=timer)

    with gr.Row():
        gr.Button("Start Updates").click(lambda: gr.Timer(active=True), None, timer)
        gr.Button("Stop Updates").click(lambda: gr.Timer(active=False), None, timer)
        gr.Button("Speed Up").click(lambda: 1, None, timer)

if __name__ == "__main__":
    demo.launch()
