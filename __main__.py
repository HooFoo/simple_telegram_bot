import config
import bot
import sys
import time
from retrying import retry

@retry
def main():
    try:
        print('Starting bot')
        myBot = bot.Bot(config.token)
    except Exception as ex:
        print(str(ex))

main()