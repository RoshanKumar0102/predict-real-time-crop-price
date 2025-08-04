document.addEventListener('DOMContentLoaded', () => {
  const fc = document.getElementById('forecastChart');
  const pc = document.getElementById('previousChart');
  const cc = document.getElementById('priceChart');

  new Chart(fc, {
    type: 'line',
    data: {
      labels: forecast_x,
      datasets: [{
        label: 'Forecast Price (₹)',
        data: forecast_y,
        borderColor: 'green',
        backgroundColor: 'rgba(0,255,0,0.2)',
        tension: 0.3,
        fill: true
      }]
    }
  });

  new Chart(pc, {
    type: 'line',
    data: {
      labels: previous_x,
      datasets: [{
        label: 'Previous Price (₹)',
        data: previous_y,
        borderColor: 'orange',
        backgroundColor: 'rgba(255,165,0,0.2)',
        tension: 0.3,
        fill: true
      }]
    }
  });

  new Chart(cc, {
    type: 'line',
    data: {
      labels: combined_labels,
      datasets: [{
        label: 'Price Trend (₹)',
        data: combined_data,
        borderColor: 'blue',
        backgroundColor: 'rgba(0,0,255,0.2)',
        fill: true,
        tension: 0.3
      }]
    }
  });
});
document.addEventListener('DOMContentLoaded', function() {
    try {
        // Forecast Chart
        const forecastCtx = document.getElementById('forecastChart').getContext('2d');
        new Chart(forecastCtx, {
            type: 'line',
            data: {
                labels: chartData.forecast_x,
                datasets: [{
                    label: 'Forecast Price (₹/qtl)',
                    data: chartData.forecast_y,
                    borderColor: 'rgb(75, 192, 192)',
                    backgroundColor: 'rgba(75, 192, 192, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.1,
                    pointRadius: 4
                }]
            },
            options: getChartOptions('Price Forecast')
        });

        // Previous Prices Chart
        const previousCtx = document.getElementById('previousChart').getContext('2d');
        new Chart(previousCtx, {
            type: 'line',
            data: {
                labels: chartData.previous_x,
                datasets: [{
                    label: 'Previous Prices (₹/qtl)',
                    data: chartData.previous_y,
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgba(255, 99, 132, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.1,
                    pointRadius: 4
                }]
            },
            options: getChartOptions('Previous Prices')
        });

    } catch (error) {
        console.error('Chart initialization error:', error);
    }
});

function getChartOptions(title) {
    return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            title: {
                display: true,
                text: title
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `₹${context.raw.toFixed(2)}/qtl`;
                    }
                }
            }
        },
        scales: {
            y: {
                title: {
                    display: true,
                    text: 'Price (₹/qtl)'
                },
                beginAtZero: false
            },
            x: {
                title: {
                    display: true,
                    text: 'Month'
                }
            }
        }
    };
}