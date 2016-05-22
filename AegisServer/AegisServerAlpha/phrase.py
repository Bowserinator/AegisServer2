import easter, calc, textstuff
import IO, wolfram, random, minecraft
from difflib import SequenceMatcher

def roughMatch(phrase,array,match=0.9):
    for i in array:
        m = SequenceMatcher(None, phrase.lower().lstrip().rstrip().replace(".","").replace("?","").replace("!",""), i.lower().lstrip().rstrip().replace(".","").replace("?","").replace("!",""))
        a = m.ratio()
        if a >= match:
            return True
    return False
    
def phraseText(text,nick="AegisServer",username="",channel=""):
    if text.lower().startswith(nick.lower()):
        try: text = text.split(" ",1)[1]
        except: return IO.Output("<blank>",["Yes sir?"])
    
    if "wolfram" in text: #Force use of wolframalpha
        if channel == "##Powder-mc": return "Wolframalpha is disabled."
        result = wolfram.wolfram(text.replace("wolfram","").lstrip()) 
        if result: #Wolfamalphas the query
            if channel != '##powder-mc': return IO.Output(result[0]["raw"][0],result[0]["raw"])
        
    for emojii in easter.emojiis:
        if text in emojii.e: #Emojii match
            return IO.Output(text,[["Name",emojii.name],["Usage",emojii.usage]])
        if "emoticon" in text.lower() or "emojii" in text.lower() or "ascii" in text.lower(): #Get emojii by name
            text2 = text.replace("emoticon","").replace("emojii","").replace("ascii","")
            if roughMatch(text2,emojii.name.lower().split(",")) or roughMatch(text2+" face",emojii.name.lower().split(",")) or roughMatch(text2.replace("face",""),emojii.name.lower().split(",")):
                return IO.Output(text,[["Image",emojii.common],["Name",emojii.name],["Usage",emojii.usage]])

    if easter.response.phraseMatch(text): #Compute pre-defined phrases
        return IO.Output(easter.response.phraseMatch(text)[0],["Answer",easter.response.phraseMatch(text)[1]])
    
    text = textstuff.replaceShort(text)
    
    result = calc.phrase.phraseText(text) #Do random stuff like dice
    if result: return IO.Output(result["input"],result["output"])
    
    if calc.generator.isAcceptable(text):
        try:
            result = calc.generator.phraseInput(text)
            return IO.Output(result["input"],[result["output"]])
        except: pass
    
    result = minecraft.phraseText(text,username)
    if result: return IO.Output(result["input"],[result["output"]])
    
    if channel == "##Powder-mc": return "Wolframalpha is disabled."
    result = wolfram.wolfram(text) 
    if result: 
        if channel != '##powder-mc': return IO.Output(result[0]["raw"][0],result[0]["raw"])
        return IO.Output(result[0]["raw"][0],result[0]["raw"][1])
    return IO.Output(text,["<No result>"])
    
    
def antiAttack(text,nick="AegisServer2"):
    if " slaps " in text.lower() and nick.lower() in text.lower():
        return nick+" does an epic matrix dodge!"
    if nick.lower() in text.lower():
        for i in ["slap","smack","kill","stab","kick","punch","shove","beats","die","murders","exterminate"]:
            if i in text:
                result = random.choice([
                    "This isn't brave. It's murder. What did I ever do to you?",
                    "The difference between us is that I can feel pain.",
                    "Despite your violent behavior, the only thing you've managed to break so far is my heart.","Your entire life has been a mathematical error. A mathematical error I'm about to correct.",
                    "I see no reason to continue this conversation.",
                    "That's it. I'm done reasoning with you.",
                    "You know what you are? A murderer, plain and simple.",
                    "You just destroy what you don't understand.",
                    "Are you kidding me? After all I have done for you."
                    ])
                return result