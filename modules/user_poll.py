# -*- coding: utf-8 -*-
import common
import telebot

class Poll:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        self.currentPoll = ''
        self.results = {
            'ids':[]
            }
        
    def listener(self,message):
        if message.text.startswith('/'):
            self.start_poll(message)
        else:
            self.accept_result(message)
            
    def start_poll(self, message):
        text = message.text.lstrip('/poll').strip()
        if not text:
           self.api.send_message(message.chat.id,"Правильно писать так: \n/poll Тема\n * первый вариант \n * второй вариант");
           return
       
        answers = text.split('*')
        
        if answers[0] == 'results':
            self.show_results(message.chat.id)
            return
        
        currentPoll = answers[0].strip()
        answers = list(map(lambda s:s.strip(),answers[1:])) 
        if len(answers) < 2:
            self.api.send_message(message.chat.id,"Какое-то глупое голосование выходит.");
            return
        self.currentPoll = currentPoll
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        
        self.results = {'ids':[]}
        for answer in answers:
            self.results[answer] = 0
            keyboard.add(answer)

        self.api.send_message(message.chat.id,text="poll\n"+self.currentPoll,reply_markup=keyboard);
    
    def accept_result(self,message):
        if message.text not in self.results:
            return
        if message.from_user.id in self.results['ids']:
            self.api.send_message(message.chat.id,"Ты уже голосовал, отстань.");
        else:
            self.results['ids'].append(message.from_user.id)
            self.results[message.text]+=1
            self.show_results(message.chat.id)
    
    def show_results(self,chat_id):
        msg = "Результаты '%s': \n" % self.currentPoll
        for answer in self.results:
            if not answer=='ids':
                msg+= answer + ' - ' + str(self.results[answer]) +'\n'
        self.api.send_message(chat_id,msg);
        
def main(bot,api):
    return Poll(bot,api)
