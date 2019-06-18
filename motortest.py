import explorerhat as ex
from time import sleep

ex.motor.one.forward(90)
sleep(15)
ex.motor.one.stop()
