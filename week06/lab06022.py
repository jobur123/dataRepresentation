# lab wk 6 part 2 2
# get info from a private repos on my github
import requests
import json


# get infor from my github
apiKey = 'fdcba01d190e2a816c7468a196f5ff4cca3c1b01'
url = 'https://api.github.com/repos/jobur123/PaS-Project-Iris-Dataset'
filename ="repo.json"

# assign response
response = requests.get(url, auth=('token',apiKey))

# format to json
repoJSON = response.json()

#print (response.json())

# create and write to json file
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
