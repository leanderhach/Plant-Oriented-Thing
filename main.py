
from time import sleep

from api import setup_db_access, api_main
from repeating_thread import RepeatingThread
from file import read_env_data
from sensors import sensors_main
from lights import setup_lights, lights_main
from detection import detection_main


"""Main loop

    main.py is responsible for starting every _main() function in each of the other python files.
    It does this by creating a new instace of the RepeatingThread class for each _main(),

"""

#TODO:
# - add ability to shut down program gracefully
#####################################################

## access database and start loop
setup_db_access()
setup_lights()

main_thread = RepeatingThread(2, api_main)
sensors_thread = RepeatingThread(2, sensors_main)
lights_main = RepeatingThread(2, lights_main)
detection_main = RepeatingThread(2, detection_main)


#### to kill the threads, call .stop()
# main_thread.stop()
# sensors_thread.stop()

