import datetime


#INPUT CLASS
#Tyoes; PRIVMSG, JOIN, PART, QUIT, MODE, INVITE, KICK, PING, NOTICE, TOPIC ERROR

#ERROR :Closing Link: 187.114.148.146.bc.googleusercontent.com (Connection timed out)
#:HAL9000!ircbot@botters/IndigoTiger/bot/IndigoBot MODE ##BWBellairs-bots -q *!*@botters/BWBellairs
#:Andromeda-dev!~Andromeda@unaffiliated/bwbellairs/bot/bwbllairstest QUIT :Quit: Ctrl-C at console.
#:Bowserinator!~Bowserina@unaffiliated/bowserinator PART ##BWBellairs-bots :"test quit message"
#:Bowserinator!~Bowserina@unaffiliated/bowserinator KICK ##BWBellairs-bots AegisServer :test
#:Bowserinator!~Bowserina@unaffiliated/bowserinator INVITE AegisServerAlpha :#ezzybot
#:Bowserinator!~Bowserina@unaffiliated/bowserinator TOPIC ##BWBellairs-bots :Welcome to ##BWBellairs bot testing channel | Command Chars: *BWBellairs[Bot], @AegisServer, .DZBot, ?!IovoidBot ,NeoFrog, !HAL9000 (poke IndigoTiger for access), `>JeDaBot | Free AKICK for anyone who causes us to use RECOVER | We survived 1 netsplits without takeovers | Currently 5 days since last takeover

class Input(object):
    def __init__(self,printType="raw"):
        self.printType = printType #Types: raw, IRC Client, Neatly formatted
        
    def phrase(self,message):
        split = message.split(" ")
        returned = {}
        if split[1] == "PRIVMSG":
            returned["type"] = "PRIVMSG"
            returned["user"] = split[0]
            returned["channel"] = split[2]
            returned["message"] = message.split(" :",1)[1]
        elif split[1] == "TOPIC":
            returned["type"] = "TOPIC"
            returned["user"] = split[0]
            returned["channel"] = split[2]
            returned["message"] = message.split(" :",1)[1]
        elif split[1] == "INVITE":
            returned["type"] = "INVITE"
            returned["user"] = split[0]
            returned["channel"] = message.split(" :",1)[1] #Channel invited to
            returned["message"] = None
        elif split[1] == "QUIT":
            returned["type"] = "QUIT"
            returned["user"] = split[0]
            returned["channel"] = None
            try: returned["message"] = message.split(" :",1)[1] #Quit message
            except: returned["message"] = ""
        elif split[0] == "PING":
            returned["type"] = "PING"
            returned["user"] = None
            returned["channel"] = None
            returned["message"] = None
        elif split[1] == "MODE":
            returned["type"] = "MODE"
            returned["user"] = split[0] #USER SETTING THE MODE
            returned["channel"] = split[2]
            returned["message"] = message.split(split[2] + " ",1)[1]
        elif split[1] == "JOIN":
            returned["type"] = "JOIN"
            returned["user"] = split[0] 
            returned["channel"] = split[2]
            returned["message"] = None
        elif split[1] == "PART":
            returned["type"] = "PART"
            returned["user"] = split[0]
            returned["channel"] = split[2]
            try: returned["message"] = message.split(" :",1)[1] #Quit message
            except: returned["message"] = ""
        elif split[1] == "KICK":
            returned["type"] = "KICK"
            returned["user"] = split[0] #User kicking
            returned["channel"] = split[2]
            returned["userkicked"] = split[3]
            try: returned["message"] = message.split(" :",1)[1] #Kick message
            except: returned["message"] = ""
        else:
            returned["type"] = split[1]
            returned["channel"] = None
            returned["message"] = None
            returned["user"] = None
        returned["raw"] = message

            
        printMsg = message
        if self.printType == "raw":
            printMsg = "[RECV] " + printMsg
        elif self.printType == "client":
            printMsg = "[RECV] [{0}]: {1}".format(str(datetime.datetime.now()), returned["raw"].encode('utf8'))
        
        print printMsg
        return returned

#Output class
#TODO :Timed outputs, ie 5 min. Immediete outputs in 1 array, timed in other. Timed ones are saved
#If output array len too large stop outputting for 5 seconds.
#Also prints output

#Logging class: Logs based on input/output classes
class Output(object):
    def __init__(self,printType="client"):
        self.printType = printType
        self.messageQueue = []
    
    def addMessage(self,channel,message):
        self.messageQueue.append([channel,message])
    
    def run(self,ircsock):
        try:
            for i in range(0,4):
                if len(self.messageQueue)>0:
                    printMsg = self.messageQueue[0][1]
                    if self.printType == "raw":
                        printMsg = "[SEND] " + printMsg
                    elif self.printType == "client":
                        printMsg = "[SEND] [{0}]: {1}".format(str(datetime.datetime.now()), printMsg.encode('utf8'))
            
                    ircsock.sendmsg(self.messageQueue[0][0], self.messageQueue[0][1])
                    print printMsg
                    del self.messageQueue[0]
        except Exception as e: pass