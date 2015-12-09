# -*- coding: utf-8 -*-
class Echo:
    
    def __init__(self,bot):
        self.bot = bot;
        
    def listener(self,message):
        text = message.text.lstrip('/echo')
        if text:
            self.bot.send_message(message.chat.id,text)

def main(bot):
    return Echo(bot)
