"""
Notes:
Using pynput (instead of winapi for cross-platform support, dont know if will work XD).
Pyautogui cannot read mouse button input, designed for automating input

Pynput to detect input & read mouse position:
    Listener class is a thread which means as soon as it has joined to the main thread no code will be executed after
    the .join() until the Listener is stopped.
    Call pynput.mouse.Listener.stop anywhere in the script to stop the thread or return False from a callback to stop
    the listener.
    Call listener.stop() in one of the definitions due to the fact that that the listener is now in scope and is an
    instance os Listener.

Pillow (PIL) to take screenshot & manage image, may be implemented in another file

"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
