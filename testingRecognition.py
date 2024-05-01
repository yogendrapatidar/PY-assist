# # Python program to translate
# # speech to text and text to speech


# import speech_recognition as sr
# import pyttsx3
# import time
# # Initialize the recognizer
# r = sr.Recognizer()

# # Function to convert text to
# # speech
# def SpeakText(command):
	
# 	# Initialize the engine
# 	engine = pyttsx3.init()
# 	engine.say(command)
# 	engine.runAndWait()
	
	
# # Loop infinitely for user to
# # speak
# print("start")

# # Exception handling to handle
# # exceptions at the runtime
# # print("start")
# try:
    
#     # use the microphone as source for input.
#     with sr.Microphone() as source2:
        
#         SpeakText("Please speak")
#         # wait for a second to let the recognizer
#         # adjust the energy threshold based on
#         # the surrounding noise level
        
#         r.adjust_for_ambient_noise(source2, duration=1)
        
#         #listens for the user's input
#         audio2 = r.listen(source2)
#         print("Processing")
#         SpeakText("Processing")
#         print("wait a min")
        
#         # Using google to recognize audio
#         MyText = r.recognize_google(audio2)
#         MyText = MyText.lower()

#         print("\nDid you say ",MyText)
#         SpeakText(MyText)
                    
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))
    
# except sr.UnknownValueError:
#     print("unknown error occurred")
    
    
# SpeakText("Program End")
# print("end")






import speech_recognition as sr
import pyttsx3
import identifyMusicTitle as imt

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
# speakText("hey utsav")


print("Program Started")
# print("Speak now!!")
#audio input
while(1):
    try:
        with sr.Microphone() as source2:
            print("Speak now!!")
            speakText("Please Speak!!")
            recog.adjust_for_ambient_noise(source2,1)

            audio2=recog.listen(source2)
            print("processing")
            speakText("processing")
            print("Wait a min")

            mytext=recog.recognize_google(audio2)
            mytext=mytext.lower()

            if(mytext=='CANCEL' or mytext=='CLOSE' or mytext=='END' or mytext=='7'):
                print("Closing")
                break

            print("did you say: ",mytext)
            speakText(mytext)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occurred")

print("Program End")
speakText("Closing the program")

