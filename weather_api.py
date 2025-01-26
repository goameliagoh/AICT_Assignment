from dotenv import load_dotenv
import os
import requests

# load .env file
load_dotenv()

# get apikeys
weather_apikey = os.getenv("WEATHER_APIKEY")

# normalize weather names that openweather api might return
def normalize_weather_description(description):
    mapping = {
        "Clouds": "Clouds",
        "Rain": "Rain",
        "Clear": "Clear",
        "Snow": "Snow",
        "Drizzle": "Drizzle",
        "Thunderstorm": "Thunderstorm",
    }
    return mapping.get(description, description)  # Default to the same description if no mapping found


# weather api
def get_weather_data(location, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,         
        "apikey": api_key, 
        "units": "metric"  # "metric" for Celsius
    }

    # send api req
    response = requests.get(url, params=params)

    # check if req successful
    if response.status_code == 200:
        data = response.json()
        weather = normalize_weather_description(data['weather'][0]['main'])  # to normalize description for data collection 
        # weather = data['weather'][0]['main'] # if you return "data", will see that weather is a list that stores arrays --> cnt just weather = data['weather']['main'] bc must rmb that theres an ARRAY in the list
        # return data 
        return {"weather" : weather}
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

location = "Singapore"  # replace with desired location
weather_data = get_weather_data(location, weather_apikey)
print(weather_data)