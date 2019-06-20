import explorerhat as ex
from file import read_env_data
from time import sleep
import datetime


def run_motor_cycle():
    try:
        data = read_env_data("plant_data")
        min = data['min_water']
        max = data['max_water']
    except Exception:
        min = 50
        max = 50
    waterAmount = ((min+max)/2)/365 #amount per day
    waterAmount = waterAmount*3 #concentrated every 3 days (verify watering frequence for our specific plant)


    flowRate = 13

    timeInOperation = waterAmount * flowRate

    
    ex.motor.one.forward(90)
    print(timeInOperation)
    sleep(timeInOperation) #change number of seconds once we figure out ml/s pumped
    ex.motor.one.stop()
    print("plant has been watered, logging time")
    with open('dayCheck.txt', 'r+') as f:
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")))
        f.close()

def stop():
    ex.motor.one.stop()


def motor_main():
    run_motor_cycle()
