# -*- coding: utf-8 -*-
import common

class Video:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = message.text.lstrip('/video').strip()
        
        data = common.bing_search(text,'Video',1)
        self.api.send_message(message.chat.id,data[0]['MediaUrl'])
            
    

def main(bot,api):
    return Video(bot,api)