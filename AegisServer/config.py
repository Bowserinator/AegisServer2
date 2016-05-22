import IO
import connection

Input = IO.Input("client")
Output = IO.Output("client")
ircsock = connection.Connection("irc.freenode.net",6697,True)

server = "irc.freenode.net"
port = 6667
ssl = False

channels = ["##FightBot","#ezzybot-bots","##powder-mc","##powder-bots","##jpec-south","##bowserinator","#ezzybot-bots","#botters-test","#aegisserver","##takeover","#ezzybot","##bowserinator-test"]
nick = "AegisServer2"
quit_message = "Despite goodwill, human intimacy cannot occur without substantial mutual harm"
commandChar = "@"
password = "aegispass"

ip = "58.208.197.104.bc.googleusercontent.com"
banmask = nick + "@" + ip
blacklistchan = [] #Channels the bot will not go into
unsafeCommandChar = False

botnick = nick

#TODO: channel class with perms per channel
userPerms = {
    "unaffiliated/bowserinator":100000,
    "unaffiliated/jeffl35":50,
}