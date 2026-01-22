import streamlit as st
import pandas as pd
import os
from src.data_loader import load_local_data

# Page Config
st.set_page_config(page_title="National AQI Analyzer", layout="wide", page_icon="🌍")

st.title("🌍 National Air Quality Index (AQI) Dashboard")
st.markdown("""
This dashboard analyzes **235,785 environmental records** across India. 
It uses a Random Forest model to analyze pollution trends.
""")

# Load Data
@st.cache_data
def get_data():
    return load_local_data()

try:
    df = get_data()

    # Sidebar Filters
    st.sidebar.header("Filter Data")
    state = st.sidebar.selectbox("Select State", sorted(df['state'].unique()))
    
    # Filter data based on selection
    state_data = df[df['state'] == state]
    
    # Dashboard Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg AQI (State)", f"{state_data['aqi_value'].mean():.2f}")
    col2.metric("Max AQI Recorded", f"{state_data['aqi_value'].max()}")
    col3.metric("Total Records", f"{len(state_data):,}")

    # Visualizations
    st.subheader(f"Pollution Trends in {state}")
    
    # Area-wise comparison within the state
    area_avg = state_data.groupby('area')['aqi_value'].mean().sort_values(ascending=False).head(10)
    st.bar_chart(area_avg)

    st.subheader("Raw Data Preview")
    st.dataframe(state_data.head(100))

except Exception as e:
    st.error(f"Please ensure 'aqi.csv' is in the 'data' folder. Error: {e}")