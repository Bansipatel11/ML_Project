import joblib
import pandas as pd
import numpy as np
import os

print(f"Current working directory: {os.getcwd()}")
try:
    scaler = joblib.load("model/scaler.pkl")
    print("Scaler loaded successfully.")
    
    if hasattr(scaler, "feature_names_in_"):
        print(f"Features expected by scaler ({len(scaler.feature_names_in_)}):")
        for i, run in enumerate(scaler.feature_names_in_):
            print(f"{i+1}. {run}")
    else:
        print("Scaler does not have 'feature_names_in_' attribute.")
        print(f"Mean shape: {scaler.mean_.shape}")
        print(f"Number of features expected: {scaler.mean_.shape[0]}")
        
except Exception as e:
    print(f"Error loading scaler: {e}")
