#Example phrase: one million twenty two
#Replace all and spaces with "" NOT HYPENS, as subtraction
#Replace one -> + 1, two -> + 2, ... ninety-nine -> + 99 ... nine hundred ninety nine -> + 999
#Replaec stuff like thousand with * 1000
#ie one million twenty two -> 1 * 1000000 + 22

import math
import re

try: numberWords = open("mathwords.txt","r").readlines()
except: numberWords = open("Database/response/mathwords.txt","r").readlines()
numberWords.reverse()
multipliers = {
    "thousand":1000,
    "million":1000000,
    "billion":1000000000,
    "trillion":1000000000000,
    "quadrillion":1000000000000000,
    "quintillion":1e18,
    "sextillion":1e21,
    "septillion":1e24,
    "octillion":1e27,
    "nonillion":1e30,
    "decillion":1e33,
}

def delQuestion(string):
    words = ["what","how","when","who","where","is","the","calculate","evaluate","eval","calc","value","number","quantity","of","result","answer","equation","for","is","an"]
    for i in words:
        string = string.replace(i,"")
    return string.lstrip().rstrip()
    
def isMath(string):
    string = string.lower()
    for i in ["plus","minus","times","divided by","factorial","squared","cubed","to the power of","sin","cos","tan","sqrt","+","-","/","*","^","=","1","2","3","4","5","6","7","8","9","0"]:
        if i in string:
            return True
    for key in multipliers:
        if key in string:
            return True
    for key in numberWords:
        if key in string:
            return True
    return False
    

def strToInt(string): 
    """Makes a string with number words into numbers
    Hardly perfect, but who inputs with words anyways?"""
    
    string = string.lower()
    string = string.replace("plus","+").replace("minus","-").replace("times","*").replace("divided by","/").replace("over","/").replace("multiplied by","*")
    string = string.replace("^","**").replace("to the power of","**").replace('factorial','!').replace("squared","**2").replace("cubed","**3")
    p = re.compile(ur'((?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety) (?:\S+ )?(?:thousand|million|billion|trillion|quadrillion|quintillion|sixtillion|septillion|octillion|nonillion|decillion))')
    subst = u"(\1)"
    result = re.findall(p,string)
    result.sort(key = len); result.reverse()

    for x in result:
        string = string.replace(x,"("+x+")")

    string = string.replace(" ","")
    for key in multipliers:
        string = string.replace(key,"*"+str(multipliers[key]))
    for n in numberWords: #Replaces inital words
        string = string.replace(n.split(":")[0],"+"+n.split(":")[1].replace("\n",""))
    
    while "++" in string:
        string = string.replace("++","+")
    while "***" in string:
        string = string.replace("***","**")
    if string[0] == "+":
        string = "0"+ string
    return string
