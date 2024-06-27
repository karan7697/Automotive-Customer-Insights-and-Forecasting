import pandas as pd
from prophet import Prophet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def load_data():
    df = pd.read_csv('data/processed_data.csv')
    return df

def train_model(df):
    df['ds'] = pd.to_datetime(df['purchase_date'])
    df['y'] = df['price']
    
    train_df, test_df = train_test_split(df, test_size=0.2, shuffle=False)
    
    model = Prophet()
    model.fit(train_df[['ds', 'y']])
    
    forecast = model.predict(test_df[['ds']])
    mae = mean_absolute_error(test_df['y'], forecast['yhat'])
    
    print(f'Mean Absolute Error: {mae}')
    
    model.plot(forecast).savefig('results/forecast.png')

if __name__ == "__main__":
    df = load_data()
    train_model(df)
