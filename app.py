from flask import Flask, render_template
from ml.predictor import CropPredictor
from datetime import datetime, timedelta
import random

app = Flask(__name__)
predictor = CropPredictor()

def get_commodities_list():
    return ["Wheat", "Rice", "Cotton", "Soybean", "Maize", 
            "Coffee", "Groundnut", "Mustard", "Sunflower"]

def generate_market_insights():
    """Generate comprehensive market insights data"""
    commodities = get_commodities_list()
    
    # Generate sample price trends for the chart
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    current_month = datetime.now().month
    price_labels = months[current_month-6:current_month] + months[:current_month-6][:6]
    
    # Generate commodity prices and changes
    commodity_prices = {}
    commodity_changes = {}
    for commodity in commodities:
        commodity_prices[commodity] = random.randint(1500, 4000)
        commodity_changes[commodity] = round(random.uniform(-8.0, 8.0), 1)
    
    # Generate regional prices with trends
    regional_prices = [
        {'name': 'North', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'South', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'East', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)},
        {'name': 'West', 'commodity': random.choice(commodities), 'price': random.randint(1500, 3000), 'trend': round(random.uniform(-5.0, 5.0), 1)}
    ]
    
    # Generate comprehensive forecast data
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
    
    # Generate market forecast summary
    forecast_summaries = [
        "Agricultural commodity prices are expected to remain stable with moderate fluctuations. Wheat and Rice prices may increase by 2-3%, while Cotton and Soybean could see slight declines due to global supply factors.",
        "Strong demand from international markets is likely to drive prices upward in the next month, particularly for premium commodities like Coffee and Rice.",
        "Supply chain improvements and government policies are expected to stabilize prices across major commodities with moderate growth expected.",
        "Seasonal factors and monsoon predictions may cause temporary price volatility in certain commodities, particularly grains and oilseeds.",
        "Government policies and MSP adjustments are expected to support price stability in the agricultural sector with controlled inflation."
    ]
    
    return {
        # Key metrics
        'price_trend': round(random.uniform(-5.0, 5.0), 1),
        'export_volume': random.randint(100000, 500000),
        'supply_status': random.choice(['Stable', 'Tight', 'Surplus']),
        'market_cap': random.randint(800000, 2000000),
        
        # Chart data
        'price_labels': price_labels,
        'price_data': [round(random.uniform(100, 200), 1) for _ in range(11)],
        
        # Commodity data
        'commodities': commodities,
        'commodity_prices': commodity_prices,
        'commodity_changes': commodity_changes,
        
        # Market news
        'market_news': [
            {'title': 'Government announces new agricultural subsidies worth ₹50,000 crore', 'date': datetime.now().strftime('%Y-%m-%d')},
            {'title': f'Drought conditions affect {random.choice(commodities)} production in major states', 'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')},
            {'title': f'Export demand for {random.choice(commodities)} increases by 15%', 'date': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')},
            {'title': 'New technology adoption improves crop yields across regions', 'date': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')},
            {'title': 'International trade agreements boost agricultural exports', 'date': (datetime.now() - timedelta(days=20)).strftime('%Y-%m-%d')}
        ],
        
        # Regional prices with trends
        'regional_prices': regional_prices,
        
        # Market insights
        'forecast_summary': random.choice(forecast_summaries),
        'forecast_data': forecast_data,
        'top_gainers': predictor.get_top_gainers(),
        'top_losers': predictor.get_top_losers(),
        
        # Additional data from your existing predictor
        **predictor.get_market_insights()
    }

@app.route('/')
def home():
    try:
        return render_template(
            'home.html',
            top_gainers=predictor.get_top_gainers(),
            top_losers=predictor.get_top_losers(),
            commodities=get_commodities_list()
        )
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/commodity/<crop_name>')
def commodity(crop_name):
    try:
        crop_data = predictor.get_crop_data(crop_name)
        if not crop_data:
            return render_template('error.html', error=f"Crop '{crop_name}' not found"), 404
            
        return render_template('commodity.html',
            crop=crop_data,
            forecast=predictor.get_forecast(crop_name)
        )
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/markets')
def markets():
    try:
        insights = generate_market_insights()
        return render_template('markets.html',
            insights=insights
        )
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/predictions')
def predictions():
    crops = predictor.crop_data['Crop'].unique()
    crop_cards = []
    for crop in crops:
        crop_name = str(crop)
        crop_data = predictor.get_crop_data(crop_name)
        forecast = predictor.get_forecast(crop_name)
        # Try to find an image for the crop
        image_filename = f"{crop_name.lower()}.jpg"
        image_path = f"/static/images/{image_filename}"
        crop_cards.append({
            'name': crop_name,
            'image': image_path,
            'regions': crop_data['production_regions'] if crop_data else [],
            'exports': crop_data['export_markets'] if crop_data else [],
            'current_price': crop_data['current_price'] if crop_data else None,
            'forecast': forecast
        })
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('prediction.html', crop_cards=crop_cards, today=today)

if __name__ == '__main__':
    app.run(debug=True,port=10000)

