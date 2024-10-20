import os
import json
from src.utils.configs import INSIGTH_JSON_FOLDER, longitude_and_latitude, WEATHER_DICT
import datetime
from datetime import datetime
from collections import deque


import requests
def load_insight_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), '..', INSIGTH_JSON_FOLDER, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            print(f)
            return json.load(f)
    else:
        return {}
    

CITIES = load_insight_file(longitude_and_latitude)
    
def load_weather():
    city_weather = {}
    CITIES = load_insight_file(longitude_and_latitude)

    for city, coords in CITIES['CITIES'].items():

        lat, lon = coords['lat'], coords['lon']
        part = None

        API_KEY = os.getenv("277b9039efcd0c0918f9a7a965bb132c", "mananb")

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=277b9039efcd0c0918f9a7a965bb132c&units=metric"

        response = requests.get(url)
        data = response.json()



        
        if 'main' in data:
            temp_kelvin = data['main']['temp'] + 273.15  # Convert from Kelvin to Celsius
            temp_celcius = data['main']['temp']
            temp_min_kelvin = data['main']['temp_min'] +273.15
            temp_min_celcius = data['main']['temp_min'] 
            temp_max_kelvin = data['main']['temp_max'] +273.15
            temp_max_celcius = data['main']['temp_max'] 
            feels_like = data['main']['feels_like'] 
            condition = data['weather'][0]['main']
            city_weather[city] = {
                'temprature_minimum_kelvin':round(temp_min_kelvin, 2),
                'temprature_minimum_celcius': round(temp_min_celcius , 2),
                'temprature_maximum_celcius':round(temp_max_celcius, 2),
                'temprature_maximum_kelvin': round(temp_max_kelvin, 2),
                'temprature_kelvin': round(temp_kelvin, 2),
                'tempratur_celcius': round(temp_celcius, 2),
                'feels_like_celcius': round(feels_like, 2),
                'condition': condition,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    return city_weather


def load_weather_data_json(filename=WEATHER_DICT, city_weather =load_weather() ):
    """Load the weather_dict from a JSON file."""
    try:

        file_path = os.path.join(os.path.dirname(__file__), '..', INSIGTH_JSON_FOLDER, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                loaded_dict = json.load(f)
                return loaded_dict
        else:
            weather_dict = {}
            for city, weather_info in city_weather.items():

                if city not in weather_dict:
                    weather_dict[city] = {
                        "call_time": deque(maxlen=288),
                        "minimum_temp": deque(maxlen=288),
                        "max_temp": deque(maxlen=288),
                        "avg_temp": deque(maxlen=288),
                        "feels_like": deque(maxlen=288),
                        "condition": deque(maxlen=288),
                        "wind_speed": deque(maxlen=288),
                        "overall_average_temp": None,
                        "alert": deque(maxlen=288)
                    }
                
            print(f"{filename} not found. Initialized new weather_dict.")
            return weather_dict
        
    except FileNotFoundError:
        weather_dict = {}

        for city, weather_info in city_weather.items():

            if city not in weather_dict:
                weather_dict[city] = {
                    "call_time": deque(maxlen=288),
                    "minimum_temp": deque(maxlen=288),
                    "max_temp": deque(maxlen=288),
                    "avg_temp": deque(maxlen=288),
                    "feels_like": deque(maxlen=288),
                    "condition": deque(maxlen=288),
                    "wind_speed": deque(maxlen=288),
                    "overall_average_temp": None,
                    "alert": deque(maxlen=288)
                }
            
        print(f"{filename} not found. Initialized new weather_dict.")
        return weather_dict

