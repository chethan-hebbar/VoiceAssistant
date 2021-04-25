# lantern version 0.00 (a simple voice assistant)
import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr

# text to speech engine
tts_engine = pyttsx3.init()

# rate                 
tts_engine.setProperty('rate', 215)

# volume                
tts_engine.setProperty('volume',1.5)    

# type 
voices = tts_engine.getProperty('voices')
tts_engine.setProperty("voice", voices[16].id)

# speech recognition
r = sr.Recognizer()
with sr.Microphone() as source:
    tts_engine.say("Hi, I am Lantern, what do you want me to find out?")
    tts_engine.runAndWait()
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Could not recognize")


#getting the number of words in the string
words = text.split()


# wolframalpha responses
if(len(words) > 3):
    wolf = wolframalpha.Client("GQ6HLR-P7RVW4888U")
    response = wolf.query(text)
    wolf_response = next(response.results).text
    tts_engine.say("This is what I found on Wolfram, {}".format(wolf_response))
    tts_engine.runAndWait()


# wikipedia results
wikipedia.set_lang("en")
if(len(words) == 1):
    wiki_page = wikipedia.page(text)
    wiki_summary = wikipedia.summary(text, sentences = 1)
    tts_engine.say("This is what I found on Wikipedia, {}".format(wiki_summary))
    tts_engine.runAndWait()

    with sr.Microphone() as source:
        tts_engine.say("Do you want me to find out more?")
        tts_engine.runAndWait()
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if(text == "yes" | text == "yeah" | text == "Yes" | text == "Yeah" | text == "yes please"):
                tts_engine.say("{}".format(wiki_page.content))
                tts_engine.runAndWait()
        except:
            print("Could not recognize")    
    

else:
    wiki_search = wikipedia.search(text)
    tts_engine.say("This is what I found on Wikipedia, {}".format(wiki_search))
    tts_engine.runAndWait()



