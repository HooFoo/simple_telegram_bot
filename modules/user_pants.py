# -*- coding: utf-8 -*-
class Pants:
    
    def __init__(self,bot):
        self.bot = bot;
        
    def listener(self,message):
        text = message.text.lstrip('/pants')
        
        if ' > ' in text:
            text, prefix = text.split(' > ', 1)
            if not prefix.startswith('@') and prefix:
                prefix = '@' + prefix
            if '_' in prefix:
                prefix='`'+prefix+'`'
        print(prefix)
        text = prefix+", у тебя в штанах *".decode("utf-8")+text.strip().upper()+"*!"
        if text:
            self.bot.send_message(message.chat.id,text, parse_mode='Markdown')

def main(bot):
    return Pants(bot)
