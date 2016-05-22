#DO STUFF
#LIke s -> autocorrect
#s/a/b -> replace a,b
import config, random, re

def phrase(text):
    pass
    
#Detect powderbot timebombs!!!
def detectBomb(text):
    if "stuffs a bomb down {0}'s pants.".format(config.nick) in text:
        text = text.replace(", and",",").replace(".","").replace("and",",")
        choices = text.split("They are: ")[1].split(",")
        return "$cut " + random.choice(choices).lstrip().rstrip().strip("\x01")

def fightBot(user,text,botnick): #WIP
    challenger = ""

    #It's T3ZlckNvZGVy's turn. 
    #Bowserinator heals for 26HP, bringing them to 55HP 
    #T3ZlckNvZGVy (100HP) deals 27 damage to Bowserinator (29HP) 
    #AegisServer2: Bowserinator challenged you. To accept, use '!accept Bowserinator'.  DONE
    if user.lower() in [":fightbot"]:
        text = text.replace("\x02","")
        if len(re.findall(botnick+": (.*?) challenged you", text )) > 0:
            challenger = re.findall(botnick+": (.*?) challenged you", text )[0]
            return "!accept " + re.findall(botnick+": (.*?) challenged you", text )[0]
        elif "It's " + botnick + "'s turn." in text:
            return "!hit " + challenger