import pynput, random
import time

from pynput.keyboard import Key, Listener, Controller

klavye = pynput.keyboard.Controller()
calisiyor_mu = True

def durdurucu(key):
    global calisiyor_mu
    if key == Key.esc:
        print("Durdurdummmm")
        calisiyor_mu = False
        return False
    
Listener = Listener(on_press=durdurucu)
Listener.start()

while calisiyor_mu:

    klavye.press('w')
    time.sleep(0.1)
    klavye.release('w')
    bekleme_suresi = random.randint(240, 300)

    time.sleep(bekleme_suresi)
