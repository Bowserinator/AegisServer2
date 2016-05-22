import re, socket, math, web, requests
import elements, util, general
import random
from decimal import Decimal

web = web.Web()

def define(args,user="",hostmask="",extra={}):
    if extra["channel"] == "##powder-mc": return "Disabled for this channel."
    #Define word <definition>
    number = args.split(" ")[-1]
    try: float(number); n = int(float(number))
    except: n = None
    
    defi = general.define(args.replace(str(n),""))
    if n and n >= 0 and n < len(defi): return defi[n].encode('utf8')
    
    if len(defi) == 0: return "Word not found."
    if len(defi) > 1 and len(defi[0]) < 270: return defi[0].encode('utf8') + "; " + defi[1].encode('utf8')
    return defi[0].encode('utf8')
    
def translate(args,user="",hostmask="",extra={}):
    #Translate phrase to_lan=<> from_lan=<>
    args = args+" "
    lan = args.split(" ")
    to_lan = "auto"; from_lan = "auto"
    for i in lan:
        if i.startswith("to_lan="):
            to_lan = i.split("=")[1]
        elif i.startswith("from_lan="):
            from_lan = i.split("=")[1]
    args = args.replace("from_lan="+from_lan,"")
    args = args.replace("to_lan="+to_lan,"")
    return general.translate(args, to_lan, from_lan)
    
def element(args,user="",hostmask="",extra={}):
    return elements.getElement(args)

#GEOIP-------------------------
def DMS(degree):
    #Returns DMS for degree
    degree = Decimal(degree)
    d = Decimal(math.floor(degree))
    m = (degree - d)*Decimal("60")
    m = Decimal(math.floor(m))
    s = (degree - d - m/Decimal("60"))*Decimal('3600')
    return d,m,s


# def geoip(args,user="",hostmask="",extra={}):
#     #GEOIP <USER>
#     #Replace with http://ipinfo.io/ ?
    
#     if len(re.findall('[a-zA-Z]+',args)) > 0:
#         args = socket.gethostbyname(args)
            
#     match = geolite2.lookup(args)
#     if match == None: return "Could not geoip the given ip address."
    
#     coords = match.location
#     c1 = DMS(coords[0]); c2 = DMS(coords[1])
#     googleUrl = "https://www.google.com/maps/place/{}%20{}'{}%22N+{}%20{}'{}%22E".format(c1[0],c1[1],round(c1[2],3),c2[0],c2[1],round(c2[2],3))
#     if c1[0] < 0: googleUrl = "https://www.google.com/maps/place/{}%20{}'{}%22S+{}%20{}'{}%22E".format(abs(c1[0]),c1[1],round(c1[2],3),c2[0],c2[1],round(c2[2],3))
#     if c2[0] < 0: googleUrl = googleUrl.replace("+-","+").replace("E","W")
#     googleUrl = web.isgd(googleUrl)
    
#     return "\x02Ip: \x0f{} | \x02Subdivision: \x0f{} | \x02Country: \x0f{} | \x02Continent: \x0f{} | \x02Map: \x0f {} | \x02Location: \x0f {} | \x02Time Zone: \x0f {}".format(
#         match.ip,
#         str(match.subdivisions).replace("frozenset([","").replace("])",""),
#         match.country,
#         match.continent,
#         googleUrl,
#         match.location,
#         match.timezone
#     )
    
def geoip(args,user="",hostmask="",extra={}):
    result = util.gethostmask(args,extra["ircsock"].ircsock)
    isUser = False
    if result:
        args = result.split("@")[1].replace("gateway/web/cgi-irc/kiwiirc.com/","").replace("gateway/web/freenode/ip.","")
        isUser = True
    
    try:
        if len(re.findall('[a-zA-Z]+',args)) > 0:
            try: args = socket.gethostbyname(args)
            except: pass
        response = requests.get("http://ipinfo.io/"+args)
        info = response.json()
        
        coords = info["loc"].split(",")
        c1 = DMS(coords[0]); c2 = DMS(coords[1])
        googleUrl = "https://www.google.com/maps/place/{}%20{}'{}%22N+{}%20{}'{}%22E".format(c1[0],c1[1],round(c1[2],3),c2[0],c2[1],round(c2[2],3))
        if c1[0] < 0: googleUrl = "https://www.google.com/maps/place/{}%20{}'{}%22S+{}%20{}'{}%22E".format(abs(c1[0]),c1[1],round(c1[2],3),c2[0],c2[1],round(c2[2],3))
        if c2[0] < 0: googleUrl = googleUrl.replace("+-","+").replace("E","W")
        try: googleUrl = web.tinyurl(googleUrl)
        except: 
            try: googleUrl = web.isgd(googleUrl)
            except: pass
        
        returned = "\x02Location: \x0f{}, {}, {} {} | \x02Hostname: \x0f{} ({}) | \x02Provider: \x0f{} | \x02Maps: \x0f{} ({})".format(
            info.get("city") or "[Unknown]",
            info.get("region") or "[Unknown]",
            info.get("country") or "[Unknown]",
            info.get("postal") or "[Unknown]",
            
            info.get("hostname") or "[Unknown]",
            info.get("ip") or "[Unknown]",
            info.get("org") or "[Unknown]",
            googleUrl,
            info.get("loc") or "[Unknown]"
        )
        return returned
    except:
        if isUser: return "Hostmask found or could not get ip address info."
        
        
def attack(args,user="",hostmask="",extra={}):
    attacks = [
        "drops a cool black planet on {}",
        "eats {} for breakfast.",
        "tackles {} and annihilates {} completely, ending {}'s thoughts of revenge. ",
        "smashes {}'s face through 4 layers of glass.",
        "whacks {} into space.",
        "breathes out a stream of white hot fire, melting {}'s face instantly.",
        "takes out a sharpness V sword and slices {} in half.",
        "detonates an antimatter missile onto {}.",
        "fires the B.E. Space Laser, shooting a beam of death towards {}.",
        "takes the brush and drops some SING near where {} was standing.",
        "borrows a banhammer and smashes it on {}'s skull.",
        "beats {} in a game of chess, causing {} to die of shame.",
        "forces {} to listen to Justin Bieber, causing their eardrums to explode.",
        "shoves {} into a vat of sodium hydroxide.",
        "types /kill @p[Name={}]",
        "types !set type {} none in the console.",
        "straps {} onto a rocket heading towards the sun.",
        "drops an anvil onto {}, cracking their skull",
    ]
    
    return "\x01ACTION "+random.choice(attacks).format(args)+ "\x01"