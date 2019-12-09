# lab week06 02 part 1
# https://html2pdf.app/
# https://developer.github.com/v3/guides/

import requests
import json

# read html page from a file and print it out
f = open("../carviewer2.html", "r")
html = f.read()
print (html)

# use api html2pdf
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'

url = 'https://api.html2pdf.app/v1/generate'
data={'html':html,'apiKey':apiKey}
response = requests.post(url,json=data)
print (response.status_code)

# create file and write response to it
newFile = open ("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write (response.content)
