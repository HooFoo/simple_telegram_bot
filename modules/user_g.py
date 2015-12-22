# -*- coding: utf-8 -*-
import common

class G:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = message.text.lstrip('/g').strip()
        
        data = common.bing_search(text,'Web',1)

        self.api.send_message(message.chat.id,data[0]['Url'])
            
    

def main(bot,api):
    return G(bot,api)
