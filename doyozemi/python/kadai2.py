import requests
from bs4 import BeautifulSoup

#相鉄線の運行状況のURL
soutetu_URL = 'https://transit.yahoo.co.jp/diainfo/125/0'

#Requestsを利用してWebページを取得する
soutetu_URL_Requests = requests.get(soutetu_URL)

# BeautifulSoupを利用してWebページを解析する
soutetu_URL_Soup = BeautifulSoup(soutetu_URL_Requests.text, 'html.parser')

#.findでtroubleクラスのddタグを探す
if soutetu_URL_Soup.find('dd',class_='trouble'):
    message = '相鉄線は遅延しています'
else:
    message = '相鉄線は通常運転です'

print(message)
