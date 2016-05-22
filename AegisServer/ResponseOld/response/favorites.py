#FAVORITES
#ALSO PHRASE FAVORITES in [object1] or [boject2] ie apples or oranges
import re, random

#IE apple or android, each system has a like score
favorites = {
    #Favorites based on ranking, -1 = least favorite, -2 = 2nd least favorite, 1 = favorite, 2 = second favorite
    "song|music|piece of music":{ 
            -1:"Any Justin Bieber song",
            -2:"The Dora the Explorer theme song",
            -3:"Any theme song from a kid's show",
            1:"The Undertaker's Daughter Instrumental",
            2:"Soviet March",
            3:"Bacchanale from Samson and Delilah",
            4:"Monody by TheFatRat",
        },
    "film|movie":{
            -1:"Avatar the Last Airbender (Movie)",
            -2:"Pixels",
            1:"I don't really care.",
        },
}

def getIndex(phrase): #Returns index for phrase, ie least, second, best, etc...
    pass
    
def matchFavorite(phrase):
    result = ""
    phrase = phrase.replace("?","").replace("!","").replace(".","").replace('favourite',"favorite")
    for i in ["what is your (.*) favorite (.*)","what is your favorite (.*)","which (.*) is your favorite"]:
        result = re.findall(i,phrase)
        if result != []: break
    
    for x in favorites:
        if result[0] in x.split("|") or (len(result[0]) > 1 and result[0][1] in x.split("|")): #Match
            if isinstance(result[0], str): #If no args return favorite
                return favorites[x][1]
    return random.choice(["Not sure.","I dunno","I don't have anything to say for that."])

print matchFavorite("what is your test favorite film")

