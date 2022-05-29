"""
Modified from https://stackoverflow.com/questions/53339048/pynput-stop-listener-from-outside

try this:
https://stackoverflow.com/questions/57567885/is-there-any-way-in-python-to-let-a-user-select-bounding-box-from-mouse-clicks
"""
from pynput import mouse

logger_stop = False
points = []

class Mouselogger:
    def __init__(self):
        Mouselogger.Mouse.Listener()

    class Mouse:
        def Click(x, y, b, p):
            global logger_stop
            global points

            if logger_stop == True:
                return False

            # hold mouse button pressed, on release reset the progress
            elif b == mouse.Button.left:
                if p == True:
                    pass
            else:
                print(f"{b} was {'pressed' if p else 'released'} at ({x} x {y})")
                mouse.Listener.stop
                print("stopped")

        def Listener(self):
            mouse.Listener(on_click = Mouselogger.Mouse.Click).start()

class Main:
    def __init__(self):
        Mouselogger()

if __name__ == "__main__":
    Main()