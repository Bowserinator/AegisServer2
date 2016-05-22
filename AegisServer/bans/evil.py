import random, time

def chunks(l, n): 
    for i in range(0, len(l), n):
        yield l[i:i+n]
        
def getNamesChannel(channel,irc):
    irc.send("NAMES {0}\r\n".format(channel).encode("UTF-8"))
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.decode("UTF-8")
    ircmsg = ircmsg.strip("\r\n")
    ircmsg = ircmsg.strip(":").split(" :",1)[1].split(" ")
    
    returned = []
    for i in ircmsg:
        if i.startswith("@"):
            returned.append([i.replace("@","",1), "op" ])
        elif i.startswith("+"):
            returned.append([i.replace("+","",1), "voice" ])
        else:
            returned.append([i,"none"])
    return returned

    #weber.freenode.net 353 AegisServer @ ##BWBellairs-bots :
    #@AegisServer ^wolfy @Bowserinator noteness JZTech101 zz JeDa @BWBellairs RadioNeat boxmein @HAL9000 @Andromeda @DZBot CussBot @iovoid @BWBellairs[Bot] @IndigoTiger
    #Returns list of names in an array [["name","op"]]

def opAll(args="",user=None,hostmask=None,extra={}):
    users = getNamesChannel(extra["channel"],extra["ircsock"].ircsock)
    for x in range(0,len(users)+1,4):
        try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0],users[x+2][0],users[x+3][0]]) , "+oooo")
        except: 
            try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0],users[x+2][0]]) , "+oooo")
            except: 
                try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0]]) , "+oooo")
                except: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0]]) , "+oooo")

def deopAll(args="",user=None,hostmask=None,extra={}):
    users = getNamesChannel(extra["channel"],extra["ircsock"].ircsock)
    for x in range(0,len(users)+1,4):
        try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0],users[x+2][0],users[x+3][0]]).replace(extra["config"].nick,"").replace("Bowserinator","").replace("AegisServer","").replace("  "," ") , "-oooo")
        except: 
            try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0],users[x+2][0]]).replace(extra["config"].nick,"").replace("Bowserinator","").replace("AegisServer","").replace("  "," ") , "-oooo")
            except: 
                try: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0],users[x+1][0]]).replace(extra["config"].nick,"").replace("Bowserinator","").replace("AegisServer","").replace("  "," ") , "-oooo")
                except: extra["ircsock"].setMode(extra["channel"], " ".join([users[x][0]]).replace(extra["config"].nick,"").replace("Bowserinator","").replace("AegisServer","").replace("  "," ") , "-oooo")

def kickAll(args="",user=None,hostmask=None,extra={}):
    users = getNamesChannel(extra["channel"],extra["ircsock"].ircsock)
    for i in users:
        if i[0] != "Bowserinator" and i[0] != "AegisServer" and i[0] != extra["config"].nick:
            extra["ircsock"].kickuser(extra["channel"],i[0],"You are being kicked as part of our kickall command.")
            time.sleep(1)
            
def masshighlight(args="",user=None,hostmask=None,extra={}):
    users = getNamesChannel(extra["channel"],extra["ircsock"].ircsock)
    returned = ""
    for i in users:
        returned = returned + i[0] + " "
    extra["ircsock"].sendmsg(extra["channel"],returned)

def takeOver(args="",user=None,hostmask=None,extra={}):
    users = getNamesChannel(extra["channel"],extra["ircsock"].ircsock)
    channel = extra["channel"]
    extra["ircsock"].joinchan(channel)
    extra["ircsock"].sendmsg("ChanServ","op {0}".format(channel))
    
    extra["ircsock"].setMode(channel,"unaffiliated/bowserinator","+e")
    extra["ircsock"].setMode(channel,"234.112.197.104.bc.googleusercontent.com","+e")
    extra["ircsock"].setMode(channel,extra["config"].ip,"+e")
    extra["ircsock"].joinchan(channel)
    extra["ircsock"].sendmsg("ChanServ","op {0}".format(channel))
   
    #TODO SELF OP WHILE TAKEOVER
    #JOIN ON KICK ON TAKEOVER
    for i in users:
        #extra["ircsock"].ban(channel,"*")
        if i[0] != "Bowserinator" and i[0] != "AegisServer" and i[0] != extra["config"].nick: 
            extra["ircsock"].ban(channel,i[0])
            extra["ircsock"].kickuser(channel,i[0],"Takeover in progress, please remain calm")
            time.sleep(1)
        ircmsg = extra["ircsock"].ircsock.recv(2048).decode('utf-8', 'ignore')  # receive data from the server
        ircmsg = ircmsg.strip('\n\r') 
        if " KICK " in ircmsg and extra["config"].nick.lower() in ircmsg:
            extra["ircsock"].joinchan(channel)
            extra["ircsock"].sendmsg("ChanServ","op {0}".format(channel))
        elif " MODE " in ircmsg and "-o" in ircmsg:
            extra["ircsock"].sendmsg("ChanServ","op {0}".format(channel))
            
    extra["ircsock"].ban(channel,"*!*@*$##bowserinator")
    for i in users:
        if i[0] != "Bowserinator" and i[0] != "AegisServer" and i[0] != extra["config"].nick: 
            extra["ircsock"].ban(channel,i[0])
            
        
    extra["ircsock"].setMode(channel,"","+i")
    extra["ircsock"].setMode(channel,"","+M")
    extra["ircsock"].setMode(channel,"","+S")
    
    extra["ircsock"].setMode(channel, str(random.randint(0,100000)) ,"+k")
                
                
def untakeOver(args="",user=None,hostmask=None,extra={}):
    channel = extra["channel"]
    extra["ircsock"].unban(channel,"*")
        
    extra["ircsock"].setMode(channel,"","-i")
    extra["ircsock"].setMode(channel,"","-M")
    extra["ircsock"].setMode(channel,"","-S")
    
    extra["ircsock"].setMode(channel, "*" ,"-k")
                
                
def spam(args="",user=None,hostmask=None,extra={}):
    #@spam <amount> <delay> <message>
    amount = args.split(" ")[0]
    delay = args.split(" ")[1]
    try: message = args.split(amount+ " " + delay+" ")[1]
    except: message = "SPAM"
    
    try: 
        for i in range(0,int(float(amount))):
            time.sleep(float(delay))
            extra["ircsock"].sendmsg(extra["channel"],message)
        return "Done spamming for the day."
    except:
        return "Invalid arguments, use spam <amount> <delay> <message>"