

#:IndigoTiger!Brad@botters/IndigoTiger MODE ##BWBellairs-bots -o+b Bowserinator *!*@unaffiliated/bowserinator
#MULTI MODE EXAMPLE on one user
#:IndigoTiger!Brad@botters/IndigoTiger MODE ##BWBellairs-bots +oooo RadioNeat IovoidBot wolfy1339 Andromeda-dev
#MULTI OP EXAMPLE

def phraseModeUser(ircmsg): #Gets modes on users
    message = ircmsg
    
    ircmsg = ircmsg.split(" MODE ")[1]
    channel = ircmsg.split(" ")[0]
    modes = ircmsg.split(" ")[1]
    users = ircmsg.split(" ",2)[2]
    if len(users) == 0:
        return None
        
    currentMode = ""; modes2 = []
    for i in modes:
        if i=="+" or i=="-":
            currentMode = i; continue
        if i in ['e','I','b','q','o','v' ]: #Modes with user parameters
            modes2.append(currentMode+i)
    
    if len(users.split(" ")) == 1: #1 user
        return [message.split(" MODE ")[0],  [[users,modes2]], channel]   
    userA = []
    for i in users.split(" "):
        userA.append([i,modes2[users.split(" ").index(i)] ])
    return [message.split(" MODE ")[0],  userA , channel]   
        
    