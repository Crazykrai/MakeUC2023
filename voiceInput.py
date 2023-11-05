import speech_recognition as sr
import re

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

OPENAI_API_KEY = "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"

try:
    print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
except sr.RequestError as e:
    print("Could not request results from Whisper API")

