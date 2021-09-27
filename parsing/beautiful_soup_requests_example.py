import requests
from bs4 import BeautifulSoup

url = 'https://librebook.me/rebirth_of_the_thief_who_roamed_the_world/vol1/1189'
response2 = requests.get(url)
soup = BeautifulSoup(response2.text, 'lxml')

print(soup)