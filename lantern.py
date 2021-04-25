# lantern version 0.00 (a simple voice assistant)
import wolframalpha
import wikipedia
import pyttsx3

# text to speech engine
tts_engine = pyttsx3.init()

# wolframalpha responses
wolf = wolframalpha.Client("GQ6HLR-P7RVW4888U")
response = wolf.query("biggest planet in the solar system")
tts_engine.say(next(response.results).text)
tts_engine.runAndWait()


query = "facebook"
wikipedia.set_lang("en")
wiki_summary = wikipedia.summary(query, sentences = 1)
wiki_search = wikipedia.search(query)
wiki_page = wikipedia.page(query)

print(wiki_summary)
