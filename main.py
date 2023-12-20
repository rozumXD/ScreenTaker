import pyautogui
from pynput import mouse
from pynput.keyboard import Listener
from datetime import datetime


def start_ss():
    print('start_ss() started.')

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else '.',(x, y)))

        if not pressed:
            return False


    def take_the_screen(pressed):

        if pressed:
            fX, fY = pyautogui.position()
        else:
            sX, sY = pyautogui.position()

        today = datetime.today()
        todayTime = datetime.now()
        date_string = today.strftime("%d%m%Y") + todayTime.strftime("%H%M%S")

        image = pyautogui.screenshot('test_' + date_string + '.png', region=(fX, fY, sX, sY))

    take_the_screen()


    with mouse.Listener(
            on_click=on_click,
                        ) as mouseListener:
        mouseListener.join()


def on_press(key):
    input = ''
    try:
        input += key.char
        if input == 'p':
            print('P pressed, starting start_ss().')
            start_ss()
    except AttributeError:
        #do nothing, yet :)
        pass


if __name__ == '__main__':

    with Listener(on_press=on_press) as listener:  #keyboard listener//awaiting to be pressed 'p'
        listener.join()






