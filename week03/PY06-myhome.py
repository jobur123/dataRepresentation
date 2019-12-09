# week 03 lab webscraping
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
# with open("../carviewer2.html") as fp:
soup = BeautifulSoup(page.content, 'html.parser')
#print (soup.prettify())

home_file = open('week03MyHome.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


listings = soup.find_all("div", class_="PropertyListingCard")

for listing in listings:
  entryList = []
  price = listing.find(class_="PropertyListingCard__Price").text
  entryList.append(price)
  address = listing.find(class_="PropertyListingCard__Address").text
  entryList.append(address)


#print(price)
#print(address)



# rows = soup.find_all("tr")
# for row in rows:
#   dataList = []
#   cols = row.find_all("td")
#   for col in cols:
#     if ("Update" not in col.text) and ("Delete" not in col.text):
#       dataList.append(col.text)
#       print(dataList)
  home_writer.writerow(entryList)
home_file.close()