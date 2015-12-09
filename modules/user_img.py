# -*- coding: utf-8 -*-
import common

class Img:
    
    def __init__(self,bot):
        self.bot = bot;
        
    def listener(self,message):
        text = message.text.lstrip('/img').strip()
        
        data = common.bing_search(text,'Image',1)

        #if text:
        self.bot.send_message(message.chat.id,data[0]['MediaUrl'])
            
    

def main(bot):
    return Img(bot)
