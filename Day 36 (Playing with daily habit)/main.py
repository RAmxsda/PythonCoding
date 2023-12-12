import requests
from datetime import datetime
import os

# Personal info
GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "176"
AGE = "24"

# Nutritionix app_id and api_key
APP_ID = "7b30e90d"
API_KEY = "b647ad44d87486f48a85a08aea685cf4"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

# API CALL
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

result = response.json()
print(f"Nutritious API CALL: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "pythonworkout"
sheet_endpoint = (
    "https://api.sheety.co/48d4d836c7754fda717ed97a50ae2568/pythonWorkout/sheet1"
)

# Sheety API call
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(
    url=sheet_endpoint,
    json=sheet_inputs,
    headers={"Authorization": "Basic UmFtZXNoOmFiY2Rnc2hoanM="},
)

print(sheet_response.text)
