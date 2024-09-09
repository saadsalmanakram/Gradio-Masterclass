import gradio as gr
import requests

def stock_price(message, history):
    symbol = message.strip().upper()
    api_key = "YOUR_FINANCIAL_API_KEY"  # Replace with your financial API key
    url = f"https://api.financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
    response = requests.get(url).json()
    
    if response:
        price = response[0]["price"]
        return f"The current price of {symbol} is ${price:.2f}."
    else:
        return "Sorry, I couldn't find the stock price for that symbol."

gr.ChatInterface(stock_price).launch()
