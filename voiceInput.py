import speech_recognition as sr

r = sr.Recognizer()
OPENAI_API_KEY = "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"

async def startVoiceInput(ctx):
    await ctx.send("[DEBUG] Damn... Not here")
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        voiceInput = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
        print(f"Whisper API thinks you said {voiceInput}")
        await ctx.send(voiceInput)
    except sr.RequestError as e:
        print("Could not request results from Whisper API")

# try:
#     print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
# except sr.RequestError as e:
#     print("Could not request results from Whisper API")

