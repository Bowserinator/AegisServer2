#Makes random numbers based on input
import random, randomint

class RandomText(object):
    def __init__(self):
        pass
    
    def isAcceptable(self,text):
        #Returns if the input is a random number request
        if "random" in text or "generate" in text:
            return True
        return False
        
    def phraseInput(self,text):
        
        #Returns an output which will become the output object
        #An dict { "input": "", "output": []}
    
        #Test conflicts, ie prime and nonprime conflict, prime and square only if 1or0, etc...
        #Also generate: random string, random fake data, etc...
        #Generate n random integers or floats (0-1000),(0-1) for floats and find sum/average
        
        #Integers ======================================================
        return randomint.randomNumberText(text)
    
