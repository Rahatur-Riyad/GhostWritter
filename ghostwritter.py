import pyautogui as pag
import time
import speech_recognition as sr
import keyboard

r = sr.Recognizer()
listening = False
def toggle_listening():
    global listening
    listening = not listening
    if listening:
        print("ON")
    else:
        print("OFF")
keyboard.add_hotkey("ctrl+shift+space", toggle_listening)
while True:
    if listening:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source,timeout=5, phrase_time_limit=5)
                text = r.recognize_google(audio) + " "
                print("You said: " + text)
                if text.strip().lower() == "stop":
                    print("Stopping...")
                    break
                elif "enter" in text:
                    pag.press("enter")
                elif "new line" in text:
                    pag.hotkey("shift", "enter")
                elif "backspace" in text:
                    pag.press("backspace")
                else:
                    pag.typewrite(text,interval=0.01)
                    time.sleep(0.5)
            except sr.UnknownValueError:
                print("could not understand audio")
            except sr.WaitTimeoutError:
                print("Listening timed out")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
