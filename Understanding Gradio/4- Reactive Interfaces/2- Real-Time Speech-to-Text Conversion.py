# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:02:12 2024

@author: saads
"""

# In this example, we use a microphone to continuously stream audio input, and a speech recognition function processes the audio to return the recognized text in real-time.

import gradio as gr
import speech_recognition as sr

# Function to recognize speech
def recognize_speech(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Sorry, could not understand the audio."
        except sr.RequestError:
            text = "Error with the recognition service."
    return text

# Create the Gradio Interface with streaming audio
demo = gr.Interface(
    fn=recognize_speech,
    inputs=gr.Audio(source="microphone", streaming=True),
    outputs="text",
    live=True
)

demo.launch()
