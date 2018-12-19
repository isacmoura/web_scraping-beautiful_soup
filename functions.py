import requests
from bs4 import BeautifulSoup
from pprint import pprint

class Blog:
    
    def __init__(self, title, posts):
        self.title = title
        self.posts = posts or []
    
    def add_posts(self, post):
        self.posts.append(post)

def get_content(url):
    try:
        r = requests.get(url, allow_redirects = True)
        r.raise_for_status()

        return BeautifulSoup(r.content, 'html.parser')
    except:
        return None

base_url = 'https://rafaelmarques.mobi'
current_page = 1

bs = get_content(base_url)

blog = Blog(bs.title.string, [])

while bs is not None:

    content_box = bs.find('div', {'id': 'content_box'})
    articles = content_box.find_all('article', class_='latestPost')
    
    for article in articles:
        title = article.find('span', class_='p-name')
        if not title:
            continue
        
        url = article.find('a')['href']
        excerpt = article.find('div', class_='front-view-content')
        blog.add_posts({
            'title': title.get_text(),
            'url': url,
            'excerpt': excerpt.get_text()
        })

    current_page += 1
    print('Going to page: ' + str(current_page)) 
    bs = get_content(f'{base_url}/page/{current_page}')

print(blog.title)
pprint(blog.posts)