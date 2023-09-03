import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[2].id)

engine.say("Oi Jéssica, você é muito linda e seu marido é ainda mais lindo.")
engine.runAndWait()