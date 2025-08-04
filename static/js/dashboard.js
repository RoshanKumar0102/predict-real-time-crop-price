// Market Insights Dashboard JavaScript
class MarketDashboard {
    constructor() {
        this.charts = {};
        this.updateInterval = null;
        this.lastUpdateTime = new Date();
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.initializeCharts();
        this.startRealTimeUpdates();
        this.setupFilters();
        this.initializeTooltips();
    }

    setupEventListeners() {
        // Filter event listeners
        document.getElementById('commodityFilter')?.addEventListener('change', (e) => {
            this.filterByCommodity(e.target.value);
        });

        document.getElementById('timeFilter')?.addEventListener('change', (e) => {
            this.filterByTime(e.target.value);
        });

        // Refresh button
        document.querySelector('.refresh-btn')?.addEventListener('click', () => {
            this.refreshData();
        });

        // Export button
        document.querySelector('.export-btn')?.addEventListener('click', () => {
            this.exportData();
        });

        // Commodity card clicks
        document.querySelectorAll('.commodity-card').forEach(card => {
            card.addEventListener('click', (e) => {
                const commodityName = e.currentTarget.querySelector('.commodity-name').textContent;
                this.showCommodityDetails(commodityName);
            });
        });

        // News item clicks
        document.querySelectorAll('.news-item').forEach(item => {
            item.addEventListener('click', (e) => {
                const newsTitle = e.currentTarget.querySelector('.news-title').textContent;
                this.showNewsDetails(newsTitle);
            });
        });
    }

    initializeCharts() {
        // Price Trend Chart
        const priceCtx = document.getElementById('priceTrendChart');
        if (priceCtx) {
            this.charts.priceTrend = new Chart(priceCtx.getContext('2d'), {
                type: 'line',
                data: {
                    labels: window.priceLabels || [],
                    datasets: [{
                        label: 'Composite Price Index',
                        data: window.priceData || [],
                        borderColor: '#2e7d32',
                        backgroundColor: 'rgba(46, 125, 50, 0.1)',
                        borderWidth: 3,
                        tension: 0.4,
                        fill: true,
                        pointBackgroundColor: '#2e7d32',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2,
                        pointRadius: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(0,0,0,0.8)',
                            titleColor: '#fff',
                            bodyColor: '#fff',
                            borderColor: '#2e7d32',
                            borderWidth: 1,
                            callbacks: {
                                label: function(context) {
                                    return `Price: ₹${context.parsed.y}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: { 
                            beginAtZero: false,
                            grid: { color: 'rgba(0,0,0,0.1)' },
                            ticks: {
                                callback: function(value) {
                                    return '₹' + value;
                                },
                                font: {
                                    size: 9
                                }
                            }
                        },
                        x: {
                            grid: { color: 'rgba(0,0,0,0.1)' },
                            ticks: {
                                font: {
                                    size: 9
                                }
                            }
                        }
                    },
                    interaction: {
                        intersect: false,
                        mode: 'index'
                    }
                }
            });
        }

        // Initialize additional charts if needed
        this.createCommodityComparisonChart();
    }

    createCommodityComparisonChart() {
        const comparisonCtx = document.getElementById('commodityComparisonChart');
        if (comparisonCtx) {
            const commodities = Array.from(document.querySelectorAll('.commodity-name')).map(el => el.textContent);
            const prices = Array.from(document.querySelectorAll('.commodity-price')).map(el => 
                parseInt(el.textContent.replace(/[^\d]/g, ''))
            );

            this.charts.commodityComparison = new Chart(comparisonCtx.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: commodities,
                    datasets: [{
                        label: 'Price (₹/Qtl)',
                        data: prices,
                        backgroundColor: 'rgba(46, 125, 50, 0.8)',
                        borderColor: '#2e7d32',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `₹${context.parsed.y}/Qtl`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return '₹' + value;
                                }
                            }
                        }
                    }
                }
            });
        }
    }

    startRealTimeUpdates() {
        // Update last updated time every minute
        setInterval(() => {
            this.updateLastUpdatedTime();
        }, 60000);

        // Simulate real-time data updates every 5 minutes
        this.updateInterval = setInterval(() => {
            this.simulateDataUpdate();
        }, 300000);
    }

    updateLastUpdatedTime() {
        const now = new Date();
        const lastUpdatedElement = document.getElementById('lastUpdated');
        if (lastUpdatedElement) {
            lastUpdatedElement.textContent = now.toLocaleString();
        }
    }

    simulateDataUpdate() {
        // Simulate price changes
        document.querySelectorAll('.commodity-change').forEach(changeElement => {
            const currentChange = parseFloat(changeElement.textContent.match(/[\d.]+/)[0]);
            const newChange = currentChange + (Math.random() - 0.5) * 2; // ±1% change
            const isPositive = newChange > 0;
            
            changeElement.textContent = `${isPositive ? '↗' : '↘'} ${Math.abs(newChange).toFixed(1)}%`;
            changeElement.className = `commodity-change ${isPositive ? 'positive' : 'negative'}`;
        });

        // Update pulse animation
        const pulseElement = document.querySelector('.pulse');
        if (pulseElement) {
            pulseElement.style.animation = 'none';
            setTimeout(() => {
                pulseElement.style.animation = 'pulse 2s infinite';
            }, 10);
        }
    }

    setupFilters() {
        // Commodity filter
        const commodityFilter = document.getElementById('commodityFilter');
        if (commodityFilter) {
            commodityFilter.addEventListener('change', (e) => {
                this.filterCommodities(e.target.value);
            });
        }

        // Time filter
        const timeFilter = document.getElementById('timeFilter');
        if (timeFilter) {
            timeFilter.addEventListener('change', (e) => {
                this.filterByTimeRange(e.target.value);
            });
        }
    }

    filterCommodities(commodity) {
        const commodityCards = document.querySelectorAll('.commodity-card');
        commodityCards.forEach(card => {
            const cardCommodity = card.querySelector('.commodity-name').textContent;
            if (!commodity || cardCommodity === commodity) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    filterByTimeRange(days) {
        // Simulate time-based filtering
        console.log(`Filtering data for last ${days} days`);
        // In a real implementation, this would fetch new data from the server
    }

    initializeTooltips() {
        // Add tooltips to metric cards
        document.querySelectorAll('.metric-card').forEach(card => {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltiptext';
            tooltip.textContent = 'Click for detailed analysis';
            card.appendChild(tooltip);
            card.classList.add('tooltip');
        });
    }

    refreshData() {
        const refreshBtn = document.querySelector('.refresh-btn');
        if (refreshBtn) {
            refreshBtn.innerHTML = '<i class="material-icons" style="font-size: 16px; margin-right: 5px;">sync</i> Refreshing...';
            refreshBtn.disabled = true;
            
            // Simulate data refresh
            setTimeout(() => {
                location.reload();
            }, 2000);
        }
    }

    exportData() {
        const exportBtn = document.querySelector('.export-btn');
        if (exportBtn) {
            exportBtn.innerHTML = '<i class="material-icons" style="font-size: 16px; margin-right: 5px;">download</i> Exporting...';
            exportBtn.disabled = true;
            
            // Generate CSV data
            const csvData = this.generateCSVData();
            const blob = new Blob([csvData], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `market-insights-${new Date().toISOString().split('T')[0]}.csv`;
            link.click();
            
            setTimeout(() => {
                exportBtn.innerHTML = '<i class="material-icons" style="font-size: 16px; margin-right: 5px;">download</i> Export';
                exportBtn.disabled = false;
            }, 1500);
        }
    }

    generateCSVData() {
        const commodities = Array.from(document.querySelectorAll('.commodity-name')).map(el => el.textContent);
        const prices = Array.from(document.querySelectorAll('.commodity-price')).map(el => 
            el.textContent.replace(/[^\d]/g, '')
        );
        const changes = Array.from(document.querySelectorAll('.commodity-change')).map(el => 
            el.textContent.replace(/[^\d.-]/g, '')
        );

        let csv = 'Commodity,Price (₹/Qtl),Change (%)\n';
        commodities.forEach((commodity, index) => {
            csv += `${commodity},${prices[index]},${changes[index]}\n`;
        });

        return csv;
    }

    showCommodityDetails(commodityName) {
        // Create modal for commodity details
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>${commodityName} - Detailed Analysis</h2>
                <div class="commodity-details">
                    <p><strong>Current Price:</strong> ₹${Math.floor(Math.random() * 2000 + 1500)}/Qtl</p>
                    <p><strong>Price Trend:</strong> ${Math.random() > 0.5 ? '↗' : '↘'} ${(Math.random() * 10).toFixed(1)}%</p>
                    <p><strong>Market Demand:</strong> ${Math.random() > 0.5 ? 'High' : 'Moderate'}</p>
                    <p><strong>Supply Status:</strong> ${Math.random() > 0.5 ? 'Stable' : 'Tight'}</p>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
        modal.style.display = 'block';

        // Close modal functionality
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = () => modal.remove();
        window.onclick = (event) => {
            if (event.target === modal) {
                modal.remove();
            }
        };
    }

    showNewsDetails(newsTitle) {
        // Create modal for news details
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <h2>Market News</h2>
                <h3>${newsTitle}</h3>
                <p>This is a detailed analysis of the market news. The impact on commodity prices and market trends will be monitored closely.</p>
                <p><strong>Date:</strong> ${new Date().toLocaleDateString()}</p>
                <p><strong>Source:</strong> Agricultural Market Intelligence</p>
            </div>
        `;

        document.body.appendChild(modal);
        modal.style.display = 'block';

        // Close modal functionality
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = () => modal.remove();
        window.onclick = (event) => {
            if (event.target === modal) {
                modal.remove();
            }
        };
    }

    // Utility functions
    formatCurrency(amount) {
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR'
        }).format(amount);
    }

    formatPercentage(value) {
        return `${value > 0 ? '+' : ''}${value.toFixed(1)}%`;
    }
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Make chart data available globally
    if (typeof window.priceLabels !== 'undefined' && typeof window.priceData !== 'undefined') {
        window.priceLabels = window.priceLabels;
        window.priceData = window.priceData;
    }
    
    // Initialize the dashboard
    window.marketDashboard = new MarketDashboard();
});

// Add modal styles
const modalStyles = `
<style>
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
}

.modal-content {
    background-color: white;
    margin: 15% auto;
    padding: 20px;
    border-radius: 8px;
    width: 80%;
    max-width: 500px;
    position: relative;
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
}

.close:hover {
    color: #000;
}

.commodity-details p {
    margin: 10px 0;
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}
</style>
`;

// Add modal styles to head
document.head.insertAdjacentHTML('beforeend', modalStyles); 