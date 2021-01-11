#Eric Chou 95408627
#PROJECT 3: Ride Across the River
#mapquest.py
import json
import urllib.parse
import urllib.request

API_KEY = 'iA97npZzYByGoYRoS77wuLxertjTJmC9'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/'

def build_route_url(locations:list) -> str:
    #Creates the url for mapquest route api
    route_parameters = [
        ('key', API_KEY), ('from', locations[0])]
    for i in range(1, len(locations)):
        route_parameters.append(('to', locations[i]))

    return BASE_MAPQUEST_URL + '?' + urllib.parse.urlencode(route_parameters)

def build_elevation_url(lat_long: str)-> str:
    #Creates the url for the elevation route api
    elevation_parameters = [
        ('key', API_KEY), ('latLngCollection', lat_long)
    ]
    return BASE_ELEVATION_URL + 'profile?'+ urllib.parse.urlencode(elevation_parameters)

def get_result(url: str) -> dict:
    #Takes the url and creates the dict
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)
    finally:
        if response != None:
            response.close()

