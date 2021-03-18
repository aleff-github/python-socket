from socket import *
from threading import Thread
import sys

class Server(Thread): 
    def __init__(self, serverName, serverPort, aviableConnections):
        super(Server, self).__init__()
        self.serverName = serverName
        self.serverPort = serverPort
        self.aviableConnections = aviableConnections
        self.serverON = True
        self.iteraction = 0
    
    def run(self):
        welcomeSocket = socket()
        welcomeSocket.bind( ( self.serverName, self.serverPort ) )
        welcomeSocket.listen( self.aviableConnections )
        print("++++++++++++++++++++++++++")
        print("[SERVER] - LISTEN")
        print("+ + SERVER PORT: ", self.serverPort)
        print("+ + AVIABLE CONNECTIONS: ", self.aviableConnections)
        print("++++++++++++++++++++++++++")

        while self.serverON:
            connectionSocket, addr = welcomeSocket.accept()
            print(self.iteraction)
            self.iteraction += 1

            print("[SERVER] - [FROM] -> ", addr)
            clientSentence = connectionSocket.makefile().readline()
            print("[MESSAGE] -> ", clientSentence)
            
            if clientSentence == "BASTA\n":
                print("[SERVER] - Stopping...")
                connectionSocket.close()
                welcomeSocket.close()
                self.serverON = False
                sys.exit()

            responseMessage = "Message received correctly!"
            connectionSocket.makefile("w").writelines(responseMessage)
            
            connectionSocket.close()
            pass