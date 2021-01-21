import speech_recognition as sr
import pocketsphinx

r = sr.Recognizer()

# Now, let’s create an instance of Microphone.
mic = sr.Microphone()

print(sr.Microphone.list_microphone_names())

with mic as source:
    r.adjust_for_ambient_noise(source)
    #r.energy_threshold = 1000
    #r.pause_threshold = 1
    for n in range(10):
        try:
            print(".", end="")
            audio = r.listen(source)
#             z = r.recognize_google(audio)
#             print(z, n)
            z = r.recognize_sphinx(audio, language="en-US", keyword_entries = [("yes",1)],
                               show_all=pocketsphinx.pocketsphinx.Decoder)
            print(z.__dict__)
            print(f"{n}:{z.get_in_speech()}", end=" ")
        except Exception as e:
            print(f"*** {e}", end="") 


                   
