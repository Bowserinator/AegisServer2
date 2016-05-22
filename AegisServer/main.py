import traceback, socket
import connection, message, config, IO, commands, AegisServerAlpha, misc
from trival import fight
import re, time
from multiprocessing.pool import ThreadPool
import threading, os, sys

#5abcdefghi123456123111
#pip install pyimgur

FightBot = fight.FightBot()

ircsock = config.ircsock

ircsock.changenick(config.nick)
ircsock.joinchan(",".join(config.channels))
ircsock.sendmsg("NickServ","identify {0}".format(config.password))

def doAI(message,config,user,channel,ircsock):
    result = AegisServerAlpha.phrase(message,config.nick,user,channel)
    if result:
        ircsock.sendmsg(channel,result)


#TODO: sendmsg que, msg phraser,
#Config
#BETTER LOGS/stats
#Try to op self when joining back from kick? <<CONFIG FOR CERTAIN CHANNELS TOO

#MULTI Op COMMANDS http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python

#FOR CONTEST
#MAKE COOL STATS PAGE
#MAKE BOWSERCOUNTRIES

#TODO COMMAND CHANNEL RESTRICTIONS
#IF DETECTS ME BANNED
#  TRY TO CS OP ITSELF, KBAN BANNER AND UNBAN ME


while 1:
    try:
        ircmsg = ircsock.ircsock.recv(2048).decode('utf-8', 'ignore')  # receive data from the server
        ircmsg = ircmsg.strip('\n\r')  # removing any unnecessary linebreaks.
        try: ircmsg2 = config.Input.phrase(ircmsg)
        except IndexError: #RESTARTS THE BOT IF DISCONNECTED FROM SERVER
            config.Output.messageQueue = []
            time.sleep(1)
            os.execv(sys.executable, [sys.executable] + sys.argv) 

        for channel in config.channels:
            if ircmsg2["type"] == "KICK" and ircmsg2["userkicked"].lower() == config.nick.lower() and ircmsg2["channel"].lower() == channel.lower():
                ircsock.joinchan(channel)
                time.sleep(1)
                ircsock.joinchan(channel)
            if ircmsg2["type"] == "PART" and config.nick.lower() in ircmsg2["user"].lower() and "requested by" in ircmsg2["raw"].lower():
                ircsock.joinchan(channel)
                time.sleep(1)
                ircsock.joinchan(channel)
                
        #OTHER STUFF===============================================
        if ircmsg2["type"] == "MODE":
            try:
                result = message.phraseModeUser(ircmsg)
                for i in result[1]: #SELF UNBANS
                    if "+b" in i[1] and (config.ip.lower().startswith(i[0].split("@")[1].lower().replace("*","")) or config.nick.lower() in i[0].lower()):
                        ircsock.unban(result[2],i[0])
            except: pass
        
        elif ircmsg2["type"] == "PRIVMSG":
            channel = ircmsg2["channel"]
            message = ircmsg2["message"]
            user = ircmsg2["user"].split("!")[0]
            hostmask = ircmsg2["user"].split("@",1)[1]

            if user in [":potatorelay",":creativerelay"] and message.startswith("<"): #Minecraft messages
                message = message.split(">",1)[1].lstrip().rstrip()
            
            #PRIVMSG query
            if channel == config.nick:
                channel = user
            
            if message.split(" ")[0] == config.commandChar+"r" and config.userPerms.get(hostmask,0)>=4:
                reload(commands)
                commands.reload2()
                reload(commands)
                commands.reload2()
                reload(config)
                reload(misc)
                #reload(Database)
                config.Output.addMessage(channel,"Reload successful")
            
            #Database.phraseText({"channel":channel, "ircmsg":message, "user":user, "hostmask":hostmask},config,config.Output)
            if user not in [":PowderBot",":Andromeda",":AegisServer",":FightBot"] and message.lower().startswith(config.nick.lower()):
                t1 = threading.Thread(target=doAI, args=(message,config,user,channel,ircsock))
                t1.setDaemon(True); 
                t1.start(); 
            if AegisServerAlpha.antiAttack(message,config.nick):
                ircsock.sendmsg(channel,AegisServerAlpha.antiAttack(message,config.nick))
            if user == ":PowderBot" and misc.detectBomb(message):
                ircsock.sendmsg(channel,misc.detectBomb(message))
            
            if FightBot.fight(message,user,config,channel):
                ircsock.sendmsg(channel, FightBot.fight(message,user,config,channel))
            if FightBot.check_accept(message,user,config,channel):
                ircsock.sendmsg(channel, FightBot.check_accept(message,user,config,channel))
            
            #Runs all the commands
            for command in commands.commands:
                if message.split(" ")[0] == config.commandChar+command or (config.unsafeCommandChar and (config.commandChar+command) in message):
                    #Multithreading :D :D
                    if config.userPerms.get(hostmask,0) >= commands.commands[command].permLevel:
                        if command not in commands.noThread:
                            t1 = threading.Thread(target=commands.runCommand, args=(channel, message,config,commands,command, hostmask, user , config.Output, ircsock))
                            t1.setDaemon(True); 
                            t1.start(); #t1.join()
                        else: commands.runCommand(channel, message,config,commands,command, hostmask, user , config.Output, ircsock)
                    
                                    
        elif ircmsg2["type"] == "PING":
            ircsock.ping()
        
        #Sends the output from the commands
        config.Output.run(ircsock)
    
    except KeyboardInterrupt: pass
    except:
        traceback.print_exc()