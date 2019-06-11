import explorerhat as ex
from time import sleep

#we need to have the motor pump 50cl at a time, still need to figure out seconds to do that

def start(seconds):
    ex.motor.one.forward(90)
    sleep(seconds)
    ex.motor.one.stop()

def stop():
    ex.motor.one.stop()
   
