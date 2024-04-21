import google_trans_new
import speech_recognition 
import gtts
import playsound




recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak now")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google_cloud(audio,language="fr")
    print(text)


translator = google_trans_new.Translator()
translation = translator.translate(text,dest="fr")
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang="fr")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3 ")
