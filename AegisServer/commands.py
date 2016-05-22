import config, calc, connection, IO, message, BowserCountry, AegisServerAlpha, bans, trival, MC, General
import time, os, sys, subprocess, threading
from multiprocessing.pool import ThreadPool
import util

Runner = util.Repl()

def reload2():
    for x in [MC,General,config,calc,connection,IO,message,bans,util,trival,AegisServerAlpha]:
        t1 = threading.Thread(target=reload, args=(x,))
        t1.setDaemon(True); 
        t1.start();
    
#THE RUN COMMAND FUNCTION, THREADED
def runCommand(channel,message,config,commands,command,hostmask,user, output, ircsock):
    try: args = message.split(config.commandChar+command+ " ",1)[1]
    except: args = ""
    
    extra = { "channel": channel, "config":config, "output":output, "ircsock":ircsock }
    
    try: 
        result = commands.commands[command].function(args, user, hostmask, extra)
        if result != None: ircsock.sendmsg(channel, result)
    except Exception as e: 
        if commands.commands[command].autoHelp:
            ircsock.sendmsg(channel, "\x02Help: \x0f" + commands.commands[command].helpText)
        else: print(e)
            
def getCate(commands):
    #Gets command categories
    returned = []
    for c in commands:
        if commands[c].catagory not in ["evil"]:
            returned.append(commands[c].catagory)
    return list(set(returned))

#COMMAND CLASS
#+++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++
class Command(object):
    def __init__(self,name,helpText,catagory,permLevel,commandChar,autoHelp=True,chanRestrictions={},show=True): #Channels/PM restrictions
    #Catagory is for help, ie calc or general
        self.chanRestrictions = chanRestrictions
        self.catagory = catagory
        self.name = name
        self.show = show
        self.helpText = helpText
        self.permLevel = permLevel
        self.commandChar = commandChar
        self.function = None
        self.autoHelp = autoHelp


#SOME DEFAULT FUNCTIONS
def irc_help(args,user="",hostmask="",extra={}):
    try: 
        if args=="":
            return "Command does not exist, try list for full command listing."
        elif args=="me":
            return "Stay calm, help will arrive soon!"
        return "\x02Help: \x0f" + commands[args].helpText
    except: return "Command does not exist, try list for full command listing."
def ping(args=None,user=None,hostmask=None,extra={}): return "PONG PONG PONG"
def pong(args=None,user=None,hostmask=None,extra={}): return "It's ping you moron."

def ding(args=None,user=None,hostmask=None,extra={}): return "DONG DONG DONG"
def dong(args=None,user=None,hostmask=None,extra={}): return "It's ding you moron."

def pause(args=None,user=None,hostmask=None,extra={}):
    time.sleep(10)
    return "10 seconds have passed"
def irc_eval(args,user=None,hostmask=None,extra={}):
    import config, AegisServerAlpha,  bans, calc
    try: return "Result: " + str(eval(args))
    except Exception as e: return str(e)
def bot_restart(args="",user=None,hostmask=None,extra={}): extra["ircsock"].quit(config.quit_message) #It will rejoin when detected it quits
def list_irc(args="",user=None,hostmask=None,extra={}):
    cata = getCate(commands)
    if args == "":
        return "\x02Do {0}list <module name>\x0f: ".format(config.commandChar) + ", ".join(cata)
    #return ", ".join(commands.keys())
    returned = []
    for c in commands:
        if commands[c].catagory in args and commands[c].show: returned.append(c)
    if len(returned) == 0 or args == "evil": return "Not a valid list category."
    return "\x02Commands: \x0f" + ", ".join(returned)
def shell(args="",user=None,hostmask=None,extra={}): #+" | ./ircize --remove"
     try: s = subprocess.check_output(args, stderr=subprocess.STDOUT, shell=True) 
     except: return "An error has occured."
     if s: 
        s = s.decode() 
        for line in str(s).splitlines(): extra["ircsock"].sendmsg(extra["channel"], line) 
def run_python(args="",user=None,hostmask=None,extra={}): 
    returned = str(Runner.run(args))
    if returned == None or returned.replace(" ","") == "": return "[No output]"
    return returned
def bot_exec(args="",user=None,hostmask=None,extra={}): 
    try: 
        exec args
        return "It worked."
    except: return "An error has occured."
    
def pig_latin(args="",user=None,hostmask=None,extra={}):return "\x02Result: \x0f"+" ".join([x[1:]+x[0]+'ay' for x in args.split(" ")]) 
def alpha_order(args="",user=None,hostmask=None,extra={}): return "\x02Result: \x0f" + "".join(sorted(list(args))) 

commands = {}
#GENERAL -------------------------
commands['help'] = Command("help","help <command> - Gives help text for command.","general",0,config.commandChar); commands['help'].function = irc_help
commands['ping'] = Command("ping","ping - Tells if the bot is alive.","general",0,config.commandChar); commands['ping'].function = ping
commands['pong'] = Command("ping","pong - Not ping.","general",0,config.commandChar,show=False); commands['pong'].function = pong

commands['ding'] = Command("ding","ding - Tells if the bot is alive.","general",0,config.commandChar,show=False); commands['ding'].function = ding
commands['dong'] = Command("ding","dong - Not ding.","general",0,config.commandChar,show=False); commands['dong'].function = dong

commands['list'] = Command("list","list - Lists all commands.","general",0,config.commandChar); commands['list'].function = list_irc
#CONFIG ---------------------------
commands['pause'] = Command("pause","pause - Pauses the bot for 10 seconds.","config",500,config.commandChar); commands['pause'].function = pause
commands['eval'] = Command("eval","eval <code> - Evaluates code.","config",500,config.commandChar); commands['eval'].function = irc_eval
commands['exec'] = Command("exec","exec <code> - Evaluates code.","config",500,config.commandChar); commands['exec'].function = bot_exec
commands['restart'] = Command("restart","restart - Restarts bot.","config",500,config.commandChar); commands['restart'].function = bot_restart
commands['shell'] = Command("shell","shell <command> - Run shell command.","config",500,config.commandChar); commands['shell'].function = shell
commands['py'] = Command("py","py <code> - Like eval and exec.","config",500,config.commandChar); commands['py'].function = run_python


#CALC -----------------------------
commands['calc'] = Command("calc","calc <math> - Computes math, !,!!,sqrt,fact,trig. Use DEG/RAD/SCI/FRACT at the end for options. Use DIGIT=[number] to set decimal precision","calc",1000,config.commandChar); commands['calc'].function = calc.phraseTextMath
commands['convert'] = Command("convert","convert <value> <unit1> to <unit2> Converts from unit1 to unit2, use listunit to get all unit names.","calc",0,config.commandChar); commands['convert'].function = calc.convert_stuff
commands['listunit'] = Command("listunit","listunit <category> - Lists the units for that category","calc",0,config.commandChar); commands['listunit'].function = calc.list_units
commands['latex'] = Command("latex","latex <equation> - Returns image rendering of latex","calc",0,config.commandChar); commands['latex'].function = calc.formula_as_file


commands['createCountry'] = Command("createCountry","createCountry - Makes a country.","bowsercountry",0,config.commandChar); commands['createCountry'].function = BowserCountry.commandMakeCountry

#Trival
commands['periodic'] = Command("periodic","periodic - Gives an ASCII periodic table","trival",400,config.commandChar); commands['periodic'].function = trival.periodic_table
commands['ascii'] = Command("ascii","ascii <name> - Gives ascii art for name","trival",400,config.commandChar); commands['ascii'].function = trival.ascii
commands['figlet'] = Command("figlet","figlet <text> - Creates figlet for text.","trival",400,config.commandChar); commands['figlet'].function = trival.figlet
commands['moo'] = Command("moo","moo - MOOOOOO!!!","trival",0,config.commandChar); commands['moo'].function = trival.moo
commands['excuse'] = Command("excuse","excuse - Gives excuse for something","trival",0,config.commandChar); commands['excuse'].function = trival.excuse

#Filter ---------------------------
commands['filter.pig_latin'] = Command("filter.pig_latin","filter.pig_latin <text> - Returns pig latin for text","filter",500,config.commandChar); commands['filter.pig_latin'].function = pig_latin
commands['filter.alpha_order'] = Command("filter.alpha_order","filter.alpha_order <text> - Returns alphabetical order for letters in text","filter",500,config.commandChar); commands['filter.alpha_order'].function = alpha_order

#Op--------------------------------
#commands['takeover'] = Command("takeover","[Doesn't exist]","evil",500,config.commandChar,False); commands['takeover'].function = bans.takeOver
commands['opAll'] = Command("opAll","[Doesn't exist]","evil",500,config.commandChar,False); commands['opAll'].function = bans.opAll
commands['deopAll'] = Command("deopAll","[Doesn't exist]","evil",500,config.commandChar,False); commands['deopAll'].function = bans.deopAll
commands['kickAll'] = Command("kickAll","[Doesn't exist]","evil",500,config.commandChar,False); commands['kickAll'].function = bans.kickAll
commands['masshighlight'] = Command("masshighlight","[Doesn't exist]","evil",500,config.commandChar); commands['masshighlight'].function = bans.masshighlight
commands['untakeover'] = Command("untakeover","[Doesn't exist]","evil",500,config.commandChar,False); commands['untakeover'].function = bans.untakeOver
commands['spam'] = Command("spam","spam - Spams a channel, use spam <amount> <delay> <message>","evil",500,config.commandChar); commands['spam'].function = bans.spam

#MC-------------------------------------------------------------
commands['get_time'] = Command("get_time","get_time - Returns minecraft server time","mc",0,config.commandChar); commands['get_time'].function = MC.get_time
commands['get_server_time'] = Command("get_server_time","get_server_time - Returns minecraft server time in ticks","mc",0,config.commandChar); commands['get_server_time'].function = MC.get_tick
commands['get_player'] = Command("get_player","get_player <player> - Get data about player. There is auto complete.","mc",0,config.commandChar); commands['get_player'].function = MC.get_player
commands['get_weather'] = Command("get_weather","get_weather - Returns weather status.","mc",0,config.commandChar); commands['get_weather'].function = MC.get_weather
commands['online'] = Command("online","online - Get players online (Enabled on dynmap)","mc",0,config.commandChar); commands['online'].function = MC.online

commands['getmap'] = Command("getmap","getmap (<x,y,z>||<player name>||<location>) <world> <view> - Gets dynmap for location","mc",0,config.commandChar,show=False); commands['getmap'].function = MC.getmap
commands['get_map'] = Command("get_map","getmap (<x,y,z>||<player name>||<location>) <world> <view> - Gets dynmap for location","mc",0,config.commandChar); commands['get_map'].function = MC.getmap
commands['getclaim'] = Command("getclaim","getclaim <player> - Gets claim information for player, has auto complete.","mc",0,config.commandChar,autoHelp=False); commands['getclaim'].function = MC.getclaim

commands['getowc'] = Command("getowc","getowc <x>,<y>,<z> - Converts from nether to overworld.","mc",0,config.commandChar); commands['getowc'].function = MC.getowc
commands['getnwc'] = Command("getnwc","getnwc <x>,<y>,<z> - Converts from overworld to nether.","mc",0,config.commandChar); commands['getnwc'].function = MC.getnwc

#General-------------------------------
commands['geoip'] = Command("geoip","geoip <ip> - Get geoip info for ip.","general",0,config.commandChar); commands['geoip'].function = General.geoip
commands['element'] = Command("element","element <element> - Get element info on element.","general",0,config.commandChar); commands['element'].function = General.element
commands['define'] = Command("define","define <word> <n=1,2>- Get definition for a word","general",0,config.commandChar); commands['define'].function = General.define
commands['translate'] = Command("translate","translate <text> to_lan=<lan code> from_lan=<lan code>","general",0,config.commandChar); commands['translate'].function = General.translate
commands['attack'] = Command("attack","attack <user> - ATTACK!","general",0,config.commandChar); commands['attack'].function = General.attack

noThread = ["opAll","deopAll","kickAll","masshighlight","takeover","geoip"] #No threading for these commands!