"""
LEGACY IMPLEMENTATION NOT USING OOP
This module detects the state of mouse button,
and report the mouse position when mouse click or drag is detected.
"""
import sys, time
import threading
import pyautogui  # useless trash so far
from pynput import mouse


"""
Monitors mouse click (press & release) by left and right
Return an array [left, upper, right, lower] of PIL bbox parameters
"""
def on_click(x, y, button, pressed):
    btn = button.name
    points = []  # array containing the 4 parameters for PIL bbox, to be returned, implement with tuple?
    if btn == 'left':
        if pressed:
            print('Left is pressed.')
            # x, y = mouse.position
            posStr = 'X: ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4)
            print(posStr, end='\n')
            points.append(x)
            points.append(y)
        else:
            print('Left is released.')
            # x, y = mouse.position
            posStr = 'X: ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4)
            print(posStr, end='\n')
            points.append(x)
            points.append(y)
    else:
        pass
    return points

    """
    elif btn == 'right':
        if pressed:
            print('Right is pressed.')
        if not pressed:
            print('Right is released.')
        else:
            pass
    """


"""
A mouse listener is a threading.Thread, and all callbacks will be invoked from the thread.
Call pynput.mouse.Listener.stop from anywhere, raise StopException or return False from a callback to stop the listener.
    Long running procedures and blocking operations should not be invoked from the callback, as this risks freezing 
    input for all processes.
    A possible workaround is to just dispatch incoming messages to a queue, and let a separate thread handle them.
Once pynput.mouse.Listener.stop has been called, the listener cannot be restarted, since listeners are instances of 
threading.Thread.
If your application requires toggling listening events, you must either add an internal flag to ignore events when not
required, or create a new listener when resuming listening.

"""
def testMain():
    # testAutoGui()

    # Collect events until released (blocking)
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    """
    # non-blocking Listener thread, does it work???
    listener = mouse.Listener(on_move=on_move, on_click=on_click)
    listener.start()
    """

testMain()