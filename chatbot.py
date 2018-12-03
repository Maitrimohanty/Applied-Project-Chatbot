#Maitri Mohanty ASU CSE Applied Project 
# Chatbot

from chatterbot import ChatBot as cb
from chatterbot.trainers import ListTrainer as lt


def get_response(usrText):
    bot = cb('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(lt)
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break
        if usrText.strip() == ' ':
            return('Please ask something, spaces is not a question')

        
