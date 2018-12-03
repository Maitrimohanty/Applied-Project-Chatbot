#Maitri Mohanty ASU CSE Applied Project 
# Chatbot

from SimpleWebSocketServer import SimpleWebSocketServer as sws
from SimpleWebSocketServer import WebSocket as wb
from chatbot import get_response


class ChatServer(wb):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        response = get_response(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = sws('', 8000, ChatServer)
server.serveforever()
