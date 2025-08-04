import os
import pandas as pd
import json
from chardet import detect
from datetime import datetime
from sklearn.linear_model import LinearRegression


class CropPredictor:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.crop_data = self.load_data()
        self.market_data = self.load_market_data()

    def detect_encoding(self, file_path):
        with open(file_path, 'rb') as f:
            result = detect(f.read(10000))
        return result['encoding']

    def load_data(self):
        csv_path = os.path.join(self.base_dir, 'data', 'crop_prices.csv')
        try:
            try:
                df = pd.read_csv(csv_path, encoding='utf-8')
            except UnicodeDecodeError:
                encoding = self.detect_encoding(csv_path)
                df = pd.read_csv(csv_path, encoding=encoding)

            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'])
            return df

        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_path}")
            return pd.DataFrame(columns=['Crop', 'Price', 'Date'])  # type: ignore
        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            return pd.DataFrame(columns=['Crop', 'Price', 'Date'])  # type: ignore

    def load_market_data(self):
        json_path = os.path.join(self.base_dir, 'data', 'market_data.json')
        try:
            with open(json_path, 'rb') as f:
                raw_data = f.read()
                encoding = 'utf-8-sig' if raw_data.startswith(b'\xef\xbb\xbf') else 'utf-8'
                try:
                    return json.loads(raw_data.decode(encoding))
                except UnicodeDecodeError:
                    return json.loads(raw_data.decode('utf-16'))
        except FileNotFoundError:
            print(f"Error: JSON file not found at {json_path}")
            return {}
        except Exception as e:
            print(f"Error reading JSON: {str(e)}")
            return {}

    def get_crop_data(self, crop_name):
        crop_df = self.crop_data[self.crop_data['Crop'].str.lower() == crop_name.lower()]
        if crop_df.empty:
            return None
        return {
            'name': crop_name,
            'current_price': crop_df['Price'].iloc[-1],  # type: ignore
            'production_regions': self.get_production_regions(crop_name),
            'export_markets': self.get_export_markets(crop_name)
        }

    def get_top_gainers(self, days=7):
        df = self.crop_data.copy()
        if df.empty or 'Price' not in df.columns or 'Crop' not in df.columns:
            return self._fallback_gainers()

        df['price_change'] = df.groupby('Crop')['Price'].pct_change(periods=days) * 100
        result = (
            df.sort_values('price_change', ascending=False)
              .dropna()
              .head(5)
              .rename(columns={'Crop': 'name', 'Price': 'price', 'price_change': 'change'})
              .loc[:, ['name', 'price', 'change']]
              .to_dict('records')
        )
        for item in result:
            item['change'] = round(item['change'], 3)
        return result

    def get_top_losers(self, days=7):
        df = self.crop_data.copy()
        if df.empty or 'Price' not in df.columns or 'Crop' not in df.columns:
            return self._fallback_losers()

        df['price_change'] = df.groupby('Crop')['Price'].pct_change(periods=days) * 100
        result = (
            df.sort_values('price_change', ascending=True)
              .dropna()
              .head(5)
              .rename(columns={'Crop': 'name', 'Price': 'price', 'price_change': 'change'})
              .loc[:, ['name', 'price', 'change']]
              .to_dict('records')
        )
        for item in result:
            item['change'] = round(item['change'], 3)
        return result

    def _fallback_gainers(self):
        return [
            {"name": "Gram", "price": 3920.4, "change": 3.4},
            {"name": "Sunflower", "price": 3877.6, "change": 2.9},
            {"name": "Jute", "price": 2871.79, "change": 2.5},
            {"name": "Rape", "price": 3200.0, "change": 2.1},
            {"name": "Bajra", "price": 1561.68, "change": 1.9}
        ]

    def _fallback_losers(self):
        return [
            {"name": "Wheat", "price": 2040.0, "change": -2.8},
            {"name": "Cotton", "price": 6380.5, "change": -2.5},
            {"name": "Soybean", "price": 4530.3, "change": -2.2},
            {"name": "Maize", "price": 1890.0, "change": -1.8},
            {"name": "Mustard", "price": 5450.75, "change": -1.5}
        ]

    def get_forecast(self, crop_name, periods=6):
        crop_df = self.crop_data[self.crop_data['Crop'].str.lower() == crop_name.lower()]
        if crop_df.empty:
            return []

        X = crop_df.index.values.reshape(-1, 1)  # type: ignore
        y = crop_df['Price'].values  # type: ignore
        model = LinearRegression()
        model.fit(X, y)

        future_X = [[i] for i in range(len(X), len(X)+periods)]
        forecast_prices = model.predict(future_X)

        last_price = y[-1]
        forecast = []
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for i, price in enumerate(forecast_prices):
            month = months[(datetime.now().month + i - 1) % 12]
            change = ((price - last_price) / last_price) * 100
            forecast.append((month, round(price, 2), round(change, 2)))
            last_price = price

        return forecast

    def get_market_insights(self):
        return {
            'trends': self.market_data.get('trends', []),
            'news': self.market_data.get('news', []),
            'last_updated': self.market_data.get('last_updated', '')
        }

    def get_production_regions(self, crop_name):
        regions = {
            'wheat': ['Punjab', 'Haryana', 'Uttar Pradesh'],
            'rice': ['West Bengal', 'Punjab', 'Andhra Pradesh'],
            'cotton': ['Maharashtra', 'Gujarat', 'Punjab'],
            'maize': ['Karnataka', 'Andhra Pradesh', 'Bihar'],
            'soybean': ['Madhya Pradesh', 'Maharashtra', 'Rajasthan'],
            'mustard': ['Rajasthan', 'Uttar Pradesh', 'Haryana'],
            'sunflower': ['Karnataka', 'Andhra Pradesh', 'Maharashtra'],
            'groundnut': ['Gujarat', 'Andhra Pradesh', 'Tamil Nadu'],
            'coffee': ['Karnataka', 'Kerala', 'Tamil Nadu']
        }
        return regions.get(crop_name.lower(), ['Multiple regions'])

    def get_export_markets(self, crop_name):
        markets = {
            'wheat': ['Bangladesh', 'Nepal', 'UAE'],
            'rice': ['Iran', 'Iraq', 'Saudi Arabia'],
            'cotton': ['China', 'Bangladesh', 'Vietnam'],
            'maize': ['Malaysia', 'Indonesia', 'Vietnam'],
            'soybean': ['China', 'Japan', 'Vietnam'],
            'mustard': ['Bangladesh', 'Nepal', 'Pakistan'],
            'sunflower': ['Turkey', 'Egypt', 'Iran'],
            'groundnut': ['Indonesia', 'Vietnam', 'Philippines'],
            'coffee': ['Italy', 'Germany', 'Russia']
        }
        return markets.get(crop_name.lower(), ['Global markets'])
