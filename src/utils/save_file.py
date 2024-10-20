import json
from collections import deque

# def save_weather_data_json(weather_dict, filename=r"D:\weatherapp\server\src\insight_files\weather_data.json"):

#     serializable_dict = {
#         city: {
#             key: list(value) if isinstance(value, deque) else value
#             for key, value in city_data.items()
#         }
#         if isinstance(city_data, dict) else list(city_data) if isinstance(city_data, deque) 
#         else city_data 
#         for city, city_data in weather_dict.items()
#         if city_data is not None 
#     }
#     with open(filename, "w") as file:
#         json.dump(serializable_dict, file, indent=4)
#     print(f"Weather data saved to {filename}.")

import os
import json
from collections import deque

def save_weather_data_json(weather_dict, filename=None):

    current_file_path = os.path.dirname(__file__)

    if filename is None:
        filename = os.path.join(current_file_path, '..', 'insight_files', 'weather_data.json')
    
    # Normalize the path
    filename = os.path.normpath(filename)
    
    # Prepare the serializable dictionary
    serializable_dict = {
        city: {
            key: list(value) if isinstance(value, deque) else value
            for key, value in city_data.items()
        }
        if isinstance(city_data, dict) else list(city_data) if isinstance(city_data, deque)
        else city_data 
        for city, city_data in weather_dict.items()
        if city_data is not None
    }
    
    # Save the dictionary as JSON
    with open(filename, "w") as file:
        json.dump(serializable_dict, file, indent=4)
    
    print(f"Weather data saved to {filename}.")

