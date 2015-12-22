# -*- coding: utf-8 -*-
class Echo:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = message.text.lstrip('/echo')
        if text:
            self.api.send_message(message.chat.id,text)

def main(bot,api):
    return Echo(bot,api)
