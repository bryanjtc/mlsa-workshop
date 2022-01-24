import speech_recognition as sr
import pyttsx3, pywhatkit

name= "juanita"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def talk(words):
    engine.say(words)
    engine.runAndWait()
    
def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Escuchando mi pana...")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entiendo, intenta nuevamente")
    return rec

def run_juanita():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            talk("No te entiendo, intenta nuevamente")
            continue
        if name in rec:
            rec =rec.replace(name, "").strip()
            if 'reproduce' in rec:
                song = rec.replace('reproduce', '').strip()
                pywhatkit.playonyt(song)
                talk(f"Reproduciendo {song}.")
                
if __name__ == "__main__":
    run_juanita()