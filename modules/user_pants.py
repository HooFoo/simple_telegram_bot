# -*- coding: utf-8 -*-
class Pants:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = message.text.lstrip('/pants')
        
        if ' > ' in text:
            text, prefix = text.split(' > ', 1)
            if not prefix.startswith('@') and prefix:
                prefix = '@' + prefix
            if '_' in prefix:
                prefix='`'+prefix+'`'
        print(prefix)
        text = prefix+", у тебя в штанах *"+text.strip().upper()+"*!"
        if text:
            self.api.send_message(message.chat.id,text, parse_mode='Markdown')

def main(bot,api):
    return Pants(bot,api)
