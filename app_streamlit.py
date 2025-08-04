import streamlit as st
from datetime import datetime, timedelta
from ml.predictor import CropPredictor
import random

predictor = CropPredictor()

# ----------------------------
# Utility Functions
# ----------------------------

def get_commodities_list():
    return ["Wheat", "Rice", "Cotton", "Soybean", "Maize", 
            "Coffee", "Groundnut", "Mustard", "Sunflower"]

def generate_market_insights():
    """Generate comprehensive market insights data"""
    commodities = get_commodities_list()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    current_month = datetime.now().month
    price_labels = months[current_month-6:current_month] + months[:current_month-6][:6]

    commodity_prices = {}
    commodity_changes = {}
    for commodity in commodities:
        commodity_prices[commodity] = random.randint(1500, 4000)
        commodity_changes[commodity] = round(random.uniform(-8.0, 8.0), 1)

    regional_prices = [
        {'name': 'North', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'South', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'East', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'West', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)}
    ]

    forecast_data = {
        'price_forecast': {
            'next_30_days': {
                'wheat': {'trend': 'up', 'change': round(random.uniform(2.0, 5.0), 1), 'reason': 'Strong domestic demand'},
                'rice': {'trend': 'up', 'change': round(random.uniform(1.5, 4.0), 1), 'reason': 'Export demand increasing'},
                'cotton': {'trend': 'down', 'change': round(random.uniform(-3.0, -1.0), 1), 'reason': 'Global supply surplus'},
                'soybean': {'trend': 'stable', 'change': round(random.uniform(-1.0, 1.5), 1), 'reason': 'Balanced supply-demand'},
                'maize': {'trend': 'up', 'change': round(random.uniform(1.0, 3.5), 1), 'reason': 'Feed industry demand'},
                'coffee': {'trend': 'up', 'change': round(random.uniform(2.5, 6.0), 1), 'reason': 'Premium quality demand'},
                'groundnut': {'trend': 'stable', 'change': round(random.uniform(-0.5, 2.0), 1), 'reason': 'Stable production'},
                'mustard': {'trend': 'down', 'change': round(random.uniform(-2.5, -0.5), 1), 'reason': 'Seasonal decline'},
                'sunflower': {'trend': 'up', 'change': round(random.uniform(1.0, 4.0), 1), 'reason': 'Oil industry demand'}
            },
            'next_quarter': {
                'overall_trend': 'moderate_increase',
                'key_factors': [
                    'Monsoon season impact on crop yields',
                    'Export demand from neighboring countries',
                    'Government MSP policy changes',
                    'Global commodity price movements'
                ],
                'risk_level': 'medium',
                'confidence': round(random.uniform(75, 90), 1)
            }
        },
        'seasonal_trends': {
            'q2_2024': {
                'monsoon_impact': 'positive',
                'expected_yield': 'above_average',
                'price_volatility': 'moderate',
                'export_outlook': 'strong',
                'key_commodities': ['wheat', 'rice', 'cotton']
            },
            'weather_factors': [
                'Early monsoon arrival expected',
                'Favorable rainfall distribution',
                'Temperature variations affecting crops',
                'Soil moisture levels optimal'
            ]
        },
        'risk_analysis': {
            'high_risk_factors': [
                'Weather anomalies affecting crop production',
                'Global supply chain disruptions',
                'Currency fluctuations impacting exports',
                'Government policy changes',
                'International trade tensions'
            ],
            'medium_risk_factors': [
                'Transportation cost increases',
                'Storage capacity limitations',
                'Quality standards enforcement',
                'Market speculation effects'
            ],
            'low_risk_factors': [
                'Domestic demand stability',
                'Established trade relationships',
                'Infrastructure improvements'
            ],
            'overall_risk_score': round(random.uniform(25, 45), 1)
        },
        'market_insights': {
            'top_performers': [
                {'commodity': 'Coffee', 'growth': round(random.uniform(8.0, 15.0), 1), 'reason': 'Premium quality demand'},
                {'commodity': 'Wheat', 'growth': round(random.uniform(4.0, 8.0), 1), 'reason': 'Strong domestic consumption'},
                {'commodity': 'Rice', 'growth': round(random.uniform(3.0, 6.0), 1), 'reason': 'Export market expansion'}
            ],
            'underperformers': [
                {'commodity': 'Cotton', 'decline': round(random.uniform(-8.0, -3.0), 1), 'reason': 'Global oversupply'},
                {'commodity': 'Mustard', 'decline': round(random.uniform(-5.0, -2.0), 1), 'reason': 'Seasonal factors'},
                {'commodity': 'Soybean', 'decline': round(random.uniform(-3.0, -1.0), 1), 'reason': 'Competition from imports'}
            ]
        }
    }

    forecast_summaries = [
        "Agricultural commodity prices are expected to remain stable...",
        "Strong demand from international markets is likely to drive prices upward...",
        "Supply chain improvements and government policies are expected...",
        "Seasonal factors and monsoon predictions may cause volatility...",
        "Government policies and MSP adjustments support price stability..."
    ]

    return {
        'price_trend': round(random.uniform(-5.0, 5.0), 1),
        'export_volume': random.randint(100000, 500000),
        'supply_status': random.choice(['Stable', 'Tight', 'Surplus']),
        'market_cap': random.randint(800000, 2000000),
        'price_labels': price_labels,
        'price_data': [round(random.uniform(100, 200), 1) for _ in range(11)],
        'commodities': commodities,
        'commodity_prices': commodity_prices,
        'commodity_changes': commodity_changes,
        'market_news': [
            {'title': 'Govt announces ₹50,000 Cr subsidies', 'date': datetime.now().strftime('%Y-%m-%d')},
            {'title': f'Drought affects {random.choice(commodities)}', 'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')},
            {'title': f'{random.choice(commodities)} exports up 15%', 'date': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')},
        ],
        'regional_prices': regional_prices,
        'forecast_summary': random.choice(forecast_summaries),
        'forecast_data': forecast_data,
        'top_gainers': predictor.get_top_gainers(),
        'top_losers': predictor.get_top_losers(),
        **predictor.get_market_insights()
    }

# ----------------------------
# Streamlit UI Starts Here
# ----------------------------

st.set_page_config(page_title="Crop Price Forecast", layout="wide")
st.title("🌾 Real-Time Crop Price Forecasting App")

menu = st.sidebar.radio("Navigate", ["Home", "Predictions", "Markets", "Commodity Details"])

# ----------------------------
# Home Page
# ----------------------------
if menu == "Home":
    st.header("📈 Market Movers")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top Gainers")
        st.table(predictor.get_top_gainers())
    with col2:
        st.subheader("Top Losers")
        st.table(predictor.get_top_losers())

# ----------------------------
# Predictions Page
# ----------------------------
elif menu == "Predictions":
    st.header("📊 Crop Predictions")
    crops = predictor.crop_data['Crop'].unique()
    today = datetime.now().strftime('%Y-%m-%d')

    for crop in crops:
        crop_name = str(crop)
        crop_data = predictor.get_crop_data(crop_name)
        forecast = predictor.get_forecast(crop_name)
        image_path = f"static/images/{crop_name.lower()}.jpg"

        with st.expander(f"🌿 {crop_name} ({today})"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(image_path, width=150)
            with col2:
                st.markdown(f"**Price:** ₹{crop_data.get('current_price')}")
                st.markdown(f"**Regions:** {', '.join(crop_data.get('production_regions', []))}")
                st.markdown(f"**Exports:** {', '.join(crop_data.get('export_markets', []))}")
                st.markdown(f"**Forecast:** {forecast}")

# ----------------------------
# Markets Page
# ----------------------------
elif menu == "Markets":
    st.header("📈 Market Insights")
    insights = generate_market_insights()

    st.subheader("🔍 Key Metrics")
    st.metric("Market Trend", f"{insights['price_trend']}%")
    st.metric("Export Volume", f"{insights['export_volume']}")
    st.metric("Supply Status", insights['supply_status'])

    st.subheader("🌐 Regional Prices")
    st.table(insights['regional_prices'])

    st.subheader("📢 Market News")
    for news in insights['market_news']:
        st.markdown(f"**{news['date']}** - {news['title']}")

# ----------------------------
# Commodity Details Page
# ----------------------------
elif menu == "Commodity Details":
    crop_selected = st.selectbox("Select a Crop", get_commodities_list())
    crop_data = predictor.get_crop_data(crop_selected)
    forecast = predictor.get_forecast(crop_selected)

    if crop_data:
        st.subheader(f"{crop_selected} Details")
        st.write(crop_data)
        st.subheader("Forecast")
        st.write(forecast)
    else:
        st.warning("Crop not found.")
