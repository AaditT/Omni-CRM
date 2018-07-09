import speech_recognition

def audiofileToText(file):
    rec = speech_recognition.Recognizer()
    audiof = speech_recognition.AudioFile(file)
    with audiof as source:
        audio = rec.record(source)
        print(str(rec.recognize_wit(audio, 'YQA7LNG7EN4NKFJH6DUO2UG3R37L6OWR')))
 
 def speechToText():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        print(str(rec.recognize_wit(audio, 'YQA7LNG7EN4NKFJH6DUO2UG3R37L6OWR')))
