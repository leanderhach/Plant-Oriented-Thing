from time import sleep

from api import setup_db_access, api_main
from repeating_thread import RepeatingThread
from sensors import sensors_main


"""Main loop

    main.py is responsible for starting every _main() function in each of the other python files.
    It does this by creating a new instace of the RepeatingThread class for each _main(),

"""

#TODO:
# - add light function call
# - add camera function call
# - add ability to shut down program greacefully
#####################################################

## access database and start loop
setup_db_access()
RepeatingThread(5, api_main)
RepeatingThread(5, sensors_main)