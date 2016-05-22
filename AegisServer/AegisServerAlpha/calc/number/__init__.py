#http://people.math.sc.edu/girardi/m142/handouts/10sTaylorPolySeries.pdf
from decimal import Decimal
import decimal, fractions
import math, number, constant, re

import sys
sys.setrecursionlimit(20000)

def log(n,x):return n.log(x)
def phase(n):return n.phase()
def exp(n):return n.exp()
def floor(n):return n.floor()
def ceil(n):return n.ceil()
def ln(n):return n.ln()
def log10(n):return n.log10()

def sin(n):return n.sin()
def cos(n):return n.cos()
def tan(n):return n.tan()
def asin(n):return n.asin()
def acos(n):return n.acos()
def atan(n):return n.atan()
def sqrt(n): return n**number.Number(0.5)

def sinh(n):return n.sinh()
def cosh(n):return n.cosh()
def tanh(n):return n.tanh()
def asinh(n):return n.asinh()
def acosh(n):return n.acosh()
def atanh(n):return n.atanh()

def radian(n):
    return n * number.Number(constant.constants["pi"]) / number.Number(180)
def degree(n):
    return n * number.Number(180) / number.Number(constant.constants["pi"])
    
def factorial(n):
    if n.imaginary != 0:
        raise ArithmeticError("You cannot have imaginary factorial.")
    if n < number.Number(0): raise ArithmeticError("You cannot have negative factorial.")
    if n < number.Number(2): return number.Number(1)
    return n * factorial(n - number.Number(1))
    
def double_fact(n):
    if n.imaginary != 0:
        raise ArithmeticError("You cannot have imaginary factorial.")
    if n < number.Number(0): raise ArithmeticError("You cannot have negative factorial.")
    if n < number.Number(2): return number.Number(1)
    return n * (double_fact(n-number.Number(2)))
    
def computeEquation(m,modes=""):
    if "the meaning of life" in m: return number.Number(42)
    
    #Replace the constants
    for c in constant.constants:
        m = m.replace(c,constant.constants[c])
    m = m.replace("^","**")
    m = m.replace("_","").replace("import","").replace("decode","").replace("encode","").replace("open","")
    
    #Change double factorials, ie 5!! -> double_fact(5)
    p = re.compile(ur'(-?\d+)!!'); subst = r"double_fact(\1)"; m = re.sub(p, subst, m)
    p = re.compile(ur'\((.?)\)!!'); subst = r"double_fact(\1)"; m = re.sub(p, subst, m)
    #Change factorials, ie 5! -> fact(5)
    p = re.compile(ur'(-?\d+)!'); subst = r"factorial(\1)"; m = re.sub(p, subst, m)
    p = re.compile(ur'\((.?)\)!'); subst = r"factorial(\1)"; m = re.sub(p, subst, m)
    
    m = m.replace("||"," or ").replace("|"," or ")
    m = m.replace("&&"," and ").replace("&"," and ")
    
    #Converts e notation, ie 2e9 to 2 * 10**9, because errors and stuff
    p = re.compile(ur'([:]?\d*\.\d+|\d+)e([-+]?)([-+]?\d*\.\d+|\d+)'); subst = r"\1 * 10**\2\3"
    m = re.sub(p, subst, m)
    
    #Converts all remaining numbers into numbers
    p = re.compile(ur'([:]?\d*\.\d+|\d+)'); subst = r"number.Number('\1')"
    m = re.sub(p, subst, m)
    
    #Fix up i
    m = m.replace(")i",")*number.Number(0,1)")
    m = m.replace('in','@')
    p = re.compile(ur'(?<![a-zA-Z])i'); subst = u"number.Number(0,1)"
    m = re.sub(p, subst, m)
    m = m.replace("@","in")
    
    safe_dict = {}
    safe_dict["sin"] = sin
    safe_dict["cos"] = cos
    safe_dict["tan"] = tan
    safe_dict["asin"] = asin
    safe_dict["acos"] = acos
    safe_dict["atan"] = atan
    
    safe_dict["sinh"] = sinh
    safe_dict["cosh"] = cosh
    safe_dict["tanh"] = tanh
    safe_dict["asinh"] = asinh
    safe_dict["acosh"] = acosh
    safe_dict["atanh"] = atanh
    
    safe_dict["sqrt"] = sqrt
    safe_dict["abs"] = abs
    safe_dict["log"] = log
    safe_dict["fact"] = factorial
    safe_dict["factorial"] = factorial
    safe_dict["double_fact"] = double_fact
    safe_dict["ceil"] = ceil
    safe_dict["floor"] = floor
    safe_dict["exp"] = exp
    safe_dict["log10"] = log10
    
    safe_dict["deg"] = degree
    safe_dict["rad"] = radian
    safe_dict["degrees"] = degree
    safe_dict["radians"] = radian
    safe_dict["number"] = number
    result = eval(m, {"__builtins__": None}, safe_dict)
    return result
    
def phraseTextMath(text,user="",hostmask="",extra={}):
    showPrec = 5
    showMode = "SCI"
    for i in ["SCI","FRACT"]:
        if i in text:
            showMode = i; text = text.replace(i,"")
    r2 = re.findall("TRUNCT=([:]?\d*\.\d+|\d+)",text)
    for r in r2: showPrec = int(float(r)); text = text.replace("TRUNCT="+r,"")
    r2 = re.findall("DIGIT=([:]?\d*\.\d+|\d+)",text)
    for r in r2: showPrec = int(float(r)); text = text.replace("DIGIT="+r,"")
    try:
        decimal.getcontext().prec = 100
        text = computeEquation(text)
        if type(text) in (tuple,list):
            text = '['+', '.join( [ (format(a.real, '.{}f'.format(showPrec)) + "+" + format(a.imaginary, '.{}f'.format(showPrec)) + "i").replace("+-","-") for a in text])+']'
        elif type(text) == dict:
            return "Sorry dictionaries are currently not supported."
        else:  
            if showMode == "FRACT":
                text = "\x02Answer: \x0f" + (str(fractions.Fraction(float(text.real))) + "+" + str(fractions.Fraction(float(text.imaginary)))+ "i").replace("+-","-")
            elif showPrec == -1:
                text = "\x02Answer: \x0f" + str(text)
            else: text = "\x02Answer: \x0f" + (format(text.real, '.{}f'.format(showPrec)) + "+" + format(text.imaginary, '.{}f'.format(showPrec)) + "i").replace("+-","-") 
        text = text.replace('number.Number','')
        returned = text[:700]
        if len(text) > 700: returned = returned + "..."
        return returned
    except ZeroDivisionError:
        return "\x02\x034Error: \x0fCannot divide by zero."
    except OverflowError:
        return "\x02\x034Error: \x0fNumber overflowed."
    except ArithmeticError as e:
        return "\x02\x034Error: \x0f{0}".format(e)
    except ValueError as e:
        return "\x02\x034Error: \x0fMath Domain Error."
    except Exception as e:
        return "\x02\x034Error: \x0fCould not understand input."
    