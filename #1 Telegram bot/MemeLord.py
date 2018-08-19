#from scrape import *
import time
import json
import requests
from flask import Flask, request, abort

app = Flask(__name__)

#with open('TOKEN', 'r') as myfile:
#    TOKEN=myfile.read().replace('\n', '')

TOKEN = '690843027:AAGlJTnrqa385D75rvoDqrdT0bvUKAZNXBg'
url = 'https://i.kym-cdn.com/photos/images/newsfeed/001/217/729/f9a.jpg'

def sendPhoto(chat_id):
	response = requests.post(
		url='https://api.telegram.org/bot{}/sendPhoto'.format(TOKEN),
		data={'chat_id': chat_id, 'photo': url}
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
		print('$',chat_id)

		MemeLord('text', chat_id, message)

		dataDict = json.dumps(data)
		print("#####")
		print("JSON: ",dataDict)
		print("#####")
		with open('out.txt', 'w') as output:
			output.write(dataDict)
	
	return 'MemeLord Online'

if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port='8443',
		debug=True)