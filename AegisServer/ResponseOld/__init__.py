#logs
#userstats
#personal information
#responses (Easter eggs)
#WHAT TIME IS IT WHERE USER Is
#CTCP Time, /ctcp [user] TIME

#TODO

#SELF BIRTHDAY IS March 22 2016 4:11 EST

execfile("Database/response/responses.py")
execfile("Database/response/mathphrase.py")
execfile("Database/response/favorites.py")
execfile("Database/user/__init__.py")
execfile("calc/__init__.py")

from datetime import datetime, timedelta

def phraseText(args,config,output):
    ircmsg = args["ircmsg"]
    channel = args["channel"]
    user = args["user"].replace(":","")
    hostmask = args["hostmask"]
    
    if ircmsg.lower().startswith("bowserbot") or ircmsg.lower().startswith(config.nick.lower()):
        text = ircmsg+ " "
        text = text.replace("what's", "what is ")
        text = text.replace("whats", "what is").replace(" u "," you ")
        text = text.replace("where's", "where is ")
        text = text.replace("wheres", "where is ")
        text = text.replace("whos", "who is ")
        text = text.replace("who's", "who is ")
        text = text.replace("dont", "do not ")
        text = text.replace("don't", "do not ")
        text = text.replace("didnt","did not")
        text = text.replace("its","it is").replace("it's","it is")
        text = text.replace("'m"," am").replace("'ve"," have").replace("'ll"," will").replace("'re"," are").replace("'nt"," not")
        ircmsg = text

        if config.nick.lower() in ircmsg.split(" ")[0].lower() or "bowserbot" in ircmsg.split(" ")[0].lower():
            ircmsg = ircmsg.split(" ",1)[1]
                
        if isMath(ircmsg): #Calculate mathamatics
            print strToInt(delQuestion(ircmsg))
            result = "\x02Input: \x0f" + strToInt(delQuestion(ircmsg)) + " " + phraseTextMath(strToInt(delQuestion(ircmsg)))
            if "Could not understand input." not in result:
                output.addMessage(channel,result)
        result = phraseMatch(ircmsg) #"easter eggs"
        if result != None:
            output.addMessage(channel, result)
    
        result = getDataFromString(ircmsg)
        if result:
            output.addMessage(channel, result)
            
        if isSimilar("what is the time",ircmsg) or isSimilar("what time is it",ircmsg) or isSimilar("what is the time right now",ircmsg) or isSimilar("what day is it today",ircmsg) or isSimilar("what day is today",ircmsg)  or isSimilar("what day is it",ircmsg)  or isSimilar("what is the date",ircmsg):
            try:
                time = "\x02Date: \x0f" + str(datetime.now() + timedelta(hours=matchUser(user.lower())["time_shift"] )).replace("."," \x02Millis:\x0f ").replace(" ","\x02 Time: \x0f",1)
                output.addMessage(channel, time)
            except: output.addMessage(channel, "\x02Date: \x0f"+str(datetime.now()).replace("."," \x02Millis:\x0f ").replace(" ","\x02 Time: \x0f",1) )