import random, math, re

trans_num = ["(pi)","(e)","sin(35)","cos(15)","sin(75)","cos(75)"]

def listIn(l1,l2, anti=False):
    #If item in l1 in l2
    for i in l1:
        if not anti:
            if i in l2:
                return True
        elif anti:
            if "non " + i in l2 or "non"+i in l2 or "non-"+i in l2:
                return True
            if "not "+i in l2 or "not"+i in l2:
                return True
    return False

def isSpecial(requirements):
    if requirements["perfect"] or requirements["prime"] or requirements["square"] or requirements["cube"]:
        return True
    return False
    
def randomSquare(r1,r2,nonsquare=False):
    if r1 == 0: r1+=1
    if nonsquare:
        return random.randint(r1,math.floor(math.sqrt(r2)))**2 -1
    return random.randint(r1,math.floor(math.sqrt(r2)))**2

def randomCube(r1,r2,nonsquare=False):
    if r1 == 0: r1+=1
    if nonsquare:
        return random.randint(r1,math.floor(math.sqrt(r2)))**3 -1
    return random.randint(r1,math.floor(math.sqrt(r2)))**3
    
def isPrime(i):
    if i<=1:
        return False
    for j in range(2,int(math.floor(math.sqrt(i)))):
        if i%j == 0:
            return False
    return True
    
def randomPrime(r1,r2):
    if r2-r1 > 2000:
        r2 = r1+2000
    primes = [i for i in range(r1,r2) if isPrime(i)]
    if primes == []:
        return "Could not generate such prime number."
    n = random.choice(primes)
    return n

def randomPerfect(r1,r2): 
    #All perfect numbers in form 2^p * (2^p -1) if 2^p - 1 is prime
    mersenne_prime_powers = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521,
                   607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937,
                   21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433,
                   1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011,
                   24036583, 25964951]
    possible = []
    for p in mersenne_prime_powers:
        result =  2**(p-1)*(2**(p) - 1)
        if result >= r1 and result <= r2:
            possible.append(result)
    if possible != []:
        return random.choice(possible)
    return "No such known perfect number was found."
    
def randomFraction(r1,r2):
    if r1 == 0:
        r1 += 1
    return str(random.randint(r1,r2*2)) + "/" + str(random.randint(r1,r2*2))


def randomNumberText(text):
    returned = ""
    
    requirements = {
        "integer":True, #done
        "float":False, #done
        "complex":False, #done
        "range":[0,10000],
        "prime":False, #done
        "irrational":False, #done
        "fractional":False, #done
        "trans":False, #done
        "square":False, #done
        "cube":False, #done
        "perfect":False, #done
        "imaginary":False #done
    }
    
    if listIn(["whole number","integer","whole-number"],text,True):
        requirements["integer"] = False
        requirements["float"] = True
    elif listIn(["whole number","integer","whole-number"],text):
        requirements["integer"] = True
        requirements["float"] = False
        
    if listIn(["float","decimal"],text,True):
        requirements["float"] = False
        requirements["integer"] = True
    elif listIn(["float","decimal"],text):
        requirements["float"] = True
        requirements["integer"] = False
        
    if listIn(["complex"],text,True): requirements["complex"] = False
    elif listIn(["complex"],text): requirements["complex"] = True
    
    if listIn(["natrual"],text,True): 
        requirements["integer"] = False
        requirements["float"] = True
    elif listIn(["natrual"],text): 
        requirements["integer"] = True
        requirements["float"] = False
        requirements["range"][0] = 1
    
    if listIn(["fraction","fractional"],text,True): requirements["fractional"] = False
    elif listIn(["fraction","fractional"],text): requirements["fractional"] = True
    if listIn(["prime"],text,True): requirements["prime"] = False
    elif listIn(["prime"],text): requirements["prime"] = True
    if listIn(["square"],text,True): requirements["square"] = False
    elif listIn(["square"],text): requirements["square"] = True
    if listIn(["irrational"],text,True): requirements["irrational"] = False
    elif listIn(["irrational"],text): requirements["irrational"] = True
    if listIn(["cube"],text,True): requirements["cube"] = False
    elif listIn(["cube"],text): requirements["cube"] = True
    if listIn(["trans"],text,True): requirements["trans"] = False
    elif listIn(["trans"],text): requirements["trans"] = True
    if listIn(["perfect"],text,True): requirements["perfect"] = False
    elif listIn(["perfect"],text): requirements["perfect"] = True
    if listIn(["imaginary"],text,True): requirements["imaginary"] = False
    elif listIn(["imaginary"],text): requirements["imaginary"] = True
    
    if listIn(["real"],text,True): 
        requirements["imaginary"] = True
    elif listIn(["real"],text): 
        requirements["imaginary"] = False
    
        
    text2 = text.split(" ")
    try: min_num = text2[text2.index("less")+2]
    except:
        try: max_num = text2[text2.index("less")+2]
        except: 
            try: max_num = text2[text2.index("smaller")+2]
            except: pass
    try: max_num = text2[text2.index("more")+2]
    except: 
        try: max_num = text2[text2.index("larger")+2]
        except: 
            try: max_num = text2[text2.index("bigger")+2]
            except: pass
        
    
    try: 
        max_num = int(text2[text2.index("between")+1])
        min_num = int(text2[text2.index("between")+3])
    except: pass

    try: requirements["range"][0] = int(max_num)
    except: pass
    try: requirements["range"][1] = int(min_num)
    except: pass



    #The non-negative and stuff
    if listIn(["nonnegative"],text): 
        requirements["range"][0] = 0
        requirements["range"][1] = abs(requirements["range"][1])
    elif listIn(["positive"],text): 
        requirements["range"][0] = 1
        requirements["range"][1] = abs(requirements["range"][1])
    elif listIn(["nonpositive"],text): 
        requirements["range"][0] = 0
        requirements["range"][1] = -abs(requirements["range"][1])
    elif listIn(["negative"],text): 
        requirements["range"][0] = -1
        requirements["range"][1] = -abs(requirements["range"][1])
        
    #Test for conflicts
    possible = True
    if requirements["prime"] and requirements["float"]:
        possible = False
    elif requirements["trans"] and (requirements["float"] or requirements["integer"]):
        possible = False
    elif requirements["float"] and requirements["integer"]:
        possible = False
    elif requirements["complex"] and requirements["real"]:
        possible = False
    elif requirements["imaginary"] and requirements["real"]:
        possible = False
            
    #Create the actual number
    r = requirements["range"]
    input_int = []

    if requirements["complex"]: #An complex number
        if requirements["prime"] or requirements["square"] or requirements["cube"] or requirements["perfect"]:
            returned = "Could not create a complex number satisfying the requirements."; input_int.append("properties that can not be applied to a complex number.")
            
        if requirements["irrational"]: 
            if not isSpecial(requirements): returned = "sqrt("+str(randomSquare(r[0],r[1],True)) + ") + sqrt(" + str(randomSquare(r[0],r[1],True)) + ")i"; input_int.append("irrational, complex")
        elif requirements["fractional"]:
            if not isSpecial(requirements): returned = randomFraction(r[0],r[1]) + " + " + randomFraction(r[0],r[1]) + "i"; input_int.append("fractional, complex")
        elif requirements["trans"]:
            if not isSpecial(requirements): returned = random.choice(trans_num) + " + " + random.choice(trans_num) + "i"; input_int.append("transcendental, complex")
        elif requirements["float"]: 
            if not isSpecial(requirements): returned = str(random.uniform(r[0],r[1]/2.0)) + " + " + str(random.uniform(r[0],r[1]/2.0)) + "i"; input_int.append("float, complex")
        elif requirements["integer"]:
            if not isSpecial(requirements): returned = str(random.randint(r[0],r[1]/2)) + " + " + str(random.randint(r[0],r[1]/2)) + "i"; input_int.append("integer, complex")
  
    else:
        #If it's imaginary just add an i at the end
        if requirements["irrational"]: 
            if not isSpecial(requirements): returned = "sqrt("+str(randomSquare(r[0],r[1],True)) + ")"; input_int.append("irrational")
            else: returned = "This number can not be generated."; input_int.append("irrational")
        elif requirements["fractional"]:
            if not isSpecial(requirements): returned = randomFraction(r[0],r[1]); input_int.append("fraction")
            else: returned = "This number can not be generated."; input_int.append("fraction")
            
        elif requirements["trans"]:
            if not isSpecial(requirements): returned = random.choice(trans_num) ; input_int.append("transcendental")
            else: returned = "This number can not be generated."; input_int.append("that can not be applied to a transcendental number.")
        elif requirements["float"]: 
            if not isSpecial(requirements): returned = str(random.uniform(r[0],r[1]/2.0)); input_int.append("float")
            else: returned = "This float can not be generated."; input_int.append("that can not be applied to a float.")
        elif requirements["integer"]:
            if not isSpecial(requirements): returned = str(random.randint(r[0],r[1]/2)) ; input_int.append("integer")
            else:
                if requirements["square"]: returned = str(randomSquare(r[0],r[1])); input_int.append("square")
                elif requirements["perfect"]: returned = str(randomPerfect(r[0],r[1])); input_int.append("perfect")
                elif requirements["prime"]: returned = str(randomPrime(r[0],r[1])); input_int.append("prime")
                elif requirements["cube"]: returned = str(randomCube(r[0],r[1])); input_int.append("cube")
                
        #Adds i if imaginary
        if requirements["imaginary"]: 
            returned = returned + "i"
            input_int.append("imaginary")
    
    if not possible:
        returned = "The number is impossible to generate."
    input_int = "Generate a random number, range {0} to {1} and properties {2}".format(r[0],r[1],", ".join(input_int))
    return {"output":returned,"input":input_int}