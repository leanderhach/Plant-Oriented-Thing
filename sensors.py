import explorerhat as ex
from time import sleep

def get_humidity():
    return (ex.analog.two.read() / 3)

def sensors_main():
    print(ex.analog.two.read())