from flask import jsonify
from datetime import datetime
from src.summary_generator.summary import generate_weather_summary

def get_temperature_charts(data):
    line_chart_data = {}
    
    for city, city_data in data.items():
        if city not in ['call_time', 'minimum_temp', 'max_temp', 'avg_temp', 'feels_like', 'condition', 'wind_speed']:
            # Convert call_time to datetime if it's in string format
            city_data['call_time'] = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') for t in city_data['call_time']]
            line_chart_data[city] = {
                "data": [
                    {"call_time": city_data['call_time'][i], "avg_temp": city_data['avg_temp'][i]} 
                    for i in range(len(city_data['call_time']))
                ]
            }

    # Prepare bar chart data (Average temperature for each city)
    bar_chart_data = {
        "categories": [],
        "series": []
    }
    
    for city, city_data in data.items():
        if city not in ['call_time', 'minimum_temp', 'max_temp', 'avg_temp', 'feels_like', 'condition', 'wind_speed']:
            bar_chart_data['categories'].append(city)
            bar_chart_data['series'].append({
                "name": city,
                "data": [sum(city_data['avg_temp']) / len(city_data['avg_temp'])]
            })
    
    return {
        "line_chart": line_chart_data,
        "bar_chart": bar_chart_data
    }



def get_charts_for_all(summary_type, weather_dict):

    line_chart_data = {}
    
    for city, city_data in weather_dict.items():
        city_data['call_time'] = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') for t in city_data['call_time']]
        line_chart_data[city] = {
            "data": [
                {"call_time": city_data['call_time'][i], "avg_temp": city_data['avg_temp'][i]} 
                for i in range(len(city_data['call_time']))
            ]
        }

    bar_chart_data = {
        "categories": [],
        "series": []
    }
    
    for city, city_data in weather_dict.items():
        avg_temp = sum(city_data['avg_temp']) / len(city_data['avg_temp'])
        bar_chart_data['categories'].append(city)
        bar_chart_data['series'].append({
            "name": city,
            "data": [avg_temp]
        })

    summary = {}
    all_temps = []
    
    for city, city_data in weather_dict.items():
        all_temps.extend(city_data['avg_temp'])
    
    summary['overall_avg_temp'] = sum(all_temps) / len(all_temps) if all_temps else 0
    summary['max_temp'] = max(all_temps) if all_temps else None
    summary['min_temp'] = min(all_temps) if all_temps else None
    summary['total_cities'] = len(bar_chart_data['categories'])

    summary["summary_text"] = generate_weather_summary(summary, summary_type)

    response = {
        "line_chart": line_chart_data,
        "bar_chart": bar_chart_data,
        "summary": summary
    }

    return response

def get_charts_for_one(summary_type, weather_dict):

        city_data = weather_dict[summary_type]
        city_data['call_time'] = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') for t in city_data['call_time']]
        
        line_chart_data = {
            "data": [
                {"call_time": city_data['call_time'][i], "avg_temp": city_data['avg_temp'][i]} 
                for i in range(len(city_data['call_time']))
            ]
        }


        bar_chart_data = {
            "categories": [],
            "series": []
        }

        for city, city_data in weather_dict.items():
            avg_temp = sum(city_data['avg_temp']) / len(city_data['avg_temp'])
            bar_chart_data['categories'].append(city)
            bar_chart_data['series'].append({
                "name": city,
                "data": [avg_temp]
            })


        summary = {
            'overall_avg_temp': avg_temp,
            'max_temp': max(city_data['avg_temp']),
            'min_temp': min(city_data['avg_temp']),
            'total_cities': 1
        }
        summary["summary_text"] = generate_weather_summary(summary, summary_type)

        response = {
            "line_chart": line_chart_data,
            "bar_chart": bar_chart_data,
            "summary": summary
        }
        print(response)

        return response

