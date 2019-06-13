import explorerhat as ex
from time import sleep
from lights import set_led, median
import file
import datetime
import os

value = 0

def get_humidity():
    return (ex.analog.two.read() / 3)

def sensors_main():
    global value
    value = ex.analog.two.read() / 3
    sleep(0.5)
    now = datetime.datetime.now()

        
    if (value <= 0.2):
        if (!f.exists):
            f = open("myfile.txt", "a") #creates myfile.txt
            f.write(now.day) #writes which day is today
        fileHandle = open ( 'myfile.txt',"r" ) #opens the file previously created
            line = fileHandle.readlines() #reads the lines
            fileHandle.close()
            if((now.day-line) == 3): # if 3 days had passed it changes the leds color
                set_led(brightness=1, color=file.read_env_data("led_warning_color"))    

    else:
        set_led(brightness= median(), color=file.read_env_data("led_grow_color"))
        os.remove("myfile.txt") #deletes the file previously created if the plant has been watered.

