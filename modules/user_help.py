# -*- coding: utf-8 -*-
class Help:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        text = "Доступные команды: \n"
        cmds = self.bot.get_commands()
        for group in cmds:
            if not group == 'owner':
                if len(cmds[group]) > 0:
                    text+= "- Тип %s \n" % group
                    for cmd in cmds[group]:
                        text+="--- %s \n" % cmds[group][cmd].__class__.__name__.lower()
        if text:
            self.api.send_message(message.chat.id,text)

def main(bot,api):
    return Help(bot,api)
