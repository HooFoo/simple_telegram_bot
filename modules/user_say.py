# -*- coding: utf-8 -*-
import os
class Say:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = message.text.lstrip('/say')

        if len(text)>1024:
            self.api.send_message(message.chat.id, "Привет, ты что, охуел?")
        elif "pv zk" in text:
            self.api.send_message(message.chat.id, "@{0}, а не пошел бы ты нахуй?".format(message.from_user.username))
        else:
            self.api.send_voice(message.chat.id, self.make_auidio(text))
            os.system('rm /tmp/tmp.ogg')
    
    def make_auidio(self,text):
        #os.system('export $(dbus-launch)')
        os.system('echo %(text)s | RHVoice-client -s Irina > /tmp/tmp.wav' % {'text':self.process_text(text)})
        os.system('sox /tmp/tmp.wav /tmp/tmp.ogg')
        os.system('rm /tmp/tmp.wav')
        return open('/tmp/tmp.ogg','rb')
    
    def process_text(self,text):
        text = text.replace("'", ' ')
        text = text.replace('"', ' ')
        text = text.replace('|', ' ')
        text = text.replace('\n', ' ')
        return text
        
def main(bot,api):
    return Say(bot,api)
