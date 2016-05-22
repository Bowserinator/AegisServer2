from difflib import SequenceMatcher
import math,random

class MathPhrase(object):
    def __init__(self):
        pass
    
    def roughMatch(self,phrase,array,match=0.9):
        for i in array:
            m = SequenceMatcher(None, phrase.lower().lstrip().rstrip().replace(".","").replace("?","").replace("!",""), i.lower().lstrip().rstrip().replace(".","").replace("?","").replace("!",""))
            a = m.ratio()
            if a >= match:
                return True
        return False
    
    def eightball(self):
        choices=  [
            "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
            ]
        return random.choice(choices)
    
    def phraseText(self,text):
        n1 = 6; n2 = 1
        for t in text.split(" "):
            if "side" in t:
                try: n1 = int(float( text.split(" ")[text.split(" ").index(t)-1] ))
                except: pass
            if "time" in t:
                try: n2 = int(float( text.split(" ")[text.split(" ").index(t)-1] ))
                except: pass
        if "twice" in text: n2 = 2
        elif "once" in text: n2 = 1
        elif "thrice" in text: n2 = 3
        
        if n1 <= 0 or n2 <= 0:
            return {"input":"Row or flip a [impossible] die/coin an [impossible] number of times","output":[["Analysis","[Not possible]"]]}
        
        if n2 > 1000000:
            return {"input":"Row or flip a coin/dice [large number] of times","output":[["Analysis","Number too large"]]}
        if n1 > 1000000:
            return {"input":"Row a [large number] sided dice","output":[["Analysis","Number too large"]]}
            
        if "flip " in text and " coin" in text:
            returned = [];
            for i in xrange(0,n2):
                returned.append(random.choice(["heads","tails"]))
            
            data = "[Removed due to spam limits]"
            if n2 < 31: 
                data = ", ".join(returned).replace("heads","H").replace("tails","T")
            percent_heads = str(float(returned.count("heads")) * 100 / len(returned)) + "%"
            percent_tails = str(float(returned.count("tails")) * 100 / len(returned)) + "%"
            output = [["Results",data] , ["Percent heads",percent_heads], ["Percent tails",percent_tails], ["Expected heads",str(len(returned)/2.0)] ]
            return {"input":"Flip a coin {0} times".format(n2), "output":output}
            
        elif "die" in text or "dice" in text:
            returned = [];
            for i in xrange(0,n2):
                returned.append(str(random.randint(0,n1)))
            
            data = "[Removed due to spam limits]"
            if n2 < 31: 
                data = ", ".join(returned)
            average = float(sum( [int(x) for x in returned] )) / len(returned) 
            output = [["Results",data] , ["Average value",str(average)], ["Expected value",str(n1/2.0)]]
            return {"input":"Toss a {0} sided dice {1} times".format(n1,n2), "output":output}
            
        elif "eightball" in text or "eight ball" in text or "8ball" in text or "8 ball" in text:
            return {"input":"Shake a magic eight ball","output":[self.eightball()]}

