import pandas as pd
import os

def load_local_data():
    """
    Handles data ingestion and basic cleanup.
    Standardizes headers to lowercase to avoid KeyErrors.
    """
    path = os.path.join('data', 'aqi.csv')
    
    if not os.path.exists(path):
        print(f"Error: Missing {path}. Please check the data directory.")
        return None
        
    # Using low_memory=False to handle the large 235k row CSV efficiently
    df = pd.read_csv(path, low_memory=False)
    
    # Strip whitespace and lowercase columns - standard dev practice
    df.columns = df.columns.str.strip().str.lower()
    
    # Cleaning: Removing rows without AQI values as they are noise for the ML model
    initial_count = len(df)
    df = df.dropna(subset=['aqi_value', 'state'])
    
    print(f"Successfully cleaned data. Rows retained: {len(df)} (Dropped {initial_count - len(df)} nulls)")
    return df