
async function getCurrentAvgTemp() {
    try {
        const selectedCity = document.getElementById('cityDropdown').value;
        if (!selectedCity) {
            alert("Please select a city to get the current temperature.");
            return null;
        }

        const response = await fetch(`/daily-summary?city=${selectedCity}`);
        if (!response.ok) throw new Error('Failed to fetch weather data');

        const weatherData = await response.json();
        const cityKey = capitalize(selectedCity);

        if (!weatherData[cityKey]) throw new Error('City data not found');

        const avgTempArray = weatherData[cityKey].avg_temp;
        return avgTempArray[avgTempArray.length - 1]; 
    } catch (error) {
        console.error('Error fetching current average temperature:', error);
        return null;
    }
}

// Function to handle threshold submissions
async function handleThresholdSubmission() {
    const selectedCity = document.getElementById('cityDropdown').value;
    if (!selectedCity) {
        alert("Please select a city to get the current temperature.");
        return; 
    }

    const maxThreshold = parseFloat(document.getElementById('maxThreshold').value);
    const minThreshold = parseFloat(document.getElementById('minThreshold').value);

    if (isNaN(maxThreshold) || isNaN(minThreshold)) {
        alert('Please enter valid numerical threshold values.');
        return; 
    }

    const currentAvgTemp = await getCurrentAvgTemp();
    if (currentAvgTemp === null) return;

    if (minThreshold > currentAvgTemp) {
        alert('ALERT: The Current temperature is too low.');
    } else if (maxThreshold < currentAvgTemp) {
        alert('ALERT: The Current temperature is too high.');
    } else {
        alert('Current temperature is within the specified thresholds.');
    }

    showWeatherCards();
}

function showWeatherCards() {
    document.getElementById('weather-card').style.display = 'block';
    document.getElementById('graph-card').style.display = 'block';
    document.getElementById('historical-card').style.display = 'block';
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

document.getElementById('submitThresholds').addEventListener('click', handleThresholdSubmission);

document.getElementById('cityDropdown').addEventListener('change', async () => {
    const cityName = document.getElementById('cityDropdown').value;
    if (cityName) {
        console.log("City selected: ", cityName);
        await checkWeather(cityName);
        showWeatherCards(); 
    } else {
        alert('Please select a city to view the weather data.');
    }
});
