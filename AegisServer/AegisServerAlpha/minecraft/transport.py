from difflib import SequenceMatcher
import re, dynmap, base, mcmath, math

#Time it takes to travel to location
#Otherwise: time it takes, how long, length of journey/trip
#While: walking, sprinting, sprint jumping, sneaking, minecart, boat stuff, etc...
#Under potion effects too
#If no start location given assume start is the player saying it
dynmap = dynmap.Dynmap("dynmap.starcatcher.us")

#Vertical
#How long does it take to fall/drop
def convertSeconds(time):
    hour = int(time/3600)
    minute = int((time - hour*3600)/60)
    second = time-hour*3600 - minute*60
    returned = ""
    if hour > 0: returned = returned + str(hour) + " hours "
    if minute > 0: returned = returned + str(minute) + " minutes "
    if second > 0: returned = returned + str(round(second)) + " seconds "
    return returned.lstrip().rstrip()
    

def calcDis(c1,c2):
    points1 = [float(x) for x in c1.split(",")]
    points2 = [float(x) for x in c2.split(",")]
    if len(points1) == 2: points1 = [points1[0], 65, points1[1]]
    if len(points2) == 2: points2 = [points2[0], 65, points2[1]]
    return {"horz":mcmath.distance2D(points1[0], points1[2], points2[0], points2[2]), "vert":abs(points1[1] - points2[1])}
    
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

def listToCord(l):
    if len(l) == 4:
        return l[0]+l[1]+','+l[2]+l[3]
    elif len(l) == 6:
        return l[0]+l[1]+','+l[2]+l[3]+','+l[4]+l[5]
    
def phraseInput(text,username=""):
    #Returns requirements
    for i in ["how long","time it take","length of trip","length of journey"]:
        if probFind(text,i) > 0.85: #Check if it's a question regarding the length of the trip
            #Config variables
            travel_type = "walk" #Default travel type
            vert_type = "jump"
            potion = ""
            nether = False
            
            if "nether" in text or "hell" in text:
                nether = True
                
            #Horiziontal transporation methods
            if probFind(text,"walk") > 0.9: travel_type = "walk"
            elif probFindArray(text,["sprint","run"]): travel_type = "run"
            elif probFind(text,"sneak") > 0.9: travel_type = "sneak"
            elif probFind(text,"cart") > 0.9: travel_type = "minecart"
            elif probFind(text,"boat") > 0.9: travel_type = "boat"
            elif probFind(text,"pig") > 0.9: travel_type = "pig"
            elif probFindArray(text,["horse","donkey","mule"]): travel_type = "horse" #Also assume donkey and mule
            elif probFind(text,"swim") > 0.9: travel_type = "swim"
            elif probFind(text,"fly") > 0.9: travel_type = "fly" #Assume both creative and elytra
            elif probFind(text,"pearl") > 0.9: travel_type = "pearl"
            elif probFindArray(text,["elytra","wing"]): travel_type = "wing"
            
            #Vertical transporation methods
            #Swimming in lava/water is not included and so is flying in creative
            if probFind(text,"jump") > 0.9: vert_type = "jump"
            elif probFind(text,"stair") > 0.9: vert_type = "stairs"
            elif probFind(text,"ladder") > 0.9: vert_type = "ladder"
            
            #Obtain location
            text2 = text.replace(" ","")
            
            #Locate the bases FIRST
            a = re.findall(" (.*) base",text)
            if a != []:
                for i in a:
                    for b in base.bases:
                        if i.split(" ")[-1].replace("'s","") in b.users:
                            text = text.replace("base","")
                            text = text.replace(i.split(" ")[-1], str(b.x)+","+str(b.y)+","+str(b.z))
            for b in base.bases:
                if b.name.lower() in text.lower():
                    text = text.lower().replace(b.name.lower(), str(b.x)+","+str(b.y)+","+str(b.z))
            
            #Locate the players and replace names with coordinates
            dynmap.update(); names = []
            players = dynmap.getPlayers()
            for key in players:
                name = key["name"] #Prob match if player is there
                if probFind(text.lower(),name.lower()) > 0.85:
                    text = text.lower().replace(name.lower(), str(key["x"]) + ','+str(key["y"])+','+str(key["z"]) )
            
            #Locate the coordinates
            cords = re.findall("([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+)",text.replace(" ",""))
            if cords != []:
                for x in cords:
                    replace = x[0]+x[1]+","+x[2]+x[3]+","+x[4]+x[5]
                    text2 = text2.replace(replace,"")
            cords2 = re.findall("([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+)",text2.replace(" ",""))
            cords = cords + cords2; text3 = text.replace(" ","")
            
            #Facepalm, the order of the coordinates don't matter
            if len(cords)>=1:
                c1 = listToCord(cords[0]); 
                if len(cords)>=2:
                    c2 = listToCord(cords[1])
                    if text3.index(c2) < text3.index(c1):
                        c1,c2 = c2,c1
                else: 
                    c2 = c1
                    try:
                        c1 = dynmap.getPlayerData(username)
                        c1 = str(c1["x"]) + "," + str(c1["y"]) + "," + str(c1["z"])
                    except: return False
            
            #Get the actual distance
            distance = calcDis(c1,c2)
            times = []
            
            if travel_type == 'walk':
                times.append( 
                    [distance["horz"]/4.3,
                    "(Assuming flat terrain)"]
                )
            elif travel_type == 'run':
                times.append( [distance["horz"]/5.6,
                "(Assuming flat terrain)"])
            elif travel_type == 'sneak':
               times.append( [distance["horz"]/1.3,
               "(Assuming flat terrain)"])
            elif travel_type == 'minecart':
               times.append( [distance["horz"]/8,
               "(Assuming powered rails)"] )
               times.append( [distance["horz"]/7.1,
               "(Assuming 1/4 slope track)"] )
            elif travel_type == 'boat':
               times.append( [distance["horz"]/6.2,
               "(Assuming max speed on flat water)"] )
               times.append( [distance["horz"]/40,
               "(Assuming on ice)"] )
            elif travel_type == 'pig':
               times.append( [distance["horz"]/8,
               "(Assuming flat terrain)"] )
            elif travel_type == 'horse':
               times.append( [distance["horz"]/9.675,
               "(Assuming average horse)"] )
               times.append( [distance["horz"]/14.57,
               "(Assuming best horse)"] )
               times.append( [distance["horz"]/7.525,
               "(Assuming donkey)"] )
            elif travel_type == 'swim':
               times.append( [distance["horz"]/1.97,
               "(Assuming still water)"] )
            elif travel_type == 'fly':
               times.append( [distance["horz"]/10.9,
               "(Assuming creative)"] )
               times.append( [distance["horz"]/30,
               "(Assuming elytra, at 0 pitch)"] )
            elif travel_type == 'pearl':
               times.append( [distance["horz"]/23,
               "(Assuming thrown at 15 degrees)"] )
            elif travel_type == 'wing':
                times.append( [distance["horz"]/30,
               "(Assuming elytra, at 0 pitch)"] )
            
            vert_time = 0

            if travel_type == 'fly':
                vert_time = distance["vert"]/7.5
            elif travel_type == 'swim':
                vert_time = distance["vert"]/2
            elif vert_type == "jump":
                vert_time = distance["vert"]/2
            elif vert_type == "stairs":
                vert_time = distance["vert"]/3.2
            elif vert_type == "ladder":
                vert_time = distance["vert"]/2.35

            #Add vertical values to times and divide times by 8 for nether
            for i in range(0,len(times)):
                if nether:
                    times[i][0] /= 8
                times[i][0] += vert_time
                
            for i in range(0,len(times)):
                times[i][0] = convertSeconds(times[i][0])
            times.insert(0, [str(round(distance["horz"])),"meters"] )
            input_int = "Time to travel by {0} from {1} to {2}".format(travel_type,c1,c2)
            if nether: input_int += " via the nether"
            return [times,input_int]
                
    return False
    
