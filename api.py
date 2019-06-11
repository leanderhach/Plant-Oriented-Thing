"""Controls API functions

        Functions
        - get_plant_needs
        - setup_db_access
        - update_data
        - save_current_conditions
"""

import urllib.request, json, threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.oauth2 import service_account
from time import sleep
from file import write_env_data
from lights import get_light_level, get_light_intensity
from sensors import get_humidity

# Global DB client variable
db = ""


"""Sets data about the plant

        due to access restrictions on trefle, this method must be used to set data about the plant inside the datbse, 
        which can then be accessed by the app
        
        Params
        data - the full response dict from trefle.io (see get_plant_needs)
        
        Return
        None

"""
def set_plant_data(data):
       dataset = db.collection(u'plant_data').document(u'dataset')


        dataset.update({
                u'name': data['common_name'],
                u'scientific_name': data['scientific_name'],
                u'image': data['images'][0]['url'],
                u'growth_period':data['main_species']['specifications']['growth_period']
                })
        
"""Fetches plant needs from trefle API

        Params
        id - the exact ID of the plant

        Return
        A tuple containing growing requirements for the plant
"""
def get_plant_needs(id):

        print('getting plant {}'.format(id))
        with urllib.request.urlopen("http://trefle.io/api/plants/{}?token=QjFTVmRBKzk2TEh1MVpDa3BFZHJhUT09".format(id)) as url:
                data = json.loads(url.read().decode())
                
        set_plant_data(data)

        return {
                'min_water': data['main_species']['growth']['precipitation_minimum']['cm'], 
                'max_water': data['main_species']['growth']['precipitation_maximum']['cm'],
                'shade': data['main_species']['growth']['shade_tolerance']
                }


"""Sets up the connection to Google firestore

   This function will initiate the connection to google firestore
   as well as fetch the 'env_data' dataset to get the POT's initial
   operating parameters

        Params
        None

        Return
        None
"""
def setup_db_access():

        global db

        cred = credentials.Certificate('P-O-T-bb82fc334a56.json')
        firebase_admin.initialize_app(cred, {
        'projectId': 'p-o-t-242713',
        })

        db = firestore.client()

"""Updates pot operating data

   This function creates a listener that will fetch updates to the 'env_data' dataset when it is 
   changed

   Params
   None

   Return 
   None
"""
def update_data():

        dataset = db.collection(u'env_data').document(u'dataset')

        try:
                doc = (dataset.get()).to_dict()
                
                doc['plant_data'] = get_plant_needs(doc['current_plant'])

                write_env_data(doc)



        except Exception:
                print(u'No such document!')

"""Updates firestore data 

   This function will update the google firestore 'pot_data' dataset which
   contains all readngs from the pot, such as humidity and light levels, 
   which can be read by an external user

   Params
   None

   Return
   None
"""
def save_current_conditions():
        print('updating')

        humidity = get_humidity()
        led_intensity = get_led_intensity()
        light_level = get_light_level()
        dataset = db.collection(u'pot_data').document(u'dataset')


        dataset.update({
                u'humidity': humidity,
                u'led_intensity': led_intensity,
                u'light_level': light_level
                })


# main api loop
def api_main():

        print('calling api')

        #run api calls
        update_data()
        save_current_conditions()
