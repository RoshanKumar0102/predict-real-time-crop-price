# Market Insights Dashboard

A comprehensive real-time agricultural commodity trends and analysis dashboard built with Flask, featuring interactive charts, live data updates, and market intelligence.

## 🌟 Features

### 📊 Real-time Market Analytics
- **Live Price Trends**: Real-time commodity price tracking with interactive charts
- **Market Metrics**: Key performance indicators including price trends, export volume, and supply chain status
- **Regional Analysis**: Price variations across different regions with trend indicators
- **Commodity Performance**: Individual commodity cards with current prices and change percentages

### 📈 Interactive Data Visualization
- **Price Trend Charts**: Smooth line charts showing composite price index over time
- **Commodity Comparison**: Bar charts comparing prices across different commodities
- **Real-time Updates**: Live data refresh with visual indicators
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices

### 🔍 Advanced Filtering & Controls
- **Commodity Filter**: Filter data by specific agricultural commodities
- **Time Range Filter**: Analyze data for different time periods (7 days, 30 days, 90 days, 1 year)
- **Real-time Refresh**: Manual data refresh with loading indicators
- **Data Export**: Export market insights to CSV format

### 📰 Market Intelligence
- **Latest News**: Real-time market news and updates
- **Top Gainers/Losers**: Performance tracking of best and worst performing commodities
- **Market Forecast**: AI-powered market predictions and trend analysis
- **Supply Chain Status**: Real-time supply chain monitoring

### 🎨 Modern UI/UX
- **Clean Design**: Modern, professional interface with intuitive navigation
- **Color-coded Indicators**: Visual indicators for positive/negative trends
- **Interactive Elements**: Hover effects, tooltips, and clickable components
- **Mobile Responsive**: Optimized for all screen sizes

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Flask
- pandas
- scikit-learn
- chardet

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd predict-real-time-crop-price
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:5000`
   - Click on "Markets" in the navigation to access the Market Insights Dashboard

## 📁 Project Structure

```
predict-real-time-crop-price/
├── app.py                          # Main Flask application
├── data/                           # Data files
│   ├── crop_prices.csv            # Historical crop price data
│   └── market_data.json           # Market intelligence data
├── ml/                            # Machine learning components
│   ├── __init__.py
│   └── predictor.py               # Crop price prediction model
├── static/                        # Static assets
│   ├── css/
│   │   ├── dashboard.css          # Dashboard-specific styles
│   │   └── main.css              # General styles
│   ├── js/
│   │   ├── dashboard.js           # Dashboard JavaScript functionality
│   │   └── main.js               # General JavaScript
│   └── images/                    # Commodity images
├── templates/                     # HTML templates
│   ├── base.html                 # Base template
│   ├── markets.html              # Market Insights Dashboard
│   └── other templates...
└── README.md                     # This file
```

## 🎯 Dashboard Components

### 1. Key Metrics Cards
- **Price Trend**: Overall market price movement
- **Export Volume**: Current quarter export statistics
- **Supply Chain**: Real-time supply chain status
- **Market Cap**: Total market capitalization

### 2. Interactive Charts
- **Price Trend Chart**: Line chart showing composite price index
- **Commodity Comparison**: Bar chart comparing commodity prices
- **Regional Analysis**: Table with regional price variations

### 3. Market Intelligence
- **Latest News**: Real-time market updates
- **Top Performers**: Best and worst performing commodities
- **Market Forecast**: AI-powered predictions

### 4. Controls & Filters
- **Commodity Filter**: Filter by specific commodities
- **Time Filter**: Analyze different time periods
- **Refresh Button**: Manual data refresh
- **Export Button**: Download data as CSV

## 🔧 Technical Features

### Real-time Updates
- Automatic data refresh every 5 minutes
- Live "LIVE" indicator with pulse animation
- Last updated timestamp
- Simulated price changes for demonstration

### Interactive Elements
- Clickable commodity cards with detailed modals
- Hover effects and tooltips
- Smooth animations and transitions
- Responsive design for all devices

### Data Visualization
- Chart.js integration for interactive charts
- Custom CSS for modern styling
- Color-coded indicators for trends
- Professional typography and spacing

### Export Functionality
- CSV export with formatted data
- Automatic filename generation with date
- Download progress indicators

## 🎨 Design System

### Color Palette
- **Primary**: #2e7d32 (Green)
- **Secondary**: #1976d2 (Blue)
- **Success**: #4caf50 (Green)
- **Warning**: #ff9800 (Orange)
- **Danger**: #f44336 (Red)

### Typography
- Clean, modern font stack
- Consistent sizing hierarchy
- Proper contrast ratios for accessibility

### Components
- Card-based layout
- Consistent spacing and padding
- Smooth hover effects
- Professional animations

## 📱 Responsive Design

The dashboard is fully responsive and optimized for:
- **Desktop**: Full feature set with side-by-side layouts
- **Tablet**: Adjusted grid layouts and touch-friendly controls
- **Mobile**: Single-column layout with optimized touch targets

## 🔮 Future Enhancements

### Planned Features
- **Real-time API Integration**: Connect to live market data APIs
- **Advanced Analytics**: More sophisticated trend analysis
- **User Authentication**: Personalized dashboards
- **Push Notifications**: Real-time alerts for price changes
- **Advanced Filtering**: More granular filtering options
- **Data Export**: Additional export formats (PDF, Excel)

### Technical Improvements
- **WebSocket Integration**: Real-time data streaming
- **Caching**: Improved performance with data caching
- **API Rate Limiting**: Proper API usage management
- **Error Handling**: Robust error handling and recovery

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Chart.js for excellent charting capabilities
- Material Design for UI inspiration
- Flask community for the robust web framework
- Agricultural market data providers for insights

---

**Built with ❤️ for the agricultural community** 