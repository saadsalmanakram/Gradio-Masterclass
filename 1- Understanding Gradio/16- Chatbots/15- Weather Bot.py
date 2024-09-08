import gradio as gr
import requests

def weather_bot(message, history):
    city = message.strip()
    api_key = "YOUR_WEATHER_API_KEY"  # Replace with your weather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    
    if response["cod"] == 200:
        temp = response["main"]["temp"]
        description = response["weather"][0]["description"]
        return f"The current temperature in {city} is {temp}°C with {description}."
    else:
        return "Sorry, I couldn't find the weather for that city."

gr.ChatInterface(weather_bot).launch()
