from scrape import *
from flask import Flask, request, abort

app = Flask(__name__)

TOKEN = os.environ.get("MEMELORD_TOKEN")

def sendMessage(chat_id, msg):
	response = requests.post(
		url='https://api.telegram.org/bot{}/sendMessage'.format(TOKEN),
		data={'chat_id': chat_id, 'text': msg}
		).json()

def sendPhoto(chat_id):
	image_link = random.choice(hd_links)
	response = requests.post(
		url='https://api.telegram.org/bot{}/sendPhoto'.format(TOKEN),
		data={'chat_id': chat_id, 'photo': image_link}
		).json()

def default_msg(chat_id):
	sendMessage(chat_id, 'Do /HitMe for Trending Memes!')

def MemeLord(content_type, chat_id, msg):

	if content_type == 'text':
		if msg['text'] == '/HitMe':
			sendPhoto(chat_id)
		else:
			default_msg(chat_id)

@app.route('/{}'.format(TOKEN), methods=['GET', 'POST'])
def main():

	if request.method == 'POST': 
		data = request.get_json(force=True)
		chat_id = data['message']['chat']['id']
		message = data['message']

		MemeLord('text', chat_id, message)
	
	return 'MemeLord Online'

if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port='8443',
		debug=True)