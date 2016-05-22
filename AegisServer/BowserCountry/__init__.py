import generator, random, simulation

execfile("BowserCountry/generator.py")
import json

def commandMakeCountry(text,user="",hostmask="",extra={}):
    #Create country: Name, type
    args = text.split(',')
    args[0] = args[0].replace("\\","")
    countries = json.loads(open("BowserCountry/data.txt",'r').read())
    if hostmask.lower() in countries:
        extra["ircsock"].sendmsg(extra["channel"], "You already have a country registered called the {0}.".format(countries[hostmask.lower()]["name"]))
        return None
    
    for key in countries:
        if countries[key]["name"].lower() == args[0].lower():
            extra["ircsock"].sendmsg(extra["channel"],"Name is taken already.")
            return None
    try: 
        countries[hostmask.lower()] = createCountry(args[0], hostmask.lower(), int(args[1]))
        extra["ircsock"].sendmsg(extra["channel"], "You have successfully created a new country called the {0}".format(args[0]) )
    except: extra["ircsock"].sendmsg(extra["channel"], "Invalid args, use createCountry <name>,<type 0=democracy 1=republic 2=dictatorship 3=empire>")
    
    result = json.dumps(countries, sort_keys=True, indent=4, separators=(',', ': '))
    file = open("BowserCountry/data.txt",'w')
    file.write(result)
    file.close()
    