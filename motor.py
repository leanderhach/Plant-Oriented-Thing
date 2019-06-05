import explorerhat as ex
from time import sleep

def start(seconds):
    ex.motor.one.forward(90)
    sleep(seconds)
    ex.motor.one.stop()

def stop():
    ex.motor.one.stop()