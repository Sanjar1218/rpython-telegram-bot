from lib2to3.pgen2 import token
import telegram
import os
TOKEN = os.environ['token']
bot = telegram.Bot(token=TOKEN)


last_id = -1
while True:
    updates = bot.getUpdates()
    update = updates[-1]
    current_id = update.update_id
    chat_id = update.message.chat.id
    text= update.message.text
    if last_id!=current_id:
        last_id=current_id
        bot.sendMessage(chat_id, text)