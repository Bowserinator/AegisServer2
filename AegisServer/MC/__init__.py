#enchant possible, enchant prob, enchant best slot, enchant best, craftcalc, toolstats, craft, search, 
# mcwiki, brew, mcuserstats, mcstatus, gettile, getnearest
import dynmap, web, re
web = web.Web()
dynmap = dynmap.dynmap

def get_time(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    returned = dynmap.getServerTime()["time"] 
    if dynmap.getServerTime()["canSleep"]: returned = returned + " (You can sleep)"
    return "\x02Server Time: \x0f" + returned
    
def get_tick(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    returned = dynmap.getServerTick()
    return "\x02Server Tick: \x0f" + str(returned)
    
def get_player(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    players = dynmap.getPlayers()
    try: 
        data = dynmap.getPlayerData(args)
        returned = data["name"] + " is at " + "{0},{1},{2}".format(data["x"],data["y"],data["z"]) 
        world = {"world":"overworld","world_nether":"nether","world_the_end":"end"}[data["world"]]
        returned = returned + " in the {0} and has {1} health and {2} armour.".format(world,data["health"],data["armor"])
        return returned
    except: return "Could not find user, possibly hidden on dynmap?"
    
def get_weather(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    return "\x02Weather:\x0f Thundering: {0} | Raining: {1}".format(dynmap.isThundering(), dynmap.hasStorm())

def online(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    names = [x["name"] for x in dynmap.getPlayers()]
    if len(names) == 0: return "There are no players online on dynmap right now."
    return "\x02Online:\x0f " + " ".join(names)

def getmap(args="",user=None,hostmask=None,extra={}): 
    world = "overworld" 
    view = "flat"
    worlds = {"overworld":"world","nether":"world_nether","end":"world_the_end"}
    views = {"flat":"flat","3d":"surface","cave":"cave"}
    args = args.lower()
    
    if "overworld" in args:
        args = args.strip('nether').strip('overworld')
    elif "nether" in args or "hell" in args:
        world = "nether"
        args = args.strip('nether').strip('hell')
    elif "end" in args:
        world = "end"
        args = args.strip('end')
    
    if "flat" in args: args = args.strip('flat')
    elif "3d" in args: args = args.strip('3d'); view = "3d"
    elif "cave" in args: args = args.strip('cave'); view = "cave"
        
    args = args.lstrip().rstrip()
    world = worlds[world]
    view = views[view]
    dynmap.update()
    
    try: #Get the location of [player name] and return world
        if dynmap.getPlayerData(args): #If it's a valid player return map
            data = dynmap.getPlayerData(args)
            url = "http://dynmap.starcatcher.us/?worldname={0}&mapname={1}&zoom=6&x={2}&y={3}&z={4}".format(data["world"],view,data["x"],data["y"],data["z"])
            try: return web.isgd(url)
            except: return url
    except: pass

    #Obtain the location of [location] and return map
    locations = {
        "azure":{"cord":[-69,-220], "world":"world"},
        "spawn":{"cord":[-211,142], "world":"world"},
        "end portal":{"cord":[-115,-126], "world":"world_nether"},
    }
    
    for key in locations:
        if key in args.lower():
            url = "http://dynmap.starcatcher.us/?worldname={0}&mapname={1}&zoom=6&x={2}&y={3}&z={4}".format(locations[key]["world"],view,locations[key]["cord"][0],65,locations[key]["cord"][1])
            try: return web.isgd(url)
            except: return url
            
    #Obtain coordinates
    cords = re.findall("([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+)",args.replace(" ",""))
    if cords == []: cords = re.findall("([-+]?)([:]?\d*\.\d+|\d+),([-+]?)([:]?\d*\.\d+|\d+)",args.replace(" ",""))
    cords2 = []
    for i in cords[0]: cords2.append(i)
    x = cords2[0] + cords2[1]
    if len(cords2) == 4: 
        y = "65"; z = cords2[2]+cords2[3]
    elif len(cords2) == 6: 
        y = cords2[2]+cords2[3]
        z = cords2[4]+cords2[5]
    url = "http://dynmap.starcatcher.us/?worldname={0}&mapname={1}&zoom=6&x={2}&y={3}&z={4}".format(world,view,x,y,z)
    try: return web.isgd(url)
    except: return url
    
def getclaim(args="",user=None,hostmask=None,extra={}): 
    dynmap.update()
    try:
        player = dynmap.getPlayerData(args)
        x = player["x"]; z = player["z"]
        claims = dynmap.getClaims()
        for key in claims:
            claim2 = claims[key]
            if type(claim2) == dict: claim = claim2
            else: claim = claim2[0]
    
            if isBetween(x,z,claim['corners'][0], claim['corners'][1], claim['corners'][2], claim['corners'][3]):
                return "{0} is currently in a {1}x{2} ({3}) claim by {4}. \x02Permission trust:\x0f {5} | \x02Build:\x0f {6} | \x02Container:\x0f {7}".format(
                    player["name"],
                    int(abs(claim["corners"][0] - claim["corners"][2])),
                    int(abs(claim["corners"][1] - claim["corners"][3])),
                    int(abs(claim["corners"][0] - claim["corners"][2]) * abs(claim["corners"][1] - claim["corners"][3])),
                    key.split("_")[0],
                    ", ".join(claim["permTrust"]),
                    ", ".join(claim["trust"]),
                    ", ".join(claim["containerTrust"]),
                )
        return "{0} is currently not standing inside a claim.".format(player["name"])
    except: return "Could not find player {0}.".format(args)
    
def isBetween(x,z,x1,z1,x2,z2):
    if (x>x1 and x<x2) or (x>x2 and x<x1):
        if (z>z1 and z<z2) or (z>z2 and z<z1):
            return True
    return False
    
def getowc(args="",user=None,hostmask=None,extra={}): 
    cords = args.replace(","," ").split(" ")
    if len(cords) == 2:
        return "\x02Conversion: \x0f{0},{1}".format(float(cords[0])*8, float(cords[1])*8 )
    elif len(cords) == 3:
        return "\x02Conversion: \x0f{0},{1},{2}".format(float(cords[0])*8, float(cords[1]), float(cords[2])*8 )
        
def getnwc(args="",user=None,hostmask=None,extra={}): 
    cords = args.replace(","," ").split(" ")
    if len(cords) == 2:
        return "\x02Conversion: \x0f{0},{1}".format(float(cords[0])/8, float(cords[1])/8 )
    elif len(cords) == 3:
        return "\x02Conversion: \x0f{0},{1},{2}".format(float(cords[0])/8, float(cords[1]), float(cords[2])/8 )
