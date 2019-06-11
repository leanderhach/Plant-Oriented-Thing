import explorerhat as ex
import file
from time import sleep

dictionary = read_env_data("plant_data")

def start(seconds):
    ex.motor.one.forward(90)
    sleep(seconds)
    ex.motor.one.stop()

def stop():
    ex.motor.one.stop()


def motor_main():
    value = (ex.analog.one.read()/5)
    list_insert(value)
    print("\nSENSOR  ", median(), "\n")
    set_led(brightness=median())