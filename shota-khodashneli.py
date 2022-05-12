import requests
import json
API_key="907c3c87c332d3c6181267fa616f3a00"
country=input("შეიყვანეთ თქვენი ქვეყანა")
city=input("შეიყვანეთ თქვენი ქალაქი")
url = f'https://pro.openweathermap.org/data/2.5/forecast/climate?q={country},{city}&appid={API_key}'
req = requests.get(url)
print(req)
print(req.headers)
print(req.status_code)
print(req.text)
print(req.headers['Content-Type'])
result_json = req.text
res = json.loads(result_json)
res_python= json.dumps(res, indent=4)
print(res_python)
info=res['temp']
night=info["night"]
print("night:" + night)
