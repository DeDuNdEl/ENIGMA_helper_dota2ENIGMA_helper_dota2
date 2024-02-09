import pyautogui as pag
import time
from pygame import mixer


def check_black_hole():
    try:
        location = pag.locateOnScreen('black_hole_cast.png', confidence  = 0.97)
        return True
    except pag.ImageNotFoundException:
        return False


def main():
    checker = True
    is_black_hole = 0

    mixer.init()

    while True:
        time.sleep(0.1)

        if check_black_hole():
            if checker and is_black_hole == 0:

                mixer.music.load("otpusti_menya.mp3")
                mixer.music.play()
                checker = False

                is_black_hole = 1

        else:
            if is_black_hole == 1:
                time.sleep(1.5) #время проигрыша музыки после дачи блек хола

            if checker == False and check_black_hole() == False:
                checker = True
                is_black_hole = 0
                mixer.music.stop()
            

if "__main__" == __name__:

    main()

