import gtts  #google text to speech
import playsound
text = input("Enter here: ")
# create a varibale
sound = gtts.gTTS(text,lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")

