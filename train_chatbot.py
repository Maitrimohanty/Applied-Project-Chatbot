#Maitri Mohanty ASU CSE Applied Project 
# Chatbot

from chatterbot import ChatBot as cb
from chatterbot.trainers import ListTrainer as lt
import os

def setup():
    chatbot = cb('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/pratu/Desktop/Chatbot/data/'):
        convData = open(r'C:/Users/pratu/Desktop/Chatbot/data/' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(lt)
        chatbot.train(convData)
        #print("Training has been completed")
    

setup()