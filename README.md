# 🌍 National Air Quality Index (AQI) Analysis Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://air-quality-index-by-me.streamlit.app/)

A modular Python framework designed to process, analyze, and predict Air Quality Index (AQI) trends using a dataset of **235,000+ environmental records**. This project demonstrates a full-stack data engineering approach, from raw CSV ingestion to a live interactive web dashboard.

[Image of a software architecture diagram showing modular components: Data Layer, Logic Layer, and Output Layer]

## 🔗 Live Deployment
The application is currently live and accessible at:  
**[https://air-quality-index-by-me.streamlit.app/](https://air-quality-index-by-me.streamlit.app/)**

## 🛠️ Project Architecture
The system is built using **Separation of Concerns** (SoC) principles, moving beyond flat scripts into a professional modular structure:

* **`main.py`**: The central orchestrator that triggers the end-to-end pipeline.
* **`src/data_loader.py`**: ETL logic featuring automated header normalization and robust null-handling for high-volume data.
* **`src/analysis.py`**: Statistical visualization module that generates distribution profiles and saves them to the `outputs/` directory.
* **`src/model_trainer.py`**: Predictive engine utilizing a **Random Forest Regressor** to handle non-linear pollution variables ($R^2 \approx 0.92$).
* **`app.py`**: Reactive Streamlit interface with built-in data caching for high-speed user interactions.

[Image of a supervised machine learning workflow diagram: Data -> Features -> Training -> Model -> Prediction]

## 📊 Technical Highlights
* **High-Volume Processing:** Optimized to handle ~236k rows using Pandas vectorized operations for maximum efficiency.
* **Production Stability:** Implemented version pinning in `requirements.txt` to resolve compatibility issues between `Altair`, `Streamlit`, and `Python 3.13`.
* **Defensive Engineering:** Automated directory management (OS module) and error handling for missing data assets to prevent runtime crashes.
* **Scalable Modeling:** Ensemble learning approach chosen for its resilience against outliers in environmental datasets.

## 📁 Repository Map
```text
AQI_Analysis/
├── data/               # Source dataset (aqi.csv)
├── src/                # Modular logic files
│   ├── data_loader.py  # Data cleaning & ETL
│   ├── analysis.py     # EDA & Visualization
│   └── model_trainer.py# ML Model Logic
├── outputs/            # Auto-generated analytical reports
├── app.py              # Streamlit Web Dashboard
├── main.py             # Pipeline Entry Point
├── requirements.txt    # Cloud dependency configuration
└── .gitignore          # Version control exclusions

