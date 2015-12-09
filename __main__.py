import config
import bot
import sys
import time


if __name__ == '__main__':
     myBot = bot.Bot(config.token)
     while True:
        a = input()
        if a:
            myBot.send(55142102,a)
        time.sleep(100)
