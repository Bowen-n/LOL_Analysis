import requests
from bs4 import BeautifulSoup

url = 'https://www.op.gg/summoner/userName=%ED%9B%88%EB%A0%A8%EB%B3%91%EC%9D%B4%EC%83%81%ED%98%B8'
herohtml = requests.get(url).text
soup = BeautifulSoup(herohtml, 'lxml')

button = soup.find_all('a', class_='Button')
print(button)