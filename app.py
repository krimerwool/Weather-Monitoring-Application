

from flask import Flask, jsonify, request, send_from_directory, render_template
from src.utils.load_func import load_insight_file, load_weather
from src.utils.configs import longitude_and_latitude
from src.utils.save_file import save_weather_data_json
from src.utils.aggregation import calculate_mean_avg_temp, update_weather_data
from src.summary_generator.summary import generate_weather_summary
from src.logics.get_chart import get_charts_for_all, get_charts_for_one
from flask_cors import CORS
from datetime import datetime, timedelta
from collections import deque
import os
import requests

app = Flask(__name__, static_folder='../static', template_folder='../templates')
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Load initial weather data
set_thresholds = 10
city_weather = load_weather()
weather_dict = update_weather_data(city_weather, set_thresholds)

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/daily-summary', methods=['GET'])
def provide_data():
    print("this is being called")
    
    global weather_dict, city_weather
    city_weather = load_weather()
    weather_dict = update_weather_data(city_weather, set_thresholds)
    
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

    
    return jsonify(serializable_dict), 200
@app.route("/get_temp_charts", methods=["GET"])
def get_temp_charts():
    print("we're in temp_charts")
    city = request.args.get("city")
    print(city)
    if city == "all":
        response = get_charts_for_all(city, weather_dict)
        return jsonify(response), 200
    elif city in weather_dict:
        print("we're")
        response = get_charts_for_one(city, weather_dict)
        print(response,"this is the response")
        return jsonify(response), 200
    return jsonify({'invalid': 'the type selected is invalid yess'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



