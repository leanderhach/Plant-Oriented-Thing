import explorerhat as ex
from time import sleep
from lights import set_led, median
import file

value = 0

def get_humidity():
    return (ex.analog.two.read() / 3)

def sensors_main():
    global value
    value = ex.analog.two.read() / 3
    sleep(0.5)
    if (value <= 0.2):
        set_led(brightness=1, color=file.read_env_data("led_warning_color"))
    else:
        set_led(brightness= median(), color=file.read_env_data("led_grow_color"))
