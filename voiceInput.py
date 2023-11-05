import speech_recognition as sr

from search import gpt_summarize, query_google

r = sr.Recognizer()
OPENAI_API_KEY = "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"


async def searchGoogle(ctx, q):
    googleUrls = query_google(q)
    print(googleUrls)
    gptSummaries = [await gpt_summarize(x) for x in googleUrls]
    print(gptSummaries)
    for url, summary in zip(googleUrls, gptSummaries):
        await ctx.tc.send(url['link'] + ' - ' + summary.choices[0].message.content)

async def send(ctx, message):
    members = ctx.vc.members
    memusernames = []
    for member in members:
        memusernames.append(member)
    await ctx.tc.send(str(memusernames[-1]) + " " + message)

voiceCommands = {"search": searchGoogle, "send": send}


async def startVoiceInput(ctx):
    spokenWords = []

    while 'bazinga' not in spokenWords:

        await ctx.tc.send("[DEBUG] Damn... Not here")
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            voiceInput: str = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
            print(f"Whisper API thinks you said {voiceInput}")
            await ctx.tc.send(voiceInput)
            spokenWords = voiceInput.split(' ')
            spokenWords = [word.replace(',', '') for word in spokenWords]
            command = spokenWords[0]
            params = voiceInput.replace(command, '')
            print(params)
            print(command)
            voiceCommands.get(command)(ctx, params)
            spokenWords.clear()
        except sr.RequestError as e:
            print("Could not request results from Whisper API")

# try:
#     print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
# except sr.RequestError as e:
#     print("Could not request results from Whisper API")

