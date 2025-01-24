from dotenv import load_dotenv
import os
import requests

# load .env file
load_dotenv()

# get apikeys
weather_apikey = os.getenv("WEATHER_APIKEY")

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
        weather = data['weather'][0]['main'] # if you return "data", will see that weather is a list that stores arrays --> cnt just weather = data['weather']['main'] bc must rmb that theres an ARRAY in the list
        temp = data['main']['temp']
        # return data 
        return {"weather" : weather, "temperature": temp}
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

location = "Singapore"  # replace with desired location
weather_data = get_weather_data(location, weather_apikey)
print(weather_data)