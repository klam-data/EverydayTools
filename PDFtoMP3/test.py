import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices)


## Voice 0
engine.setProperty('voice', voices[0].id)
engine.say("Hello World!")
engine.runAndWait()
engine.stop()

## Voice 1
engine.setProperty('voice', voices[1].id)
engine.say("Hello World!")
engine.runAndWait()
engine.stop()

## Voice 2
engine.setProperty('voice', voices[2].id)
engine.say("Hello World!")
engine.runAndWait()
engine.stop()