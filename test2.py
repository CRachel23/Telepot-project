import sys
import time
import random
import datetime
import telepot

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	#print 'Got command: %s' % command

	if command == 'command1':
	  bot.sendMessage(chat_id="449959530", text='Hello')
	elif command == 'command2':
	  bot.sendMessage(chat_id="449959530", text='Im cute')
	elif command == 'photo':
	  bot.sendPhoto(chat_id="449959530", photo=('https://i.guim.co.uk/img/media/fe1e34da640c5c56ed16f76ce6f994fa9343d09d/0_174_3408_2046/master/3408.jpg?width=620&quality=85&dpr=1&s=none'))

bot = telepot.Bot("5617446728:AAG7DQL3IQG1H1dMoHvYWqEM7K9sPmCK7yw")
bot.message_loop(handle)

while 1:
	time.sleep(10)