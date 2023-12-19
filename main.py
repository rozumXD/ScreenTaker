import pyautogui
from pynput.keyboard import Key, Listener


def start_ss():
    image = pyautogui.screenshot('test.png')


def on_press(key):
    input = ''
    try:
        input += key.char
        if input == 'p':
            start_ss()
    except AttributeError:
        #do nothing :)
        pass


if __name__ == '__main__':

    with Listener(
            on_press=on_press) as listener:
        listener.join()
