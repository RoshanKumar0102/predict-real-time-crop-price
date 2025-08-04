import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def get_forecast(crop_name):
    try:
        # Load and filter data
        df = pd.read_csv('data/crop_prices.csv')
        df = df[df['Crop'].str.lower() == crop_name.lower()]
        
        if df.empty:
            return [], [], [], []
        
        # Prepare data
        month_mapping = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6}
        df['MonthNum'] = df['Month'].map(month_mapping)
        
        X = df['MonthNum'].values.reshape(-1, 1)
        y = df['Price'].values
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict future
        future_months = np.array([7, 8, 9, 10, 11, 12]).reshape(-1, 1)
        forecast = model.predict(future_months)
        
        # Format results
        future_labels = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        return (
            df['Month'].tolist(), 
            y.tolist(), 
            future_labels, 
            forecast.round(2).tolist()
        )
        
    except Exception as e:
        print(f"Error in get_forecast: {str(e)}")
        return [], [], [], []