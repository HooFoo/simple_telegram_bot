# -*- coding: utf-8 -*-

import os
import telebot
import time
import logging
import imp
import config
import sys, traceback


from os import listdir
from os.path import isfile, join

class Bot:
        
    def __init__(self,token):
        self.bot = telebot.TeleBot(token)
        self.load()
        self.bot.set_update_listener(self.process)
        self.bot.polling(none_stop=True)

                
    def load(self):
        """
        load
        Load all modules.
        See also: modprobe, rmmod, lsmod
        """

        self.commands = {
            # Usual text commands (e.g. "/echo 123")
            'user': {},
            'owner': {
                'load': self.load,
                'modprobe': self.modprobe,
                'rmmod': self.rmmod
            },
            # Modules for bot's reaction to a different message types
            'text': {},
            'photo': {},
            'audio': {},
            'video': {},
            'sticker': {},
            'voice': {}
        }

        for file in os.listdir('modules'):
            if file.endswith('.py'):
                command_type, command = file.split('_', 1)
                self.modprobe(self, command[:-3])


    def modprobe(self, bot, *args):
        """
        modprobe <module>
        Load module.
        See also: load, rmmod, lsmod
        """

        if len(args) != 1:
            return

        found_module = None
        for command_type in self.commands:
            name = 'modules/{}_{}'.format(command_type, args[0])
            try:
                found_module = imp.find_module(name)
            except ImportError:
                continue
            else:
                break

        if found_module is None:
            error = 'MODULE: {} not found'.format(args[0])
            logging.error(error)
            return error

        try:
            module = imp.load_module(name, *found_module).main(self,self.bot)
        except Exception as e:
            error = "MODULE: Can't load {}".format(args[0])
            logging.error(error)
            logging.error(e)
            return error
        else:
            self.commands[command_type][args[0]] = module

        info = 'MODULE: {} loaded'.format(args[0])
        logging.info(info)
        return info

    def rmmod(self, bot, *args):
        """
        rmmod <module>
        Remove module.
        See also: load, modprobe, lsmod
        """

        if len(args) != 1:
            return

        if args[0] in ('load', 'modprobe', 'rmmod'):
            return "MODULE: can't remove {0}".format(args[0])

        found = False
        for command_type in self.commands:
            if args[0] in self.commands[command_type]:
                del self.commands[command_type][args[0]]
                found = True
                break

        if not found:
            return 'MODULE: {} not loaded'.format(args[0])

        info = 'MODULE: {} removed'.format(args[0])
        logging.info(info)
        return info
        
    def process(self, messages):
        """
        Process an update
        """
        
        for m in messages:
            try:

                if m.content_type=='text':
                    
                    print("("+str(m.chat.id)+") "+str(m.chat.username)+': '+m.text)
                    if hasattr(m,'reply_to_message'):
                        # а вот тут проверяем не является ли сообщение ответом,
                        # если там есть команда, то работаем с ней
                        rmessage = m.reply_to_message
                        cmd = rmessage.text.split('\n')[0];
                                
                    if m.text.startswith('/') or 'cmd' in locals():
                        text = m.text.lstrip('/')
                        error = False
            

                        if not text: return
                        if not 'cmd' in locals():
                            cmd = text.split(' ')[0];

                        if cmd in self.commands['user'] or (cmd in self.commands['owner'] and self._is_owner(m)):
                            command_type = 'user' if cmd in self.commands['user'] else 'owner'
                            try:
                                cmd_main = self.commands[command_type][cmd]
                                result = cmd_main.listener(m)
                            except TypeError as e:
                                if 'positional argument' in str(e):
                                    result = 'wrong parameters'
                                    error = True
                                else:
                                    raise
                    else:
                        for cmd in self.commands[m.content_type]:
                            self.commands[m.content_type][cmd].listener(m)
                else:
                    print("("+str(m.chat.id)+") "+str(m.chat.username)+': '+m.content_type)
                    for cmd in self.commands[m.content_type]:
                        self.commands[m.content_type][cmd].listener(m)
            except Exception as ex:
                print(str(ex))
                traceback.print_exc(file=sys.stdout)
                #self.send(m.chat.id,'Что-то поломалось: '.decode('utf-8')+str(ex))
        
    def _is_owner(self, update):
        return update['from']['username'] == config.owner

    def _get_chat_id(self, update):
        return update.chat.id
        
    def send(self,chat_id, text):
        self.bot.send_message(chat_id,text)
        
    def get_commands(self):
        return self.commands