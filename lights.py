import 
import neopixel
import explorerhat as ex
from time import sleep

pixels = neopixel.NeoPixel(board.D12, 30)
pixels.fill((0, 255, 0))

while True:
    print(1 - (ex.analog.one.read() / 5))
    sleep(2)
    
pause()
