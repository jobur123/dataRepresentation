# week 6 lecture DR
import requests as rq 
# url = 'https://www.gmit.ie'

# response = rq.get(url)

# print(response.status_code, response.text)

url = 'http://127.0.0.1:5000/cars'
data = {'reg':'123', 'make':'blablalba', 'model':'dumdumdumd', 'price':1}

response = rq.post(url, json=data)
print(response.status_code)
print(response.json())