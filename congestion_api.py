# * diff apis = diff url formats = diff names for the "params"'s key eg "apiKey" in HERE API, but "apikey" in WEATHER API

from dotenv import load_dotenv
import os
import requests
import xml.etree.ElementTree as ET

# load .env file
load_dotenv()

# get apikeys
congestion_apikey = os.getenv("CONGESTION_APIKEY")

# get latitude & longitude for the location user input (since HERE API deals with lat & lon)
def get_lat_lon(location, api_key):
    url = f"https://api.tomtom.com/search/2/geocode/{location}.json" # must put the 'f' in front so that the location goes inside the url link, without the 'f' --> "{location}" will be treated as tho it is literally part of the url...
    params = {
        "key": api_key # dont nd declare location in params bc it is alr in url
    }

    # send req to geocode api
    response = requests.get(url, params=params)

    # check if req successful
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            lat = data['results'][0]['position']['lat']
            lon = data['results'][0]['position']['lon']
            return lat, lon
        else:
            print(f"No results found for {location}")
            return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# congestion api to get data
def get_congestion_data(api_key, lat, lon):
    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml"
    params = {
        "key": api_key,         
        "point": f"{lat},{lon}"
    }

    # print("Request URL:", requests.Request("GET", url, params=params).prepare().url) # debug

    # send api req
    response = requests.get(url, params=params)

    # check if req successful
    if response.status_code == 200:
        data = response.text # stores data in xml format, thus is not "data = response.json"
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
# function to determine the congestion levels (low, med, high) )
def get_congestion_level(current_speed, free_flow_speed, road_closure):
    speed_ratio = current_speed / free_flow_speed 
    
    if road_closure:
        if speed_ratio > 0.8: # bc road close, more vehicles
            return "Medium" 
        else:
            return "High"
        
    else:
        if speed_ratio > 0.8:
            return "Low"
        elif 0.5 <= speed_ratio <= 0.8:
            return "Medium"
        else:
            return "High"


# function to get specific data to pass into the above function which will then dtermine congestion levels
# --- bc tomtom api do not directly say congestion level, have to use the data they have & infer yourself
def parse_congestion_data(xml_data):
    root = ET.fromstring(xml_data)

    road_closure = root.find('.//roadClosure').text.lower == "true"
    current_speed = float(root.find('.//currentSpeed').text)
    free_flow_speed = float(root.find('.//freeFlowSpeed').text) # == the ideal speed vehicles shld travel at to prevent congestion

    if road_closure:
        return "Road Closed" # print this as a warning to drivers eg just let them know that have road closure, thus congestion might == medium/high altho vehicles travelling at an ideal pace aka > 0.8
    
    congestion_level = get_congestion_level(current_speed, free_flow_speed, road_closure)
    return congestion_level
    
    
def main():
    location = input("Enter location: ")
    lat_lon = get_lat_lon(location, congestion_apikey)
    
    if lat_lon:
        lat, lon = lat_lon
        print(f"Latitude: {lat}, Longitude: {lon}")
        current_congestion = get_congestion_data(congestion_apikey, lat, lon)
        if current_congestion:
            congestion_level = parse_congestion_data(current_congestion)
            print(f"Current Congestion Level: {congestion_level}")
        else:
            print("Could not retrieve congestion data.")
        
    else:
        print("Unable to find location.")

# Run the program
if __name__ == "__main__":
    main()

