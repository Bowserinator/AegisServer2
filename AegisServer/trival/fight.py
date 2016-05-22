#FIGHTBOT THING
#https://github.com/tonyravioli/dongerdong/blob/master/dongerdong.py

#It's T3ZlckNvZGVy's turn. 
#Bowserinator heals for 26HP, bringing them to 55HP 
#T3ZlckNvZGVy (100HP) deals 27 damage to Bowserinator (29HP) 
#AegisServer2: Bowserinator challenged you. To accept, use '!accept Bowserinator'.  DONE

import re
    
class FightBot(object):
    def __init__(self):
        self.players = {}
        self.start = False
        self.health = 100
        self.praised = False
    
    def fight(self,message,user,config,channel):
        """Check for people joining in
        if fail message try another move
        if in bad time try praising
        attack weakest player
        heal if health < 44
        
        If no game don't do anything
        If gameover or dead start=False
        
        BOWSERINATOR JOINS THE FIGHT (80HP) 
        BOWSERINATOR'S ZOMBIE JOINS THE FIGHT (31HP) <- Add Bowserinator as user
        It's JeDa's turn. 
        JeDa forfeits due to idle. -> remove player
        BWBellairs REKT iovoid, bowserinator -> remove player

        DONE=======================================
        !quit -> remove player
        If game cancneled
        JeDa (76HP) deals 32 damage to FightBot (19HP) 
        FightBot heals for 41HP, bringing them to 60HP 
        
        if user accepts challenger in player list
        !accept zz
        if zz in player list add user to player list""" 
        message = message.replace("\x02","").replace("\x0f","")
        if message.startswith("!accept "):
            if message.split("!accept ")[1].lower() in self.players.keys():
                self.players[user.lower().replace(":","")] = {"health":100}
        if message == "!quit":
            try: del self.players[user.lower().replace(":","")]
            except: pass
        
        if self.isBot(user):
            #UPdate the health
            #Update health for attacks
            result = re.findall("(.*) \((.*)HP\) deals (.*) damage to (.*) \((.*)HP\)",message)
            if len(result) > 0:
                result = result[0]
                if result[0].lower() == config.botnick.lower():
                    self.health = int(result[1])
                else: self.players[result[0].lower()]["health"] = int(result[1])
                if result[3].lower() == config.botnick.lower():
                    self.health = int(result[4])
                else: self.players[result[3].lower()]["health"] = int(result[4])
            
            #Update health for heals
            result = re.findall("(.*) heals for (.*)HP, bring them to (.*)HP",message)
            if len(result) > 0:
                result = result[0]
                if result[0].lower() == config.botnick.lower():
                    self.health = int(result[2])
                else:
                    self.players[result[0].lower()]["health"] = int(result[2])
            
            #Remove players 
            if " forfeits due to idle." in message:
                try: del self.players[message.split(" forfeits")[1].lower()]
                except: pass
            
            #Check for commands
            if message == "Fight cancelled.": 
                self.start = False
                self.players = {}
            if message == "You can't heal.":
                return self.attack()
            if "It's {}'s turn".format(config.botnick) in message: #IT's the bot's turn
                if self.health < 44: 
                    return "!heal"
                return self.attack()
            
    def attack(self):
        current = {"health":100,"key":"BWBellairs"}
        for key in self.players:
            if self.players[key]["health"] <= 24: return "!hit {}".format(key) #Always attack :D
            if self.players[key]["health"] <= current["health"]:
                current = self.players[key]
                current["key"] = key
        return "!hit {}".format(current["key"])
            
    
    def check_accept(self,message,user,config,channel):
        #Bowserinator: JeDa challenged you to a deathmatch. The loser will be banned for 20 minutes. To accept, use '!accept JeDa'. 
        message = message.replace("\x02","").replace("\x0f","")
        if self.isBot(user) and config.botnick in message:
            result = re.findall("(.*): (.*) challenged (.*) To accept, use '(.*)'." ,message)
            if len(result) > 0:
                self.players[result[0][1].lower()] = {"health":100}
                self.start = True
                return result[0][3]
        
    def isBot(self,user):
        if user.lower() in [":fightbot"]:
            return True
        return False
  
class config(object):
    def __init__(self):
        self.botnick = "AegisServer2"

c = config()
a = FightBot()
print a.check_accept("AegisServer2, AegisServer: Bowserinator challenged you. To accept, use '!accept Bowserinator'.",":fightbot",c,"##powder-bots")
print a.players
#(self,message,user,config,channel):
print a.fight("It's AegisServer2's turn.",":fightbot",c,"##powder-bots")
print a.fight("AegisServer2 (200HP) deals 32 damage to Bowserinator (32HP)",":fightbot",c,"##powder-bots")
