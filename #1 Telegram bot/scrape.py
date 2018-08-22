from bs4 import BeautifulSoup
import random
import requests
import json
import os

# Request headers to avoid 403 Forbidden
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

link = 'https://knowyourmeme.com/memes/memes/photos/trending'

page_source = requests.get(link, headers=HEADERS).text
soup = BeautifulSoup(page_source, 'html.parser')

gallery = soup.find('div', {'id': 'photo_gallery'})
images = gallery.find_all('img')
links = [image['data-src'] for image in images]
hd_links = ['https://i.kym-cdn.com/photos/images/newsfeed/{}'.format('/'.join(links.split('/')[-4:])) for link in links]