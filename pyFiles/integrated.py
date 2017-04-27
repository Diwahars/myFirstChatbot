import aiml
import os
import pyttsx
import speech_recognition as sr

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
    		print("Say something!")
    		audio = r.listen(source)
	try:
		message = r.recognize_google(audio)
		print("You: " + message)
    		if message == "quit":
        		exit()
    		elif message == "save":
        		kernel.saveBrain("bot_brain.brn")
    		else:
			engine = pyttsx.init()
        		bot_response = kernel.respond(message)
			engine.say(bot_response)
			print bot_response
			engine.runAndWait()
	except sr.UnknownValueError:
    		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
    		print("Could not request results from Google Speech Recognition service; {0}".format(e))

