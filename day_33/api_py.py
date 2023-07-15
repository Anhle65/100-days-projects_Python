import requests

parameter = {
    "lat": -43.532055,
    "lng": 172.636230,
    "formatted": 1
}
rsp = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
data = rsp.json()["results"]['sunrise']
rsp.raise_for_status()
print(data)
# print(rsp.status_code)
