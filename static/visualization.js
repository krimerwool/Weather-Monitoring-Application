


function updateWeatherGraph(lineChartData, barChartData, summary) {
    const ctx = document.getElementById('weatherGraph').getContext('2d');
    const ctxBar = document.getElementById('barChart').getContext('2d');

    // Validate lineChartData
    console.log("updateweathergraph is being called")
    if (!lineChartData || !lineChartData.data || !Array.isArray(lineChartData.data)) {
        console.error("Invalid line chart data format");
        return;
    }

    // Validate barChartData
    if (!barChartData || !barChartData.categories || !Array.isArray(barChartData.categories) || !barChartData.series) {
        console.error("Invalid bar chart data format");
        return;
    }

    const timeLabels = lineChartData.data.map(entry => entry.call_time);
    const avgTemp = lineChartData.data.map(entry => entry.avg_temp);

    if (window.weatherChart) {
        window.weatherChart.destroy();
    }

    // Create new line chart
    window.weatherChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeLabels,
            datasets: [
                {
                    label: 'Avg Temp (°C)',
                    data: avgTemp,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    fill: true,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true
        }
    });
    if (window.barChart && typeof window.barChart.destroy === 'function') {
        window.barChart.destroy();
    }
    
    // Create new bar chart
    window.barChart = new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: barChartData.categories,  
            datasets: [{
                label: 'Favourite Colour',  
                data: barChartData.series.map(series => series.data), 
                backgroundColor: [
                    '#FF0000',  
                    '#0000FF',  
                    '#90EE90',  
                    '#FFD700',  
                    '#FFB6C1'   
                ], 
                borderColor: [
                    '#FF0000',  
                    '#0000FF',  
                    '#90EE90', 
                    '#FFD700', 
                    '#FFB6C1'   
                ],  
                borderWidth: 1,
                barPercentage: 0.8,  
                categoryPercentage: 0.8 
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,  
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'City',
                        font: {
                            size: 16, 
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        font: {
                            size: 14 
                        }
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature', 
                        font: {
                            size: 16, 
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        beginAtZero: true,  
                        font: {
                            size: 14  
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false  
                }
            }
        }
    });

    const summaryTextElement = document.getElementById('summaryText');  
    if (summaryTextElement) {
        summaryTextElement.innerText = summary.summary_text;  // Display the summary text
    } else {
        console.error("Summary text element not found");
    }
    


}
