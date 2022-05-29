import sys, time
import threading
import pyautogui  # useless trash so far
from pynput import mouse


"""
Unused
Testing code using pyautogui, useless trash
If KeyboardInterrupt (ctrl+c) doesn't stop execution in PyCharm: 
    go to "Run"/"Edit Configurations" and check "Emulate terminal in output console"    
"""
def testAutoGui():
    print('Press ctrl+c to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            posStr = 'X: ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4)
            print(posStr, end='\n')
            # print('\b' * len(posStr), end='', flush=False)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n')

"""
Unused
Mouse monitoring code from pynput doc: https://pynput.readthedocs.io/en/latest/mouse.html
"""
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))