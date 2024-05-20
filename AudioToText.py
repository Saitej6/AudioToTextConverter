import threading
import speech_recognition as sr

recognizer = sr.Recognizer()

microphone = sr.Microphone()

stop_recording = False
def listen_for_stop():
    global stop_recording
    input("Press Enter to stop recording...")
    stop_recording = True

stop_thread = threading.Thread(target=listen_for_stop)
stop_thread.start()

with open("output.txt", "w") as file:
    with microphone as source:
        print("Listening for audio...")

        recognizer.adjust_for_ambient_noise(source)

        
        while not stop_recording:

            audio_data = recognizer.listen(source)

            try:
               
                text = recognizer.recognize_google(audio_data)
                print("Text converted from audio:", text)

                file.write(text + "\n")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("Recording stopped. Output saved to 'output.txt'.")
