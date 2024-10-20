
import os
import google.generativeai as genai
def generate_weather_summary(summary, city):
    try:
        api_key = os.getenv("API_KEY", "")

        if not api_key:
            return "No API key found. Please set the API_KEY environment variable."

        genai.configure(api_key=api_key)

        # Initialize the model and generate content
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        text = f"You are a weather reporter generate summary in more than 100 words. consider the date provided to you for the city {city}. {city} has this current temprature report well  "
        response = model.generate_content(f"{summary} \n generate summary of above weather\n\n\n {text}")

        if response.candidates:
            content = response.candidates[0].content.parts[0].text
            return content
            print(content)
        else:
            return "PUT AN API KEY TO GENERATE CONTENT"
    except e:
        return f'{e} has been encountered'
