import requests
import json

url= "https://prodapi.metweb.ie/observations/athenry/today"
response = requests.get(url)
data = response.json()

# filename = 'athenryweather.json'
# f = open(filename, 'w')
# json.dump(data, f, indent=4)

for row in data:
  print(row["pressure"])
