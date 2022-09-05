from pydoc import render_doc
from bs4 import BeautifulSoup
import requests
import lxml  
import json
# Site URL
url="https://merolagani.com/LatestMarket.aspx"

# make a Get request to fentch the raw HTML data
con = requests.get(url)
soup = BeautifulSoup(con.text,'lxml') #code of the page
table = soup.find('table', class_="table table-hover live-trading sortable") #table of data
headers = [i.text for i in table.find_all ('th')] #data of the th tag
# print(headers)
data = [j for j in table.find_all("tr", {"class" : ["decrease-row","increase-row","nochange-row"]})] #data inside the tr tag

# making in the formate of list like [{'name':'ADCL', 'LTP':'123'}]

result = [{headers[index]:cell.text for index,cell in enumerate(row.find_all ("td"))} for row in data]
print (result)

json_file = open('data/','Live Nepse Data.json','w')
json.dump(result,json_file)
json_file.close()
