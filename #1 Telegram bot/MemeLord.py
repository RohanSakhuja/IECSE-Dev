#from scrape import *
from flask import Flask, request, abort

app = Flask(__name__)

with open('TOKEN', 'r') as myfile:
    TOKEN=myfile.read().replace('\n', '')

def sendMessage(chat_id, msg):
	response = requests.post(
		url='https://api.telegram.org/bot{}/sendMessage'.format(TOKEN),
		data={'chat_id': chat_id, 'text': msg}
		).json()

def default_msg(chat_id):
	sendMessage(chat_id, 'Do /HitMe for Trending Memes!')

def MemeLord(content_type, chat_id, msg):

	if content_type == 'text':
		if message['text'] == '/Hitme':
			sendMessage(chat_id, message['text'])
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