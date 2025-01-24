# * diff apis = diff url formats = diff names for the "params"'s key eg "apiKey" in HERE API, but "apikey" in WEATHER API

from dotenv import load_dotenv
import os
import requests

# load .env file
load_dotenv()

# get apikeys
congestion_apikey = os.getenv("CONGESTION_APIKEY")

# get latitude & longitude for the location user input (since HERE API deals with lat & lon)
def get_lat_lon(location, api_key):
    url = "https://geocode.search.hereapi.com/v1/geocode"
    params = {
        "q": location, # "q" bc that is the param HERE API expects
        "apiKey": api_key 
    }

    # send req to geocode api
    response = requests.get(url, params=params)

    # check if req successful
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            lat = data['items'][0]['position']['lat']
            lon = data['items'][0]['position']['lng']
            return lat, lon
        else:
            print(f"No results found for {location}")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# congestion api
def get_congestion_data(api_key, lat, lon):
    url = "https://traffic.api.here.com/traffic/6.3/incidents.json" 
    params = {
        "apiKey": api_key,         
        "prox": f"{lat},{lon},5000",  # 5000 = 5km. eg User input effiel tower, i will extract data regarding traffic congestion for within 5km of the effiel tower
        "responseattributes": "severity"  # to get severity of traffic incidents/disruptons eg Constructions, road closures
    }

    # send api req
    response = requests.get(url, params=params)

    # check if req successful
    if response.status_code == 200:
        data = response.json()
        incidents = data.get('incidents', [])
        
        # analyze how severe the incidents are --> then can get traffic congestion
        if incidents: 
            severity = incidents[0].get('severity',0) # if severity key not inside, then return 0
            if severity == 1:
                return "Low"
            elif severity == 2:
                return "Medium"
            elif severity == 3:
                return "High"
        else:
            return "Low" # since no incidents found
    else:
        print(f"HELLO Error: {response.status_code}")
        return None
    
    
def main():
    location = input("Enter location: ")
    lat, lon = get_lat_lon(location, congestion_apikey)
    
    if lat and lon:
        print(f"Latitude: {lat}, Longitude: {lon}")
        current_congestion = get_congestion_data(congestion_apikey, lat, lon)
        print(f"Current Congestion Level: {current_congestion}")
        
    else:
        print("Unable to find location.")

# Run the program
if __name__ == "__main__":
    main()

