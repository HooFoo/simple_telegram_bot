class All:
    
    def __init__(self,bot):
        self.bot = bot;
        
    def listener(self,message):
        print(message);
        self.bot.send_message(message.chat.id, '@nikdem @dimasssik @lolligym @maaakso @HooFoo @ivanpopoloko @nastya_yeah @maxim_kozorez @savinov @ovaliko')

                

def main(bot):
    return All(bot)