import time
import json
from weather_api import get_weather_data, normalize_weather_description
from congestion_api import get_lat_lon, get_congestion_data, parse_congestion_data
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

weather_apikey = os.getenv("WEATHER_APIKEY")
congestion_apikey = os.getenv("CONGESTION_APIKEY")

# to categorize time of day
def get_time_period(current_time):
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"

def collect_data(location):

    current_time = datetime.now()
     # Categorize the time of day
    time_period = get_time_period(current_time)

    # get weather data
    weather_data = get_weather_data(location, weather_apikey)
    if not weather_data:
        print("Failed to retrieve weather data.")
        return None
    
     # normalize the weather description using the new function
    weather_data["weather"] = normalize_weather_description(weather_data["weather"])
    
    # get latitude and longitude for congestion data
    lat_lon = get_lat_lon(location, congestion_apikey)
    if not lat_lon:
        print("Failed to retrieve location data.")
        return None
    lat, lon = lat_lon

    # get congestion data
    current_congestion = get_congestion_data(congestion_apikey, lat, lon)
    if not current_congestion:
        print("Failed to retrieve congestion data.")
        return None
    
    congestion_level = parse_congestion_data(current_congestion)

    # then, return collected data
    return {
        "time_period": time_period,
        "weather": weather_data["weather"],
        "congestion_level": congestion_level
    }

def save_data(data, filename="collected_data.json"):
    try:
        # load existing data if any
        if os.path.exists(filename):
            with open(filename, "r") as file:
                # read the current data and parse it
                existing_data = json.load(file)
        else:
            existing_data = []

        # append new data
        existing_data.append(data)

        # then save all the data back to the file
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)  # adding indent for better readability
    except Exception as e:
        print(f"Error saving data: {e}")


def main():
    location = "Singapore"  
    start_time = datetime.now()  # Record the start time
    end_time = start_time + timedelta(hours=15) # will collect data for 15 hours (7am to 10pm) due to lack of time

    while datetime.now() < end_time:  # Loop runs for __  minutes
        # call out collection of data for it to occur
        data = collect_data(location)
        if data:
            print(f"Data collected: {data}")
            save_data(data)

        # wait for 30 minutes before collecting data again
        time.sleep(1800)  # Collect data every 30 minutes (is in seconds so eg 120s=2min)

    print("Data collection completed. You can now check the collected data.")

# run the program
if __name__ == "__main__":
    main()