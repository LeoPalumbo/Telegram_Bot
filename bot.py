import telepot

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        if txt == '/start' :
           bot.sendMessage(chat_id, '%s Welcome in my bot!'%name)
        else:
           print txt
TOKEN = '#YOUR_TOKEN_HERE'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)
print 'Listening ...'

import time
while 1:
    time.sleep(10)
