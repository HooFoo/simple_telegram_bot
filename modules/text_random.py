# -*- coding: utf-8 -*-
import common

class Random:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        if message.content_type == 'text':
        	if message.text == 'кек':
        		self.api.send_message(message.chat.id, '@maaakso удали кека')
        	if message.text == 'не, эт не кек':
        		self.api.send_message(message.chat.id, 'нет кек!!!')
        	if 'coub' in message.text:
        		self.api.send_message(message.chat.id, 'иди работай!')
        	if 'youtube' in message.text:
        		self.api.send_message(message.chat.id, 'иди работай!')
        #self.say_random_word(message.chat.id)		
   
    def say_random_word(self,chat_id):
        if common.dice(24)>22:
            self.api.send_message(chat_id,"кек") 

def main(bot,api):
    return Random(bot,api)