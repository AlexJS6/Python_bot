from threading import Thread
import time

def playing():
    for i in range(5, -1, -1):
        if i == 0:
            print('GOGOGO')
            print(time.time()+10)
            break
        else:
            print(i)
        time.sleep(1)
        print(time.time())

playing()
