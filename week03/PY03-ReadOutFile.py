# week 03 lab webscraping
#import requests
from bs4 import BeautifulSoup


# test we can read a file 
with open("../carviewer2.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')
  #first one only to get them all use for loop below
  #print (soup.tr)
  rows = soup.find_all("tr")
  for row in rows:
    print("----------")
    #print(soup.tr)
    #  for each row get the contents of TD
    # cols = row.find_all("td")
    # for col in cols:
    #   print(col.text)
    # modified to store text in a list
    dataList = []
    cols = row.find_all("td")
    for col in cols:
      dataList.append(col.text)
      print(dataList)
      #print(col.text)
