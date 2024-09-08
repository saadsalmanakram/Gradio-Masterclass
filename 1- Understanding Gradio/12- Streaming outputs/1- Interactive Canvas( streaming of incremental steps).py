import gradio as gr
import numpy as np
import time

def gradual_painting(steps):
    # Initialize a white canvas
    canvas_size = (600, 600, 3)
    canvas = np.ones(canvas_size, np.uint8) * 255  # White canvas
    
    for step in range(steps):
        # Simulate some painting process: fill random parts of the canvas with random colors
        x = np.random.randint(0, canvas_size[0])
        y = np.random.randint(0, canvas_size[1])
        color = np.random.randint(0, 255, size=3)  # Random color
        
        # Paint a small square on the canvas
        canvas[x:x+10, y:y+10] = color
        
        # Add a delay to simulate gradual painting
        time.sleep(0.5)
        yield canvas

    # Final step: Add a diagonal line to mark the completion
    for i in range(min(canvas_size[0], canvas_size[1])):
        canvas[i, i] = [0, 0, 255]  # Blue diagonal line
    
    yield canvas

demo = gr.Interface(gradual_painting,
                    inputs=gr.Slider(5, 50, 10, step=5, label="Steps"),
                    outputs="image",
                    description="Watch as the canvas gets painted step by step.")

demo.launch()
