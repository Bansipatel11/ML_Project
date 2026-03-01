import requests
import json

url = "http://127.0.0.1:5000/predict"

def test_high_risk():
    print("Testing High Risk Input (Age 80, BP 180)...")
    data = {
        "age": 29200, # 80 years in days
        "gender": 1,
        "height": 177,
        "weight": 80.0,
        "ap_hi": 180,
        "ap_lo": 120,
        "cholesterol": 3,
        "gluc": 2,
        "smoke": 1,
        "alco": 1,
        "active": 0
    }
    try:
        res = requests.post(url, json=data).json()
        print(f"Prediction: {res['prediction']}")
        print(f"Probability: {res['probability']}%")
        print(f"Risk Level: {res['level']}")
        
        if res['level'] == "High":
            print("SUCCESS: Risk Level is High.")
        else:
            print(f"FAILURE: Risk Level is {res['level']} (Expected High).")
            
    except Exception as e:
        print(f"Error: {e}")

test_high_risk()
