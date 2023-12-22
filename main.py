import pyautogui, os, sys
from pynput import mouse
from pynput.keyboard import Listener
from datetime import datetime
from PyQt5.QtWidgets import QApplication
from tkinter import *
import threading
from tkinter import ttk


def start_ss():
    print('start_ss() started.')

    def display_lock():
        print(f"Starting window.")
        root = Tk()

        width, height = pyautogui.size()
        size = str(width) + "x" + str(height)

        #Config
        #frm = ttk.Frame(root)
        root.geometry(size)
        root.configure(bg="#000000")
        root.attributes("-alpha", 0.2, '-topmost', True)
        #root.overrideredirect(True)
        root.mainloop()

    def capturing_screen():

        tabClickXY = []  # table storing x y where mouse clicked.

        def on_click(x, y, button, pressed):
            print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

            tabClickXY.append(x)
            tabClickXY.append(y)

            if not pressed:
                print(f"Listening ended. Starting take_the_screenshot().")
                take_the_screenshot()
                tryso()
                return False

        def take_the_screenshot():

            print(tabClickXY[0], tabClickXY[1])
            print(tabClickXY[-2], tabClickXY[-1])

            x, y = tabClickXY[0], tabClickXY[1]
            rx, ry = tabClickXY[-2], tabClickXY[-1]

            # getting todats date and time
            today = datetime.today()
            todayTime = datetime.now()
            date_string = today.strftime("%d%m%Y") + todayTime.strftime("%H%M%S")

            image = pyautogui.screenshot('test_' + date_string + '.png', region=(x, y, rx - x, ry - y))

        def tryso():
            app = QApplication(sys.argv)
            for screen in QApplication.screens():
                screen_path = os.path.expanduser(f"~/Desktop/{screen.name()}.jpg")
                screen.grabWindow(0).save(screen_path, 'jpg')
                # grabWindow(0) means full screen
                # for area use following format; x=0, y=0, w=-1, h=-1

        with mouse.Listener(
                on_click=on_click,
        ) as mouseListener:
            mouseListener.join()


    background_thread = threading.Thread(target=capturing_screen())

    background_thread.daemon = True
    background_thread.start()
    #display_lock()


def on_press(key):
    input = ''
    print('{0}'.format(key))
    try:
        input += key.char
        if input == 'p':
            print('P pressed, starting start_ss().')
            start_ss()
        if input != 'p':
            print(f'Trying to end process.')
            quit()
    except AttributeError:
            quit()
            #do nothing, yet :)


if __name__ == '__main__':

    def awaiting_p():
        with Listener(on_press=on_press) as listener:  # keyboard listener//awaiting to be pressed 'p'
            listener.join()


    bg_thread = threading.Thread(awaiting_p())










