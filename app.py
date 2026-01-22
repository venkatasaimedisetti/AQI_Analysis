import streamlit as st
import pandas as pd
from src.data_loader import load_local_data

# 1. Page Config (Always first)
st.set_page_config(page_title="AQI Analysis", layout="wide")

# 2. Define the function (MUST come before calling it)
@st.cache_data
def get_data():
    return load_local_data()

# 3. Now call the function
st.title("🌍 National AQI Analysis Dashboard")

df = get_data()

# 4. Handle if the data didn't load (The "NoneType" fix)
if df is None:
    st.error("Data file 'aqi.csv' not found in the 'data/' folder.")
    st.stop()

# 5. Rest of your dashboard logic...
st.success(f"Successfully loaded {len(df):,} records!")

# State Selector
state = st.sidebar.selectbox("Select a State", sorted(df['state'].unique()))
state_data = df[df['state'] == state]

# Display Metrics
st.metric(label=f"Average AQI in {state}", value=round(state_data['aqi_value'].mean(), 2))
st.bar_chart(state_data.groupby('area')['aqi_value'].mean().sort_values(ascending=False).head(10))