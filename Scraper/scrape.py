from bs4 import BeautifulSoup
import requests
import json
import os

if not os.path.exists(os.path.join(os.getcwd(), 'memes')):
	os.makedirs(os.path.join(os.getcwd(), 'memes'))

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

link = 'https://knowyourmeme.com/memes/memes/photos/trending'

limit = 3
high_def = True

page_source = requests.get(link, headers=HEADERS).text
soup = BeautifulSoup(page_source, 'html.parser')

gallery = soup.find('div', {'id': 'photo_gallery'})
images = gallery.find_all('img')

meme_details = []

for image in images[:limit]:
	image_link = image['data-src']
	image_desc = image['alt']
	image_identifier = '/'.join(image_link.split('/')[-4:])
	file_name = image_link.split('/')[-1]

	if high_def == True:
		image_link = 'https://i.kym-cdn.com/photos/images/newsfeed/{id}'.format(id=image_identifier)

	r = requests.get(image_link)
	print('Downloading: {link}'.format(link=image_link))

	with open('memes/{name}'.format(name=file_name), 'wb') as f:
		f.write(r.content)

	meme_details.append({
		'file_name': file_name,
		'description': image_desc
	})

with open('memes/file_data.json', 'w') as f:
	json.dump(meme_details, f, indent=2)
