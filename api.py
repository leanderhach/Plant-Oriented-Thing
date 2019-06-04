"""Controls API functions

        Functions
        - get_plant_needs
        - setup_db_access
        - update_data
        - save_current_conditions
        - on_snapshot
"""

import urllib.request, json, sensors, lights
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.oauth2 import service_account

# Global DB client variable
db = ""


"""Fetches plant needs from trefle API

        Params
        id - the exact ID of the plant

        Return
        A tuple containing growing requirements for the plant
"""
def get_plant_needs(id):
    with urllib.request.urlopen("http://trefle.io/api/plants/{}?token=QjFTVmRBKzk2TEh1MVpDa3BFZHJhUT09".format(id)) as url:
        data = json.loads(url.read().decode())
        
        return(data['main_species']['growth'])


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

        
        dataset = db.collection(u'env_data').document(u'dataset')

        try:
                doc = doc_ref.get()
                print(u'Document data: {}'.format(doc.to_dict()))
        except Exception:
                print(u'No such document!')

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
        dataset_listener = dataset.on_snapshot(on_snapshot)


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

        humidity = sensors.get_humidity()
        led_intensity = lights.get_led_intensity()
        light_level = sensors.get_light_level()
        dataset = db.collection(u'pot_data').document(u'dataset')


        dataset.update({
                u'humidity': humidity,
                u'led_intensity': led_intensity,
                u'light_level': light_level
                })



"""helper function for live db updates

   Params
   None

   Return
   None
"""
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(u'Received document snapshot: {}'.format(doc.id))




# test loop
setup_db_access()
update_data()