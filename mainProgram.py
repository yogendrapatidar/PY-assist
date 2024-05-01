import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
from AppOpener import *


import identifyMusicTitle as imt
# import identifySearchCommand as isc
import identifyOpenCommand as ioc
import identifyCloseCommand as icc

recog=sr.Recognizer()

# recog.energy_threshold=300
recog.dynamic_energy_threshold=True
recog.dynamic_energy_adjustment_damping=0.25
recog.pause_threshold=0.6

def speakText(text):
    Speakobj=pyttsx3.init()
    Speakobj.setProperty('rate',150)
    Speakobj.say(text)
    Speakobj.runAndWait()


print("Program Started")

while(1):
    try:
        with sr.Microphone() as source2:

            recog.adjust_for_ambient_noise(source2,1)
            print("Speak now!!")
            speakText("Please Speak!!")

            audio2=recog.listen(source2)
            print("processing")
            speakText("processing") 
            print("Wait a min")

            mytext=recog.recognize_google(audio2)
            mytext=mytext.upper()

            if(mytext=='CANCEL' or mytext=='CLOSE' or mytext=='END' or mytext=='7'):
                print("Closing")
                break


            print("You said: ",mytext)
            speakText(mytext)

            ocommand=ioc.identifyOpenC(mytext)
            if(ocommand!="not open command"):
                print("OPENING: ",ocommand)
                speakText("opening")
                speakText(ocommand)
                open(mytext,match_closest=True)
                time.sleep(3)
                continue
            
            ccommand=icc.identifyCloseC(mytext)
            if(ccommand!="not close command"):
                print("CLOSING: ",ccommand)
                speakText("closing")
                speakText(ccommand)
                close(ccommand,match_closest=True)
                continue

            mcommand=imt.identifyMusic(mytext)
            if(mcommand!='no music'):
                #code to play music
                print("Playing")
                pywhatkit.playonyt(mcommand)
                speakText("playing")
                speakText(mcommand)
                speakText("on youtube")
                time.sleep(10)
                continue

            
            pywhatkit.search(mytext)
                # break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occurred")

print("Program End")
print("Thank You")
speakText("thank you")
speakText("Closing the program")

      