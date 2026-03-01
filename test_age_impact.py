import requests
import json

url = "http://127.0.0.1:5000/predict"

def get_prediction(age_value, label):
    data = {
        "age": age_value, 
        "gender": 1, # Female 
        "height": 177, 
        "weight": 80.0,
        "ap_hi": 180, 
        "ap_lo": 120, 
        "cholesterol": 3, # Well Above Normal
        "gluc": 2, # Above Normal
        "smoke": 1, # Smoker
        "alco": 1, # Yes
        "active": 0 # Sedentary
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            res = response.json()
            print(f"--- {label} (Age={age_value}) ---")
            print(f"Prediction: {res['prediction']}")
            print(f"Probability: {res['probability']}%")
            print(f"Risk Level: {res['level']}")
        else:
            print(f"Error {label}: {response.text}")
    except Exception as e:
        print(f"Exception {label}: {e}")

print("Testing Age Impact...")
# Case 1: Age in Years (Current Bug)
get_prediction(80, "Age in Years")

# Case 2: Age in Days (Proposed Fix)
get_prediction(80 * 365, "Age in Days")

def get_low_risk_prediction():
    data_low = {
        "age": 30,
        "gender": 1,
        "height": 170,
        "weight": 65,
        "ap_hi": 110,
        "ap_lo": 70,
        "cholesterol": 1,
        "gluc": 1,
        "smoke": 0,
        "alco": 0,
        "active": 1
    }
    print("\n--- Low Risk Case (Age=30, Normal BP, Healthy) ---")
    try:
        response = requests.post(url, json=data_low)
        if response.status_code == 200:
            res = response.json()
            print(f"Prediction: {res['prediction']}")
            print(f"Probability: {res['probability']}%")
            print(f"Risk Level: {res['level']}")
        else:
            print(f"Error Low Risk: {response.text}")
    except Exception as e:
        print(f"Exception Low Risk: {e}")

get_low_risk_prediction()
