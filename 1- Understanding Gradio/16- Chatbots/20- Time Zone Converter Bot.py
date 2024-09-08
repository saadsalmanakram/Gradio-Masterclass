import gradio as gr
from datetime import datetime
import pytz

def time_zone_converter(message, history):
    try:
        time, from_tz, to_tz = message.split(";")
        time = datetime.strptime(time.strip(), "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz.strip())
        to_tz = pytz.timezone(to_tz.strip())
        
        local_time = from_tz.localize(time)
        converted_time = local_time.astimezone(to_tz)
        return f"Converted Time: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error: {str(e)}"

gr.ChatInterface(time_zone_converter).launch()
