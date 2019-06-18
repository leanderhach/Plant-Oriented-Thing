import explorerhat as ex
from time import sleep
from lights import set_led, median
import file
import datetime
import os

value = 0
needs_water = False

def get_needs_water():
    return needs_water

def get_humidity():
    return (ex.analog.two.read() / 3)

def sensors_main():
    global value
    global needs_water
    value = ex.analog.two.read() / 3
    sleep(0.5)

        
    if (value <= 0.2):
        with open('dayCheck.txt', 'r+') as f:
            
            lines = f.read().splitlines()
            last_line = lines[-1]

            if((datetime.datetime.now - last_line) >= 3): # if 3 days had passed it changes the leds color
                needs_water = True
                set_led(brightness=1, color=file.read_env_data("led_warning_color"))    

            f.close()

    else:
        needs_water = False
        set_led(brightness= median(), color=file.read_env_data("led_grow_color"))
        os.remove("myfile.txt") #deletes the file previously created if the plant has been watered.
        f.write(datetime.datetime.now) # write that the plant was watered

