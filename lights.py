import neopixel
import board
import file
import explorerhat as ex
from time import sleep

light_levels = []
led = 0
value = 0
def setup_lights():
    global led
    global light_levels
    led = neopixel.NeoPixel(board.D18, 30, auto_write=True, brightness=0)
    for i in range(5):
        light_levels.append(0)

def list_insert(lightvalue):
    global light_levels
    light_levels.append(lightvalue)
    light_levels.pop(0)
    
def median():
    global light_levels
    total = 0
    for value in light_levels:
        total += value
    return total/len(light_levels)

def set_led(**kwargs):
    global led
    for key, value in kwargs.items():
        if key == "color":
            led.fill(value)
        if key == "brightness":
            led.brightness = value
            
def get_light_level():
    return value

def get_light_intensity():
    return led.brightness

def lights_main():
    global value
    value = (ex.analog.one.read()/5)
    list_insert(value)
    print("\nSENSOR  ", median(), "\n")
    set_led(brightness=median(), color=file.read_env_data("led_grow_color"))
