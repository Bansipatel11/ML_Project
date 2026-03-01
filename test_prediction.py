import urllib.request
import json

url = "http://127.0.0.1:5000/predict"
data = {
    "age": 20000, "gender": 1, "height": 165, "weight": 65.0,
    "ap_hi": 120, "ap_lo": 80, "cholesterol": 1, "gluc": 1,
    "smoke": 0, "alco": 0, "active": 1
}

req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(data)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))

try:
    response = urllib.request.urlopen(req, jsondataasbytes)
    print(f"Status Code: {response.getcode()}")
    print(f"Response: {response.read().decode('utf-8')}")
    if response.getcode() == 200:
        print("SUCCESS: Prediction works!")
except Exception as e:
    print(f"ERROR: Could not connect to server: {e}")
