import gradio as gr
import requests

def currency_converter(message, history):
    amount, from_currency, to_currency = message.split(";")
    amount = float(amount.strip())
    from_currency = from_currency.strip().upper()
    to_currency = to_currency.strip().upper()
    
    # Replace with your own API or a fixed exchange rate for demo purposes
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url).json()
    rate = response['rates'].get(to_currency, 0)
    
    if rate:
        converted_amount = amount * rate
        return f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}"
    else:
        return "Invalid currency code."

gr.ChatInterface(currency_converter).launch()
