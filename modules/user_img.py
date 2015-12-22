# -*- coding: utf-8 -*-
import common

class Img:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        self.counter = 1
        self.last = ''
        
    def listener(self,message):
        text = message.text.lstrip('/img').strip()
        if not text:
            self.counter+=1
            text = self.last
        else:
            self.counter=1
        self.last = text
        data = common.bing_search(text,'Image',self.counter)

        #if text:
        self.api.send_message(message.chat.id,data[self.counter-1]['MediaUrl'])
            
    

def main(bot,api):
    return Img(bot,api)
