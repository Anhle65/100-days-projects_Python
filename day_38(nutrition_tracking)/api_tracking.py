import requests
from datetime import datetime
API_key = "51271aac0e4614b0b1948140e934aa0a"
app_id = "dadbfd87"
data = input("what activity you did? ")
header = {

    'x-app-id': app_id,
    'x-app-key': API_key,
    "Content-Type": "application/json"
    }
endpoint_post = "https://trackapi.nutritionix.com/v2/natural/exercise"
para = {
    'query': data,
    "gender": "female",
    "weight_kg": "49",
    "height_cm": '150',
    'age': '21'

}
res = requests.post(endpoint_post, json=para, headers=header)
exercises = res.json()
print(exercises)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety = "https://api.sheety.co/6ad185981dcd170af6b5519eaf363953/myTrackingData/workouts"
for exercise in exercises['exercises']:
    input_data = {
        'workout': {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
check = requests.post(sheety, json=input_data)
print(check.text)
