import explorerhat as ex
import file
from time import sleep


def start(seconds):
    dictionary = read_env_data("plant_data")
    min = dictionary['min_water']
    max = dictionary['max_water']
    waterAmount = ((min+max)/2)/365 #amount per day
    waterAmount = waterAmount*3 #concentrated every 3 days (verify watering frequence for our specific plant)
    ex.motor.one.forward(90)
    sleep(seconds) #change number of seconds once we figure out ml/s pumped
    ex.motor.one.stop()

def stop():
    ex.motor.one.stop()


def motor_main():
    value = (ex.analog.one.read()/5)
    list_insert(value)
    print("\nSENSOR  ", median(), "\n")
    set_led(brightness=median())
