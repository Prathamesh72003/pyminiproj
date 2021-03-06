import bookingModule as booking
import varModule as var
import roomInfoModule as room
import roomServiceModule as roomServe
import paymentModule as payment
import recordModule as record
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

class exce(Exception):
    def __init__(self):
        record()

def record():
    var.hear
    with sr.Microphone() as source:
        var.hear.adjust_for_ambient_noise(source)
       # var.hear.energy_threshold(int(800))
        print("Listening...")
        audio = var.hear.listen(source)
        try:
            text = var.hear.recognize_google(audio)
            return text
        except:
            print("Could not listene")
            # raise(exce())
     
save_path = "./AudioFiles"      
def tts(text,fileName):
    var.hear
    output = gTTS(text=text, lang=var.lang, slow=False)
    completeName = os.path.join(save_path, fileName+".mp3")
    output.save(completeName)
    playsound("./AudioFiles/"+fileName+".mp3")