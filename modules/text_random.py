# -*- coding: utf-8 -*-
class Random:
    
    def __init__(self,bot):
        self.bot = bot;
        
    def listener(self,message):
            if message.content_type == 'text':
            	if message.text == 'кек'.decode('utf-8'):
            		self.bot.send_message(message.chat.id, '@maaakso удали кека')
            	if message.text == 'не, эт не кек'.decode('utf-8'):
            		self.bot.send_message(message.chat.id, 'нет кек!!!')
            	if message.text == '/all':
            		self.bot.send_message(message.chat.id, '@nikdem @dimasssik @lolligym @maaakso @HooFoo @ivanpopoloko @nastya_yeah @maxim_kozorez @savinov @ovaliko')
            	if 'coub' in message.text:
            		self.bot.send_message(message.chat.id, 'иди работай!')
            	
            	if 'youtube' in message.text:
            		self.bot.send_message(message.chat.id, 'иди работай!')
                

def main(bot):
    return Random(bot)