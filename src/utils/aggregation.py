import datetime
from collections import deque
from src.utils.load_func import load_weather, load_weather_data_json
from src.utils.save_file import save_weather_data_json
from datetime import datetime


weather_dict = load_weather_data_json()
city_weather = load_weather()


def update_weather_data(city_weather , thresholds):
    weather_dict = load_weather_data_json()
    print(weather_dict)
    """Update the weather_dict based on the `city_weather` data from multiple cities."""
    
    for city, weather_info in city_weather.items():
        
        
        # Initialize city's weather data if it does not  exist
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
        
        # Update the weather data for the city
        call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp_min = weather_info['temprature_minimum_celcius']
        temp_max = weather_info['temprature_maximum_celcius']
        temp_avg = (temp_min + temp_max) / 2
        feels_like = weather_info['feels_like_celcius']
        condition = weather_info['condition']
        wind_speed = weather_info.get('wind_speed', None)  # Add wind speed if available

        weather_dict[city]["call_time"].append(call_time)
        weather_dict[city]["minimum_temp"].append(temp_min)
        weather_dict[city]["max_temp"].append(temp_max)
        weather_dict[city]["avg_temp"].append(temp_avg)
        weather_dict[city]["feels_like"].append(feels_like)
        weather_dict[city]["condition"].append(condition)
        weather_dict[city]["wind_speed"].append(wind_speed)
        if(weather_dict[city]["avg_temp"][-1] >= thresholds):
            weather_dict[city]["alert"].append(True)
        else:
            weather_dict[city]["alert"].append(False)
            


        calculate_mean_avg_temp(city)
        save_weather_data_json(weather_dict)

    return weather_dict

def calculate_mean_avg_temp(city):
    print(len(weather_dict[city]["avg_temp"]), "this is len")
    """Calculate the overall average temperature for a specific city from the average temps."""
    if len(weather_dict[city]["avg_temp"]) > 0:
        overall_avg = sum(weather_dict[city]["avg_temp"]) / len(weather_dict[city]["avg_temp"])
        weather_dict[city]["overall_average_temp"] = overall_avg
    else:
        weather_dict[city]["overall_average_temp"] = None











