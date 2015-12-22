class All:
    
    def __init__(self,bot,api):
        self.bot = bot; 
        self.api = api;
        
    def listener(self,message):
        self.api.send_message(message.chat.id, '@nikdem @dimasssik @lolligym @maaakso @HooFoo @ivanpopoloko @nastya_yeah @maxim_kozorez @savinov @ovaliko')

                

def main(bot,api):
    return All(bot,api)