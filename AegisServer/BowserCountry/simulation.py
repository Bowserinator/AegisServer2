import random, math

def simulateCountry(country,printLog=True):
    logs = ["=====Simulation======"]
    
    if country["total_population"] <= 0: 
        country["total_population"] = 0
        logs.append("Everyone in your country is dead.")
        if printLog: print logs
        return country
    elif country["total_population"] < 1000000:
        country["money"] -= random.randint(50000000,1000000000)
    
    """Simulates the country
    Deaths and population growth
    Crime rates
        PROPORTIONAL TO WEALTH AND POPULATION
    Pollution: DONE :D
    
    Randomizes events such as pademics, disasters
        How government handles based on money and stuff
        How much disaster is based on poorness and living conidtions
    SCientific achievements increase money
    Factories and stuff increase money
    
    Increase buildings and stuff and tech level"""
    
    #POPULATION INCREASE
    #+============================================================================================
    rich = country["money"] / float(country["total_population"])
    if rich >=1: pop_increase = 1 + (1000000/rich - 1)/20000000.0 #Exponentional growth, less money = more people
    else: pop_increase = 1.001
    logs.append("Total population is {0}".format(math.floor(pop_increase*country["total_population"])))
    
    country["total_population"] *=  pop_increase #At some point if your country gets too wealthy people will not increase, around 100 trillion dollars
    country["total_population"] = math.floor(country["total_population"])
    for i in country["cities"]:
        country["cities"][i]["population"] *= pop_increase
        country["cities"][i]["population"] = math.floor(country["cities"][i]["population"])
    
    #Money increase, based on number of factories and stuff
    #============================================================================================
    country["money"] += country["structures"]["factories"]*100000+country["structures"]["clean_factories"]*90000 + country["structures"]["mines"]*random.randint(10000,500000)
    
    #CRIME RATE INCREASE, linear. 
    #============================================================================================
    if rich <= 1:
        country["crime_rate"] = 1
        logs.append("Crime rate changed to {0}%".format(1*100))
    elif rich >= 1000:
        country["crime_rate"] = 0
        logs.append("Crime rate changed to {0}%".format(0))
    else:
        country["crime_rate"] = 1-(rich/1000)
        logs.append("Crime rate changed to {0}%".format((1-(rich/1000)) * 100))
    
    #POLLUTION, gradually decreases always, but will increase with factories/power plants
    #===============================================================================================
    addPollution = (country["structures"]["factories"] + country["structures"]["coal_plant"])*0.000001 + country["structures"]["mines"]*0.0000001 + country["structures"]["air_scrubbers"]*-0.000001
    country["pollution"] += addPollution - 0.00000000001
    logs.append("Pollution changed to {0}".format((country["pollution"] + addPollution  - 0.00000000001)) )
    
    #POLLUTION FAILURE
    #+==============================================================================================
    if country["pollution"] >= 100:
        total_minus = 0
        for i in country["cities"]:
            minus = random.randint(10000,1000000)
            if country["cities"][i]['population'] - minus > 1000-country["pollution"]:
                country["cities"][i]['population'] -= minus
                country["total_population"] -= minus
                total_minus += minus
        if country['total_population'] - minus > 1000-country["pollution"]:
            total_minus += minus
            country["total_population"] -= minus
        logs.append("Pollution levels are at dangerous levels, {0} people have died so far.".format(total_minus))

    
    #DISASTERS
    #Pademic, 
        #Azure virus, everyone turns into a cow
        #BIoweapon attacks too :D
    #Nuclea rpowerplant failure: minus money
    #Justin Bieber visits
    #earthquake <-> tsunami, hurricane
    #STOCK market crash, terriost attacks
    #===============================================================================================
    
    #Earthquakes: Average 2 major earthquakes a year
    if random.random() <= 2.0/(365): #Subtract money, lives, randomly damage strucutres
        logs.append("A major earthquake has hit your country.")
        minus_money = random.randint(100000000,10000000000)
        country["money"] -= minus_money
        logs.append("${0} was lost because of earthquake damages.".format(minus_money))
        
        total_minus = 0
        for i in country["cities"]:
            minus = random.randint(10000,1000000)
            country["cities"][i]['population'] -= minus
            country["total_population"] -= minus
            total_minus += minus
        logs.append("{0} lives were lost in total".format(total_minus))
    
    logs.append("Total wealth: ${0}".format(country["money"]))
        
    if printLog: print logs
    return country