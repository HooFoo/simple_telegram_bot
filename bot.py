# -*- coding: utf-8 -*-
import config
import telebot
import time

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
        	if m.text == 'кек'.decode('utf-8'):
        		bot.send_message(m.chat.id, '@maaakso удали кека')
        	if m.text == 'не, эт не кек'.decode('utf-8'):
        	    
        		bot.send_message(m.chat.id, 'нет кек!!!')
        	if m.text == '/all':
        		bot.send_message(m.chat.id, '@nikdem @dimasssik @lolligym @maaakso @HooFoo @ivanpopoloko @nastya_yeah @maxim_kozorez @savinov @ovaliko')
        	if 'coub' in m.text:
        		bot.send_message(m.chat.id, 'иди работай!')
        	
        	if 'youtube' in m.text:
        		bot.send_message(m.chat.id, 'иди работай!')
            

if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)

