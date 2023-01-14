import pyautogui as pg
from time import sleep

print('Press Ctrl-C to quit.')
try:
    while True:
        pg.moveTo(1365, 767, 3.0)
        sleep(5)
        pg.moveTo(1365, 700, 3.0)
        sleep(3)
except KeyboardInterrupt:
    print('\n')