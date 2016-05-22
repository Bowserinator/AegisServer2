from difflib import SequenceMatcher
import re

def probFind(main,substr): #Probibility of substr in main
    currentProb = 0
    if len(substr) >= len(main):
        return 0
    for i in range(0,len(main)-len(substr)+1):
        test = main[i:i+len(substr)]
        if SequenceMatcher(None, test, substr).ratio() > currentProb:
            currentProb = SequenceMatcher(None, test, substr).ratio() 
    return currentProb
    
def probFindArray(main,substr2): #Probibility of substr in main
    for substr in substr2:
        currentProb = 0
        if len(substr) >= len(main):
            return 0
        for i in range(0,len(main)-len(substr)+1):
            test = main[i:i+len(substr)]
            if SequenceMatcher(None, test, substr).ratio() > currentProb:
                currentProb = SequenceMatcher(None, test, substr).ratio() 
        if currentProb > 0.9: return True
    return False


def phraseData(text):
    #Blocks beacon
    #Speed to walk
    if probFindArray(text,["level","height","layer"]):
        if probFind(text,"best") >= 0.9: #Get best layer to get ore/lava
            if probFind(text,"iron") >= 0.9: return "The best layer to mine iron is 5 - 54."
            elif probFind(text,"coal") >= 0.9: return "The best layer to mine coal is 5 - 52."
            elif probFind(text,"gold") >= 0.9: return "The best layer to mine gold is 5 - 29."
            elif probFind(text,"redstone") >= 0.9: return "The best layer to mine redstone is 5 - 12."
            elif probFind(text,"diamond") >= 0.9: return "The best layer to mine diamond is 5 - 12."
            elif probFind(text,"lapis") >= 0.9: return "The best layer to mine lapis is 14 - 16."
            elif probFind(text,"quartz") >= 0.9: return "The best layer to mine nether quartz is 15 - 120."
            elif probFind(text,"emerald") >= 0.9: return "The best layer to mine emerald ore is 5 - 29 in extreme hills biome."
            elif probFind(text,"lava") >= 0.9: return "Lava spawns in levels 1-10 in caves/ravines, although lava lakes can spawn in any biome at any height. In the nether lava spawns at levels 22-31."
        
    elif probFindArray(text,["how many","how much"]): #Get how much stuff in a chunk
        if probFind(text,"redstone") >= 0.9: return "There is on average 24.8 redstone ore per chunk. (117 items)"
        elif probFind(text,"stone") >= 0.9: return "There is about 15000 stone per chunk."
        elif probFind(text,"diamond") >= 0.9: return "There is on average 5 diamond ore per chunk, but there can be up to 10."
        elif probFind(text,"gold") >= 0.9: return "There is on average 8.2 gold ore per chunk."
        elif probFind(text,"iron") >= 0.9: return "There is on average 77 iron ore per chunk."
        elif probFind(text,"lapis") >= 0.9: return "There is on average 3.43 lapis ore per chunk."
        elif probFind(text,"quartz") >= 0.9: return "There is on average 79 nether quartz ore per chunk."
        elif probFind(text,"emerald") >= 0.9: return "There is on average 0.2 emerald ore per chunk."
        
    elif probFind(text,"ticks") >= 0.9 and probFind(text,"second") >= 0.9: return "There are 20 ticks per second."
    elif probFind(text,"beacon") >= 0.9 and probFind(text,"block") >= 0.9: 
        return "Level 1: 9 | Level 2: 34 | Level 3: 83 | Level 4: 164"
        
    elif probFindArray(text,["how fast","speed"]): #Get how fast a mode of travel is
        if probFind(text,"walk") >= 0.9: return "4.3 m/s (Flat terrain) | 34.4 m/s (Nether equivelent)"
        elif probFind(text,"run") >= 0.9 or probFind(text,"sprint") >= 0.9: return "5.6 m/s (Flat terrain) | 44.8 m/s (Nether equivelent)"
        elif probFind(text,"sneak") >= 0.9: return "1.3 m/s (Flat terrain) | 10.4 m/s (Nether equivelent)"
        elif probFind(text,"minecart") >= 0.9: return "8 m/s (Powered Track) | 64 m/s (Nether equivelent)"
        elif probFind(text,"boat") >= 0.9: return "6.2 m/s (Flat water) | 40 m/s (On ice) | 320 m/s (Nether equivelent)"
        elif probFind(text,"pig") >= 0.9: return "8 m/s (Carrot + stick) | 64 m/s (Nether equivelent)"
        elif probFind(text,"horse") >= 0.9: return "9.675 m/s (Average horse) | 77.4 m/s (Nether equivelent) | 14.57 m/s (Best horse) | 116.6 (Nether equivelent)"
        elif probFind(text,"donkey") >= 0.9: return "7.525 m/s | 60.2 m/s (Nether equivelent)"
        elif probFind(text,"swim") >= 0.9: return "2.2 m/s (Horiziontal) | 0.6 m/s (Going up) | 3.4 m/s (Going down)"
        elif probFind(text,"fly") >= 0.9: return "10.9 m/s (Creative) | 7.5 m/s (Going vertically)"
        elif probFind(text,"ender pearl") >= 0.9: return "~23 m/s (15 degrees above horiziontal)"
        elif probFind(text,"wing") >= 0.9 or probFind(text,"elytra") >= 0.9: return "30 m/s (At 0 degree pitch) | 240 m/s (Nether equivelent)"
        
        elif probFind(text,"jump") >= 0.9: return "2.0 m/s (Jumping such as pillar jumping or jumping up stairs)"
        elif probFind(text,"stair") >= 0.9: return "3.2 m/s (Going up) | 3.6 m/s (Going down)"
        elif probFind(text,"ladder") >= 0.9: return "2.35 m/s (Going up) | 3 m/s (Going down)"
        