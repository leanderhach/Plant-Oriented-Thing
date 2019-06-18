import explorerhat as ex
import file
from time import sleep
from api import update_pump_status

def start():
    data = read_env_data("plant_data")
    min = data['min_water']
    max = data['max_water']
    waterAmount = ((min+max)/2)/365 #amount per day
    waterAmount = waterAmount*3 #concentrated every 3 days (verify watering frequence for our specific plant)


    flowRate = 13

    timeInOperation = waterAmount / flowRate

    
    ex.motor.one.forward(90)
    sleep(timeInOperation) #change number of seconds once we figure out ml/s pumped
    ex.motor.one.stop()

def stop():
    ex.motor.one.stop()


def motor_main():
    if read_env_data("pump_status") == True:
        update_pump_status(False)
        start()
    else:
        #do nothing
