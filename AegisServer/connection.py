import socket, ssl
import socks, time, datetime

class Connection(object):
    def __init__(self,server,port,SSL=True):
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if SSL: 
            self.ircsock = ssl.wrap_socket(self.ircsock)
        self.ircsock.connect((server, port)) #SSL for secure connection :D
        self.ircsock.send("USER {0} * * :Bowserinator's Bot.\r\n".format("AegisServer2").encode('utf-8'))

    def notice(self, user, message):
        self.ircsock.send("NOTICE {} :{}".format(user, message))
    def ctcp(self, user, message):
        self.ircsock.send("PRIVMSG {} :\x01{}\x01\x01".format(user, message))
    def ping(self): 
        self.ircsock.send("PONG :pingis\n".encode('utf-8'))
    def partchan(self,chan):
        self.ircsock.send("PART {0}\n".format(chan).encode('utf-8'))
    def changenick(self,nick):
        self.ircsock.send("NICK {0}\n".format(nick).encode('utf-8'))
        
    def sendmsg(self,chan, msg):
        n = 340; msg=str(msg)
        msg = [msg[i:i+n] for i in range(0, len(msg), n)]
        for m in msg:
            print ("[SEND] [{0}]: [{1}] {2}".format(datetime.datetime.now(),chan,m))
            self.ircsock.send("PRIVMSG {0} :{1}\n".format(chan, m))#.encode('utf-8'))
            time.sleep(0.7)
   
    def joinchan(self,chan):  
        self.ircsock.send("JOIN {0}\n".format(chan).encode('utf-8'))
    def action(self,channel,message):
        self.sendmsg(channel,"\x01ACTION " + message + "\x01")
        
    def kickuser(self,channel,user,message):
        user = user.replace(" ","").replace(":","")
        self.ircsock.send("KICK " + channel + " " + user+ " :" + message +"\r\n")
    def opnick(self,channel,nick):
        self.ircsock.send("MODE {0} +o {1}\n".format(channel,nick).encode('utf-8'))
    def deopnick(self,channel,nick):
        self.ircsock.send("MODE {0} -o {1}\n".format(channel,nick).encode('utf-8'))
    def ban(self,channel,nick):
        self.ircsock.send("MODE {0} +b {1}\n".format(channel,nick).encode('utf-8'))
    def unban(self,channel,nick):
        self.ircsock.send("MODE {0} -b {1}\n".format(channel,nick).encode('utf-8'))
    def stab(self,channel,nick):
        self.ircsock.send("MODE {0} +q {1}\n".format(channel,nick).encode('utf-8'))
    def unstab(self,channel,nick):
        self.ircsock.send("MODE {0} -q {1}\n".format(channel,nick).encode('utf-8'))
    def unvoice(self,channel,nick):
        self.ircsock.send("MODE {0} -v {1}\n".format(channel,nick).encode('utf-8'))
    def voice(self,channel,nick):
        self.ircsock.send("MODE {0} +v {1}\n".format(channel,nick).encode('utf-8'))
    def setMode(self,channel,nick,mode):
        self.ircsock.send("MODE {0} {1} {2}\n".format(channel,mode,nick).encode('utf-8'))
        
    
    def whois(self,user):  
        self.ircsock.send("WHOIS {0}\n".format(user).encode('utf-8'))
        
    def quit(self,message):
        self.ircsock.send("QUIT :{0}\n".format(message).encode('utf-8'))