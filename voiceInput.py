import speech_recognition as sr
import os

from search import gpt_summarize, query_google
from dotenv import load_dotenv

r = sr.Recognizer()
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAPI_API_KEY')

bazingaList = ['bazinga', 'Bazinga', 'Bazinga!', 'Bazinga.', 'bazinga.']
pauseFlag = False

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

async def pauseCheck(flag):
    global pauseFlag
    if flag:
        pauseFlag = True
    else:
        pauseFlag = False

async def bazingaCheck(spokenList):
    if pauseFlag == True:
        return True
    for bazinga in bazingaList:
        if (bazinga in spokenList):
            return True
    return False

async def startVoiceInput(ctx):
    spokenWords = []
    while not await bazingaCheck(spokenWords):
        spokenWords.clear()
        await ctx.tc.send("[DEBUG] Speech recognition activated!")
        with sr.Microphone() as source:
            print("Say something!")
            await ctx.tc.send("[DEBUG] Say something!")
            audio = r.listen(source)
        try:
            voiceInput: str = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
            if voiceInput:
                print(f"Whisper API thinks you said {voiceInput}")
                await ctx.tc.send(voiceInput)
                spokenWords = voiceInput.split(' ')
                spokenWords = [word.replace(',', '') for word in spokenWords]
                command = spokenWords[0]
                params = voiceInput.replace(command, '')
                print(params)
                print(command)
                if command.lower() in voiceCommands:
                    await voiceCommands.get(command.lower())(ctx, params)    
        except sr.RequestError as e:
            print("Could not request results from Whisper API")

    await ctx.tc.send("[DEBUG] Exiting speech recognition!")    

