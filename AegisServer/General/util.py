def gethostmask(nick,ircsock):
    ircsock.send("WHO {0}\r\n".format(nick).encode("UTF-8"))
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.decode("UTF-8")
    ircmsg = ircmsg.strip("\r\n")
    ircmsg = ircmsg.strip(":")
    ircmsg = ircmsg.split()
    if ircmsg[1] == "352":
        user = ircmsg[4]
        host = ircmsg[5]
        hm = "{0}!{1}@{2}".format(nick, user, host)
        return hm
    else:
        return False
        
def getbanmask(nick,ircsock):
    return "*!*@" + gethostmask(nick,ircsock).split("@")[1]