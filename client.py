from threading import Thread
from socket import *
import threading
from time import sleep
from random import randrange
import sys

class Client(Thread): 
    def __init__(self, serverName, serverPort):
        super(Client, self).__init__()
        self.serverName = serverName
        self.serverPort = serverPort

        self.genericMessage = "Message from Thread: " + str(threading.get_native_id())
        self.stopServerMessage = "BASTA"

    def create_sentence(self):
        if randrange(0, 999) < 995:
            return self.genericMessage
        return self.stopServerMessage
    
    def run(self):
        while 1:
            try:
                self.clientSocket = socket(AF_INET, SOCK_STREAM) # TCP
                #self.clientSocket = socket(AF_INET, SOCK_DGRAM) # UDP
                self.clientSocket.connect((self.serverName, self.serverPort))

                self.clientSocket.makefile("w").writelines( self.create_sentence() + "\n")
                responseMessage = self.clientSocket.makefile().readline()

                #Risposta dal server
                print("[INFO] - ", responseMessage)
                sleep(randrange(1,5))

                self.clientSocket.close()
            except:
                print("[CLIENT] - Connection Refused!")
                sys.exit()
