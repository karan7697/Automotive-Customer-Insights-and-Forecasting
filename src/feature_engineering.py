import pandas as pd
from sklearn.preprocessing import StandardScaler

def feature_engineering():
    df = pd.read_csv('data/raw_data.csv')
    
    # Example feature engineering
    df['purchase_year'] = pd.to_datetime(df['purchase_date']).dt.year
    df['purchase_month'] = pd.to_datetime(df['purchase_date']).dt.month
    
    scaler = StandardScaler()
    df[['price_scaled']] = scaler.fit_transform(df[['price']])
    
    df.to_csv('data/processed_data.csv', index=False)

if __name__ == "__main__":
    feature_engineering()
