import gradio as gr
import sympy as sp

def math_solver(message, history):
    try:
        result = sp.sympify(message)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

gr.ChatInterface(math_solver).launch()
