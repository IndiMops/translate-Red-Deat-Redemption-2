import pyautogui as pg
from time import sleep
import os

import psutil
from pypresence import Presence
import time

client_id = '1054749227860889630'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

    
path = os.path.abspath(__file__)
path = path.replace(f'\{os.path.basename(__file__)}', '')
print(path)

pg.press('winleft')
pg.typewrite('openIV')
pg.press('enter')


pg.moveTo(850, 728, 0.5)
pg.click()
sleep(3)
pg.moveTo(1459, 184, 0.5)# full window
pg.click()
sleep(1)


pg.moveTo(306, 560)# data_0
sleep(1)
pg.click()
sleep(1)
pg.press('enter')
sleep(1)

pg.moveTo(276, 173)
sleep(0.5)
pg.click()# data
sleep(0.5)
pg.press('enter')
sleep(0.5)

pg.click(318, 209)# lang

sleep(0.5)
pg.press('enter')
sleep(1)

pg.click(315, 153)# rus
sleep(1)
pg.press('enter')
sleep(1)


pg.moveTo(357, 175, 0.1)# first file
sleep(1)
pg.click()

sleep(0.5)
pg.press('enter')
sleep(1)

def export_file(iteration: int):
    pg.click(1270, 308)
    sleep(0.5)

    pg.click(1125, 333)
    sleep(0.3)

    pg.click(1180, 350)
    sleep(0.5)

    pg.typewrite(f'{path}\n')
    sleep(0.5)
    

    pg.click(1321, 790
             )
    sleep(0.5)
    pg.hotkey('altleft', 'f4')
    sleep(0.5)
    
    if iteration != 1929:
        pg.press('down')
        sleep(0.1)
        pg.press('enter')
        sleep(0.1)
    else:
        pg.alert(text='Файли успішно експортовані', title='Готово!', button='OK')
        
        
iteration = 1
while iteration < 2319:
    export_file(iteration)
    cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(details="Red Dead Redemtion 2 - Експортує файли", state=f"Стан сервера - Ram: {str(mem_per)}%; CPU: {str(cpu_per)};", start=int(time.time()), large_image="rdr_large", large_text="Red Dead Redemption 2")
    iteration+=1