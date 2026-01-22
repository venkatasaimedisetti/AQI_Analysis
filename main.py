import os
from src.data_loader import load_local_data
from src.analysis import generate_visual_insights
from src.model_trainer import train_prediction_model

def run_project_pipeline():
    print("[INFO] Initializing AQI Analysis Pipeline...")

    # Load
    data = load_local_data()
    if data is None:
        return

    # Analyze
    print("[INFO] Running Exploratory Data Analysis...")
    generate_visual_insights(data)

    # ML Train
    print("[INFO] Training Predictive Model (Random Forest)...")
    r2 = train_prediction_model(data)
    
    print("-" * 40)
    print(f"PIPELINE SUCCESSFUL")
    print(f"Model Performance (R2): {r2:.4f}")
    print("-" * 40)

if __name__ == "__main__":
    # Safety check for the output directory
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    run_project_pipeline()