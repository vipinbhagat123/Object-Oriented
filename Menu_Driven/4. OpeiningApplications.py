import os
import webbrowser

def open_notepad():
    os.system("notepad.exe")
def open_chrome():
    webbrowser.open("http://www.google.com")
def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com/")

open_notepad()
open_chrome()
open_whatsapp()