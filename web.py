#import requests libs
import requests
from bs4 import BeautifulSoup
import csv

# url to the page to scrap
url="http://example.com"

# send a get request to the erver
response = requests.get(url)

# print the scrap data
if response.status_code == 200:
  soup = BeautifulSoup(response.content, 'html.parser')

  # Extract text from the parsed HTML
  heading = soup.title.string
  phara=soup.p.string
  atag=soup.a.string

  # can get the defining tag included data using the array
  ptag=soup.find_all(['p','h1'])

  for p in ptag:
      print(p.string)

  # print("This is title tag content:"+heading)
  # print("This is anchor tag content:"+atag)

else:
    print("error")

