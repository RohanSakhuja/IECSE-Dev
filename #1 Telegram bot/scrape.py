from bs4 import BeautifulSoup
import requests
import json
import os

# Check if memes folder exists
if not os.path.exists(os.path.join(os.getcwd(), 'memes')):
	os.makedirs(os.path.join(os.getcwd(), 'memes'))

# Request headers to avoid 403 Forbidden
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

link = 'https://knowyourmeme.com/memes/memes/photos/trending'

# Meme limit to download
limit = 1

page_source = requests.get(link, headers=HEADERS).text
soup = BeautifulSoup(page_source, 'html.parser')

gallery = soup.find('div', {'id': 'photo_gallery'})
images = gallery.find_all('img')

for image in images[:limit]:
	image_link = image['data-src']