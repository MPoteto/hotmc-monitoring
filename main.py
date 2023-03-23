import requests
from bs4 import BeautifulSoup
import datetime

from config import url, webhook, timeout

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find('div', class_='place-rating')
q=quotes.find('span')
q=q.text.replace(' ', '')
q=q.replace('\n', '')

old=q+f"/{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"


while True:
    import time
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='place-rating')
    q=quotes.find('span')
    q=q.text.replace(' ', '')
    q=q.replace('\n', '')
    if old.split('/')[0] != q:
        status=""
        if old < q:
            status = "📈"
        if old > q:
            status = "📉"
        
        requests.post(webhook, data={'content': f'🔥 @everyone !! Изменение рейтинга!\n\n🧂 Статус: {status}\n👴 До: `{old.split("/")[0]}` ({old.split("/")[1]})\n🧑 После: `{q}` ({datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second})\n\n📎 Ссылка: `{url}`'})
        old=q+f"/{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    
    time.sleep(int(timeout))
