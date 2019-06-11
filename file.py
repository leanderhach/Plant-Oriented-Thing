"""file.py

    methods for reading and modifying data from data.json

"""

import json


"""Writes environment data to file

    this function saves environment data that is passed to in inside env.json.

    File Structure:
        "led_warning_color": [r, g, b], 
        "current_plant": "id", 
        "led_grow_color": [r, g, b], 
        "pump_status": boolean, 
        "plant_data": {
            "min_water": float, 
            "max_water": float, 
            "shade": float
            }

    Params
    data - a dict

    Return 
    None

"""
def write_env_data(data):
    with open ('env.json', 'w') as outfile:
            json.dump(data, outfile)


"""Reads environment data

    this function will return the value of a specified environment variable

    Params
    key - a string that has the value of valid environment variable key

    Return
    The key's value - may be:
                            - array
                            - boolean
                            - int

""" 
def read_env_data(key):
    with open ('env.json', 'r') as infile:
        data = json.load(infile)

        if type(data[key]) is list:

            print(tuple(data[key]))
            return tuple(data[key])

        else:

            return data[key]
