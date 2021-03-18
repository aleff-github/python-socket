from os import system
from random import randrange
from server import Server
from client import Client

class God(object):
    def __init__(self):
        self.aviableConnections = 0
        self.clientNum = 0
        self.serverPort = 0
        self.serverName = ""
        self.TCPServer = None
        self.TCPClient = None

    def startServer(self):
        self.TCPServer = Server(serverName = self.serverName,
                                                serverPort = self.serverPort, 
                                                aviableConnections = self.aviableConnections)
        self.TCPServer.start()

    def startClient(self):
        self.TCPClient = Client(serverName = self.serverName,
                                                serverPort = self.serverPort)
        self.TCPClient.start()


system("clear")
god = God()

default = int(input("Do you want default settings? 1 for yes | 0 for no "))
if default == 1:
    god.aviableConnections = 5
    god.serverName = "192.168.1.9"
    god.serverPort = randrange(1000, 65530)
    god.clientNum = 100
else:
    god.aviableConnections = int(input("How many client do you want accept with the server? "))
    god.serverName = input("What is server address ?")
    god.serverPort = int(input("What is server port? "))
    god.clientNum = int(input("How many client do you want run?"))

try:
    god.startServer()
    for i in range(god.clientNum):
        god.startClient()
except:
    print("[ERROR] - Try/Catch main ")
