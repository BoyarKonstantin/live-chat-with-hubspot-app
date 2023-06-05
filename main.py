import json
import requests
import telebot
from requests.auth import HTTPBasicAuth
import re
from LiveChatApi import LiveChatApi

bot = telebot.TeleBot('6075598101:AAHKui1LDUrnWzGN8ytIvSpsxOlh0Bd21N4')

email = ''
name = ''

@bot.message_handler(commands=['start'])
def start(message): 
    email_message = 'Your email' 
    bot.send_message(message.chat.id, email_message, parse_mode = 'html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    global email, name
    if not email:
        email = message.text
        if not is_valid_email(email):
            error_message = 'Email is not correct, try again!'
            bot.send_message(message.chat.id, error_message, parse_mode='html')
        else:
            name_message = 'Your name' 
            bot.send_message(message.chat.id, name_message, parse_mode='html')
    elif not name:
        name = message.text
        start_chat(name, email) 

def is_valid_email(email): 
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
    



#bot.polling(none_stop=True)

if __name__ == "__main__":

    account_id = "d72aabe6-77b9-439d-b789-4cb04ccd6593"

    live_chat_token = "dal:3kfmrh8Drk814qWH-AqA3RCwxS0"
    live_chat_api = LiveChatApi(token=live_chat_token)

    customer_id = live_chat_api.post_customer(live_chat_token,
                                               "Kostiantyn", 
                                               "kostya20041234@gmail.com", 
                                               account_id=account_id)
    
    live_chat_api.create_chat(live_chat_token, account_id,
                               customer_id=customer_id, agent_id=account_id)

    #get_agent_id(live_chat_token, 'Kostiantyn Boiar')
