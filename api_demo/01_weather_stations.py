# pip3 install haversine
from requests import get
from pprint import pprint
from haversine import haversine

url = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations"

weatherStations = get(url).json()["items"]
#print(weatherStations)

latitude = -37.815018  # Melbourne latitude - hardcoded as no GPS plugged into Pi.
longitude = 144.946014 # Melbourne longitude - hardcoded as no GPS plugged into Pi.
location = (latitude, longitude)

def getLocation(weatherStation):
    return (weatherStation["weather_stn_lat"], weatherStation["weather_stn_long"])

def findNearestWeatherStationID(weatherStations, location):
    if(not weatherStations):
        return None

    id = weatherStations[0]["weather_stn_id"]
    distance = haversine(location, getLocation(weatherStations[0]))
    
    for weatherStation in weatherStations:
        currentDistance = haversine(location, getLocation(weatherStation))
        if(currentDistance < distance):
            id = weatherStation["weather_stn_id"]
            distance = currentDistance

    return id

weatherStationID = findNearestWeatherStationID(weatherStations, location)

print("Next call.")

url = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/{}".format(weatherStationID)

weatherStation = get(url).json()["items"]
print(weatherStation)
