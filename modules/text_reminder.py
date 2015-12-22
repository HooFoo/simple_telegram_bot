import common

class Reminder:
    
    def __init__(self,bot,api):
        self.bot = bot;
        self.api = api;
        
    def listener(self,message):
        """придумать"""
        #self.api.send_message(message.chat.id,message.sticker)
            
    

def main(bot,api):
    return Reminder(bot,api)