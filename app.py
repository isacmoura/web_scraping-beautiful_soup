import requests
from bs4 import BeautifulSoup

r = requests.get('https://rafaelmarques.mobi')
bs = BeautifulSoup(r.content, 'html.parser')

print(f'O título do site é: {bs.title.string}')

content_box = bs.find('div', {'id': 'content_box'})
articles = content_box.findAll('article', class_ = 'latestPost')

for article in articles:
    title = article.find('span', class_ = 'p-name')
    if not title:
        continue
    
    url = article.find('a')['href']
    excerpt = article.find('div', class_ = 'front-view-content')

    print(f'{title.getText()}: {url}')
    print(f'Excerpt: {excerpt.getText()}\n')