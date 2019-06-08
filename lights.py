import neopixel
import explorerhat as ex
from time import sleep

light_levels = []
led = 0

def setup_lights():
    global led
    global light_levels
    led = neopixel.NeoPixel(board.D12, 30, auto_write=True, brightnes=0)
    led.fill((223, 147, 189))
    for i in range(20):
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

def lights_main():
    value = (ex.analog.one.read()/5)
    list_insert(value)
    print("\nSENSOR  ", median(), "\n")
    set_led(brightness=median())
    
