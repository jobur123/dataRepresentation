# week 03 lab webscraping
from bs4 import BeautifulSoup
import csv

with open("../carviewer2.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')

employee_file = open('employee_file.csv', mode = 'w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.find_all("tr")
for row in rows:
  dataList = []
  cols = row.find_all("td")
  for col in cols:
    if ("Update" not in col.text) and ("Delete" not in col.text):
      dataList.append(col.text)
      print(dataList)
  employee_writer.writerow(dataList)

employee_file.close()