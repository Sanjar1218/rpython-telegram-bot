from lib2to3.pgen2 import token
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
TOKEN = os.environ['token']
bot = telegram.Bot(token=TOKEN)
updates = bot.getUpdates()
update = updates[-1]
chat_id = update.message.chat.id

text= update.message.text
keyboard = KeyboardButton('text')
reply_markup = ReplyKeyboardMarkup(
    [[keyboard]],
    resize_keyboard=True
)
bot.sendMessage(chat_id, text, reply_markup=reply_markup)

# last_id = -1
# while True:
#     #gets all updates
#     updates = bot.getUpdates()
#     #last updates object
#     update = updates[-1]
#     #current user update_id
#     current_id = update.update_id
#     #user id
#     chat_id = update.message.chat.id
#     #text user sended
#     text= update.message.text
#     #checks it'snot last id used
#     if last_id!=current_id:
#         #storese current_id
#         last_id=current_id
#         #sendMessage
#         bot.sendMessage(chat_id, text)