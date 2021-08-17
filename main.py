#main file.
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

#sintetisador de voz
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-3].id)

def speek(text):
    engine.say(text)
    engine.runAndWait()

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p= pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            speek(text)