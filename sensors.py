import explorerhat as ex
from time import sleep
from lights import set_led, median
import file
import datetime
import os
from motor import motor_main
import api

value = 0
needs_water = False
def get_needs_water():
    return needs_water

def get_humidity():
    return (ex.analog.two.read() / 3)

def sensors_main():

    print("checking water")
    global value
    global needs_water
    value = ex.analog.two.read() / 3
    sleep(0.5)

    if(file.read_env_data("debug_needs_water")):
        with open("dayCheck.txt", "w") as f:
            f.write("2000-06-18-16:47")
            f.close()

    if file.read_env_data('pump_status'):
       motor_main()
       api.update_pump_status(False)
       
        

    with open('dayCheck.txt', 'r+') as f:
    
        print("insufficient water")
                
        lines = f.read().splitlines()
                
    
        if ((len(lines) > 0 and datetime.datetime.now() - datetime.datetime.strptime(lines[len(lines) - 1], "%Y-%m-%d-%H:%M") >= datetime.timedelta(days=3) or (len(lines) == 0)) or (value <= 0.2)): # if 3 days had passed it changes the leds color
            needs_water = True
            set_led(brightness=1, color=file.read_env_data("led_warning_color"))

        else:

            print("plant was recently watered. continuing")
            needs_water = False
            set_led(brightness= median(), color=file.read_env_data("led_grow_color"))

        f.close()

