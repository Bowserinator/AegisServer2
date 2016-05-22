import random

def generateState(): #Random state abbrevation, ie NY or NT
    letters = "qwertyuiopasdfghjklzxcvbnm".upper()
    return letters[random.randint(0,25)] + letters[random.randint(0,25)]

def generatePostal():
    return "".join([str(random.randint(0,9)) for i in range(0,5)])

def generateCityName():
    cities = [
        'Aachen', 'Ahaus', 'Altentreptow', 'Altotting', 'Amberg', 'Angermunde',
        'Anklam', 'Ansbach', 'Apolda', 'Arnstadt', 'Artern', 'Aschaffenburg',
        'Aue', 'Auerbach', 'Augsburg', 'Aurich', 'Backnang', 'Bad Bruckenau',
        'Bad Freienwalde', 'Bad Kissingen', 'Bad Kreuznach', 'Bad Langensalza',
        'Bad Liebenwerda', 'Bad Mergentheim', 'Badalzungen', 'Badibling',
        'Badoberan', 'Bamberg', 'Bautzen', 'Bayreuth', 'Beeskow', 'Beilngries',
        'Belzig', 'Berchtesgaden', 'Bergzabern', 'Berlin', 'Bernburg',
        'Bersenbruck', 'Biedenkopf', 'Bischofswerda', 'Bitterfeld', 'Bogen',
        'Borken', 'Borna', 'Brand', 'Brandenburg', 'Bremen', 'Bremervorde',
        'Brilon', 'Bruchsal', 'Burg', 'Burgdorf', 'Burglengenfeld',
        'Boblingen', 'Busingenm Hochrhein', 'Butzow', 'Calau', 'Calw', 'Celle',
        'Chemnitz', 'Cloppenburg', 'Coburg', 'Cottbus', 'Crailsheim',
        'Cuxhaven', 'Dachau', 'Darmstadt', 'Deggendorf', 'Delitzsch', 'Demmin',
        'Dessau', 'Dieburg', 'Diepholz', 'Dinkelsbuhl', 'Dinslaken',
        'Donaueschingen', 'Dresden', 'Duderstadt', 'Dobeln', 'Duren',
        'Ebermannstadt', 'Ebern', 'Ebersberg', 'Eberswalde', 'Eckernforde',
        'Eggenfelden', 'Eichstatt', 'Eichstatt', 'Eilenburg', 'Einbeck',
        'Eisenach', 'Eisenberg', 'Eisenhuttenstadt', 'Eisleben', 'Emmendingen',
        'Erbisdorf', 'Erding', 'Erfurt', 'Erkelenz', 'Euskirchen', 'Eutin',
        'Fallingbostel', 'Feuchtwangen', 'Finsterwalde', 'Floha', 'Forchheim',
        'Forst', 'Freising', 'Freital', 'Freudenstadt', 'Fulda',
        'Furstenfeldbruck', 'Furstenwalde', 'Fussen', 'Gadebusch',
        'Gardelegen', 'Garmisch-Partenkirchen', 'Geithain', 'Geldern',
        'Gelnhausen', 'Genthin', 'Gera', 'Germersheim', 'Gerolzhofen',
        'Gieben', 'Gifhorn', 'Goslar', 'Gotha', 'Grafenau', 'Gransee',
        'Greifswald', 'Greiz', 'Grevenbroich', 'Grevesmuhlen',
        'Griesbach Rottal', 'Grimma', 'Grimmen', 'GroB-Gerau', 'GroBenhain',
        'Grafenhainichen', 'Guben', 'Gunzenhausen', 'Goppingen', 'Gorlitz',
        'Gottingen', 'Gunzburg', 'Gustrow', 'Gutersloh', 'Hagenow',
        'Hainichen', 'Halberstadt', 'Haldensleben', 'Hamburg', 'Hammelburg',
        'Hannover', 'Hannoversch Munden', 'Hansestadttralsund', 'Havelberg',
        'Hechingen', 'Heiligenstadt', 'Heinsberg', 'Helmstedt', 'Herford',
        'Hersbruck', 'Herzberg', 'Hettstedt', 'Hildburghausen', 'Hildesheim',
        'Hofgeismar', 'Hohenmolsen', 'Hohenstein-Ernstthal', 'Holzminden',
        'Hoyerswerda', 'Husum', 'Hoxter', 'Hunfeld', 'Illertissen', 'Ilmenau',
        'Ingolstadt', 'Iserlohn', 'Jena', 'Jessen', 'Julich', 'Juterbog',
        'Kaiserslautern', 'Kamenz', 'Karlsruhe', 'Kassel', 'Kehl', 'Kelheim',
        'Kemnath', 'Kitzingen', 'Kleve', 'Klotze', 'Koblenz', 'Konstanz',
        'Kronach', 'Kulmbach', 'Kusel', 'Kyritz', 'Konigs Wusterhausen',
        'Kotzting', 'Leipziger Land', 'Lemgo', 'Lichtenfels', 'Lippstadt',
        'Lobenstein', 'Luckau', 'Luckenwalde', 'Ludwigsburg', 'Ludwigslust',
        'Lorrach', 'Lubben', 'Lubeck', 'Lubz', 'Ludenscheid', 'Ludinghausen',
        'Luneburg', 'Magdeburg', 'Main-Hochst', 'Mainburg', 'Malchin',
        'Mallersdorf', 'Marienberg', 'Marktheidenfeld', 'Mayen', 'Meiningen',
        'MeiBen', 'Melle', 'Mellrichstadt', 'Melsungen', 'Meppen', 'Merseburg',
        'Mettmann', 'Miesbach', 'Miltenberg', 'Mittweida', 'Moers', 'Monschau',
        'Muhldorfm Inn', 'Muhlhausen', 'Munchen', 'Nabburg', 'Naila', 'Nauen',
        'Neu-Ulm', 'Neubrandenburg', 'Neunburg vorm Wald', 'Neuruppin',
        'Neuss', 'Neustadtm Rubenberge', 'Neustadtner Waldnaab', 'Neustrelitz',
        'Niesky', 'Norden', 'Nordhausen', 'Northeim', 'Nordlingen',
        'Nurtingen', 'Oberviechtach', 'Ochsenfurt', 'Olpe', 'Oranienburg',
        'Oschatz', 'Osterburg', 'Osterodem Harz', 'Paderborn', 'Parchim',
        'Parsberg', 'Pasewalk', 'Passau', 'Pegnitz', 'Peine', 'Perleberg',
        'Pfaffenhofenner Ilm', 'Pinneberg', 'Pirmasens', 'Plauen', 'Potsdam',
        'Prenzlau', 'Pritzwalk', 'PoBneck', 'Quedlinburg', 'Querfurt',
        'Rastatt', 'Rathenow', 'Ravensburg', 'Recklinghausen', 'Regen',
        'Regensburg', 'Rehau', 'Reutlingen', 'Ribnitz-Damgarten', 'Riesa',
        'Rochlitz', 'Rockenhausen', 'Roding', 'Rosenheim', 'Rostock', 'Roth',
        'Rothenburg oberauber', 'Rottweil', 'Rudolstadt', 'Saarbrucken',
        'Saarlouis', 'Sangerhausen', 'Sankt Goar', 'Sankt Goarshausen',
        'Saulgau', 'Scheinfeld', 'Schleiz', 'Schluchtern', 'Schmolln',
        'Schongau', 'Schrobenhausen', 'Schwabmunchen', 'Schwandorf',
        'Schwarzenberg', 'Schweinfurt', 'Schwerin', 'Schwabisch Gmund',
        'Schwabisch Hall', 'Sebnitz', 'Seelow', 'Senftenberg', 'Siegen',
        'Sigmaringen', 'Soest', 'Soltau', 'Soltau', 'Sondershausen',
        'Sonneberg', 'Spremberg', 'Stade', 'Stade', 'Stadtroda',
        'Stadtsteinach', 'Staffelstein', 'Starnberg', 'StaBfurt', 'Steinfurt',
        'Stendal', 'Sternberg', 'Stollberg', 'Strasburg', 'Strausberg',
        'Stuttgart', 'Suhl', 'Sulzbach-Rosenberg', 'Sackingen', 'Sommerda',
        'Tecklenburg', 'Teterow', 'Tirschenreuth', 'Torgau', 'Tuttlingen',
        'Tubingen', 'Ueckermunde', 'Uelzen', 'Uffenheim', 'Vechta',
        'Viechtach', 'Viersen', 'Vilsbiburg', 'VohenstrauB', 'Waldmunchen',
        'Wanzleben', 'Waren', 'Warendorf', 'Weimar', 'WeiBenfels',
        'WeiBwasser', 'Werdau', 'Wernigerode', 'Wertingen', 'Wesel', 'Wetzlar',
        'Wiedenbruck', 'Wismar', 'Wittenberg', 'Wittmund', 'Wittstock',
        'Witzenhausen', 'Wolfach', 'Wolfenbuttel', 'Wolfratshausen', 'Wolgast',
        'Wolmirstedt', 'Worbis', 'Wunsiedel', 'Wurzen', 'Zerbst', 'Zeulenroda',
        'Zossen', 'Zschopau',
    ]
    
    city_prefixes = ['North', 'East', 'West', 'South', 'New', 'Lake', 'Port']
    city_suffixes = [
        'town', 'ton', 'land', 'ville', 'berg', 'burgh', 'borough', 'bury', 'view', 'port', 'mouth', 'stad', 'furt',
        'chester', 'mouth', 'fort', 'haven', 'side', 'shire']
        
    returned = ""
    if random.random() < 0.3:
        returned = returned + random.choice(city_prefixes) + " "
    returned = returned + random.choice(cities)
    if random.random() < 0.3:
        returned = returned + random.choice(city_suffixes)
    return returned.encode('utf8')

def createCountry(name,hostmask,ctype):
    #Possible ctypes: 0 = democracy 1 = dictatorship 2 = empire
    
    returned = {
        "name":name,
        "hostmask":hostmask,
        "owner":hostmask,
        "type":ctype,
        "cities":{},
        "total_population":100000000,
        "money": 100000000000,
        "pollution" : 10.0, #Pollution index, 0 - 100, humans die at 100, 0 = nature.
        "imports" : 0,  #Money made /lost in imports
        "exports" : 0,  #Money made in exports
        
        "nationalism": 0,
        "support": 0.5,
        "crime_rate": 0.2,
        "tech_level":80, #80 = industrial revolution, 0 = stone age, 100 = 2000s
        
        "inventory" : {},
        "cities":{},
        
        "structures": {
            "hydro_dam":0,
            "nuclear_plant":0,
            "coal_plant": 100,
            "solar_plant":0,
            "wind_plant":0,
            
            "mines":100,
            "factories":100,
            "clean_factories":10,
            "military_bases":10,
            "bunkers":10,
            "labs":10,
            "air_scrubbers":0
            },
        "major_structures": {
            "temples":0,
            "particle_collider":0,
            "radio_telescope":0,
            },
        "weapons" : {
            "people":0, #Soilders
            "missile":0,
            "tanks":0, #vechicles
            "bioweapon":0,
            "ships":0,
            "aircraft":0,
            "nukes":0
            }
    }
    
    #Randomly add 5 cities, change population accordingly
    for i in range(0,20):
        returned["cities"][str(generateCityName())] = {
            "population":random.randint(200000,2000000),
        }
    for key in returned["cities"]:
        returned["total_population"] += returned["cities"][str(key)]["population"]
        
    return returned

