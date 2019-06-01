"""
Methods for fetching and setting data regarding plant attributes
"""

import urllib.request, json 


def get_plant_needs(id):
    with urllib.request.urlopen("http://trefle.io/api/plants/{}?token=QjFTVmRBKzk2TEh1MVpDa3BFZHJhUT09".format(id)) as url:
        data = json.loads(url.read().decode())
        
        return(data['main_species']['growth'])
