from travelerApp import db, owm
from flask import session
import googlemaps


def GeoCode(address: str) -> dict:
    '''
    Returns a dictionary containing latitude and longitude for the supplied address.

    address is a any string parsible by the Google Maps API as an address, from simply a ZIP Code to a fully qualified address.

    The keys in the returned dictionary are 'lat' & 'lng'.
    '''

    gmaps = googlemaps.Client(key=session['gm_key'])
    geocode_result = gmaps.geocode(address)
    latLngDict = geocode_result[0]['geometry']['location']
    
    return latLngDict


