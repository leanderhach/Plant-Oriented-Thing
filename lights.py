import gpiozero
from signal import pause

led = RGBLED(2, 3, 4)
sensor = LightSensor(18)

led.color = (1, 1, 0)

led = PWMLED(16)

led.source = sensor


pause()
