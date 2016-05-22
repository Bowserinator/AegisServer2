import ssl, socket
from time import sleep

class Connection(object):
    def recv(self):
        self.part = ""
        self.data = ""
        while not self.part.endswith("\r\n"):
            self.part = self.ircsock.recv(2048)
            #part = part
            self.data += self.part
        self.data = self.data.splitlines()
        return self.data
    def __init__(self,server,port,SSL=True):
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if SSL:
            self.ircsock = ssl.wrap_socket(self.ircsock)
        self.ircsock.connect((server, port)) #SSL for secure connection :D
        sleep(3)
        self.ircsock.send("NICK {0}\r\n".format("AEGISSERVER2").encode('utf-8'))
        self.ircsock.send("USER {0} * * :Bowserinator's Bot.\r\n".format("AegisServer2").encode('utf-8'))

        
    def ping(self): 
        self.ircsock.send("PONG :pingis\n".encode('utf-8'))
    def partchan(self,chan):
        self.ircsock.send("PART {0}\n".format(chan).encode('utf-8'))
    def changenick(self,nick):
        self.ircsock.send("NICK {0}\n".format(nick).encode('utf-8'))
    def sendmsg(self,chan, msg):
        self.ircsock.send("PRIVMSG {0} :{1}\n".format(chan, msg))#.encode('utf-8'))
    def joinchan(self,chan):  
        self.ircsock.send("JOIN {0}\n".format(chan).encode('utf-8'))
    def action(self,channel,message):
        self.sendmsg(channel,"\x01ACTION " + message + "\x01")
    
    