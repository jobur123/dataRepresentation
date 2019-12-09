# week 6 lab 1 part 2 - create a car on the server by using api

import requests
import json

dataString = {'reg': '08 C 1234', 'make' : 'Ford', 'model' : 'Galaxy', 'price' : 1234}
url = 'http://127.0.0.1:5000/cars'

response = requests.post(url, json=dataString)

print (response.status_code)