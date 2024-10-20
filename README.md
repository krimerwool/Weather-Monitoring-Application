# Weather App

## Overview

The Weather App is a feature-rich application that provides users with real-time weather information and historical weather data for various cities . With a sleek and modern user interface, this app allows users to explore weather conditions, set custom thresholds for alerts, and visualize weather trends over time. It is built using HTML, CSS, JavaScript for the front end, and Python for the backend, ensuring a seamless and efficient experience.

## Features

### 1. City Selection
- Users can choose a city from a dynamic dropdown menu populated with a list of available cities.
- The List of cities are Delhi, Mumbai, Bengaluru, Chennai, Kolkata, Hyderabad.
- The app retrieves and displays weather data based on the selected city.

### 2. Current Weather Display
Calls the OpenWeatherAPI to get the real time data for the selected city. The Application calls the API for data every 5 minutes.
- Displays key weather metrics including:
  - **Temperature**: Current, minimum, maximum, and feels-like temperature.
  - **Wind Speed**: Current wind conditions measured in km/h or mph. I could not get the Wind data as it is on the paid version of the API, but it can certainly be integrated later.
  - **Weather Conditions**: Descriptive weather data (e.g., sunny, cloudy) along with a corresponding weather icon.

### 3. Historical Weather Data
- Provides access to past weather conditions, enabling users to compare current weather with historical data.
- The historical data is displayed in a visually engaging format for easy comprehension.

### 4. Graphical Representation
- Users can view graphs representing historical weather trends, such as temperature changes over a specific time period.
- Graphs allow for easy visualization of fluctuations in weather data.

### 5. Bar Chart Representation
- A Bar chart is used which represents the Current temperatures of all 6 cities at the current moment.

### 6. Custom Thresholds
- Users can define custom thresholds for Maximum temperatures and Minimum Temperatures.
- The app sends alerts when weather conditions exceed these thresholds.

### 7. Weather Summary Generation
-  User gets a Custom Weather Report of that day according to the data recieved by the api, which is generated using Google's Gemini flash 1.5.
-  To Enable this feature the user will need to Enter their own gemini flash 1.5 API Key.

### 8. Responsive Design
- The application is designed to be fully responsive, ensuring a seamless experience.

### 9. User-Friendly Interface
- Clean and intuitive user interface with a modern aesthetic.
- Easy navigation and accessibility for users of all technical levels.

## Technologies Used

### Frontend
- **HTML5**: Markup for structuring the application.
- **CSS3**: Styling with a focus on a modern and responsive design.
- **JavaScript**: Dynamic content rendering and interaction handling.
- **Font**: Utilizes [Poppins](https://fonts.google.com/specimen/Poppins) for a clean typography.

### Backend
- **Python**: The backend logic is implemented in Python.
- **Flask**: Flask is used to Design the API, etc.
- **JSON**: Weather data is stored and retrieved in JSON format for efficient handling.
- **Deque**: Utilized from the `collections` module to manage and optimize the performance of data structures.

## Installation

### Prerequisites
- Ensure you have [Python](https://www.python.org/downloads/) installed on your system.
- Optionally, create a virtual environment for package management.

### Steps to Install
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather-app.git

2. **Navigate to the Project Directory**
   ```bash
   cd Weather-Monitoring-Application
   
3. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Application:
   ```bash
   python app.py
5. Access the Application:
   ```bash
   http://localhost:5000/

## Usage
### Setting Custom thresholds
Input your desired thresholds for Maximum and Minimum Temperatures to get Alerts based on the set thresholds.

### Selecting a City
Select any city from the dropdown, to get the data for that city.

### Get a Graph Representation
User gets a graph which represents the data recieved for the selected city by the API from the moment of selecting the city to however long the application runs for.

### Get a Bar graph Representation
User gets a Bar graph which compares the current temperature of the six cities.

## Contact
For any questions, feedback, or inquiries, please reach out:
⚫ Sarthak Pundir
⚫ E-mail: sarthakpundir2003@gmail.com
⚫ GitHub: https://github.com/krimerwool

