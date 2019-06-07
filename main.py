from time import sleep

from api import setup_db_access, api_main
from repeating_thread import RepeatingThread
from sensors import sensors_main
#MAIN LOOP

#TODO:
# - add light function call
# - add sensor function call
# - add camera function call
# - add call for speakers based on camera call return
#####################################################

## access database and start loop
setup_db_access()
RepeatingThread(5, api_main)
RepeatingThread(5, sensors_main)

## start sensors
# sensors_main()


# sleep for a second, then repeat program