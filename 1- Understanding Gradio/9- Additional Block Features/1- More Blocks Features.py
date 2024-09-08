# This example demonstrates how to use gr.Examples to provide predefined inputs for a function that determines if a number is prime and returns its factors.

import gradio as gr

def prime_factors(number):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if is_prime(number):
        return f"{number} is a prime number."
    else:
        factors = [i for i in range(1, number + 1) if number % i == 0]
        return f"Factors of {number}: {', '.join(map(str, factors))}"

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            number_input = gr.Number(value=10, label="Number")
            submit_button = gr.Button(value="Check")
        with gr.Column():
            result_output = gr.Textbox()

    submit_button.click(prime_factors, inputs=[number_input], outputs=[result_output])
    
    examples = gr.Examples(
        examples=[
            [7],
            [12],
            [17],
            [28],
        ],
        inputs=[number_input],
    )

if __name__ == "__main__":
    demo.launch()
