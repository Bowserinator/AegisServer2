
#http://people.math.sc.edu/girardi/m142/handouts/10sTaylorPolySeries.pdf
from decimal import Decimal
import math, constant

class ComparasionError(Exception):
    pass

class Number(object):
    def __init__(self,positive,imaginary="0.0"):
        self.real = Decimal(positive)
        self.imaginary = Decimal(imaginary)
    
    def phase(self): #Returns "angle" in radians
        return math.atan2(self.imaginary, self.real)
    def polar(self): #Converts to polar
        return (abs(self), self.phase())
    def toRect(self,r,phi):
        return Number(r) * Number(math.cos(phi) , math.sin(phi))
        
    def exp(self): #Returns e**x
        e = Decimal(constant.constants["E"])
        if self.imaginary == 0:
            return Number(e**(self.real),0)
        return Number(e**(self.real) * Decimal(math.cos(self.imaginary)), e**(self.real) * Decimal(math.sin(self.imaginary)))
    def conj(self):
        return Number(self.real,-self.imaginary)
        
    def floor(self):
        return Number(self.real.to_integral(), self.imaginary.to_integral())
        
    def ceil(self):
        return Number(math.ceil(self.real),math.ceil(self.imaginary))
        
    #Trig and log/log10/ln
    #http://mathonweb.com/help_ebook/html/complex_funcs.htm
    def ln(self):
        if self.imaginary == 0:
            try: return Number(math.log(self.real))
            except: pass
        p = self.polar()
        return Number(math.log(p[0]), p[1])
        
    def log(self,x=10):
        if self.imaginary == 0:
            try: return Number(math.log(self.real,x))
            except: pass
        p = self.polar()
        return Number(math.log(p[0],x), p[1])
        
    def log10(self):
        if self.imaginary == 0:
            return Number(math.log10(self.real))
        return Number(self.ln() / Number(math.log(10)))
        
    def sin(self):
        if self.imaginary == 0:
            return Number(math.sin(self.real))
        try: return Number(math.sin(self.real) * math.cosh(self.imaginary), math.cos(self.real) * math.sinh(self.imaginary))
        except: return Number("inf")
        
    def cos(self):
        if self.imaginary == 0:
            return Number(math.cos(self.real))
        try: return Number(math.cos(self.real) * math.cosh(self.imaginary), -math.sin(self.real) * math.sinh(self.imaginary))
        except: return Number("inf")
    
    def tan(self):
        try: return self.sin() / self.cos()
        except: return Number("inf")
        
    def acos(self):
        if self.imaginary == 0:
            return Number(math.acos(self))
        A = Number(((Decimal(1) + self.real)**Decimal(2) + self.imaginary**Decimal(2))**Decimal(0.5) - ((Decimal(1) - self.real)**Decimal(0.5) + self.imaginary**Decimal(2))**Decimal(0.5)) / Number(2)
        B = Number(((Decimal(1) + self.real)**Decimal(2) + self.imaginary**Decimal(2))**Decimal(0.5) + ((Decimal(1) - self.real)**Decimal(0.5) + self.imaginary**Decimal(2))**Decimal(0.5)) / Number(2)
        return Number(A.acos(), -(B+(B*B - Number(1))**Number(0.5)).ln() )
        
    def asin(self):
        if self.imaginary == 0:
            return Number(math.asin(self))
        A = Number(((Decimal(1) + self.real)**Decimal(2) + self.imaginary**Decimal(2))**Decimal(0.5) - ((Decimal(1) - self.real)**Decimal(0.5) + self.imaginary**Decimal(2))**Decimal(0.5)) / Number(2)
        B = Number(((Decimal(1) + self.real)**Decimal(2) + self.imaginary**Decimal(2))**Decimal(0.5) + ((Decimal(1) - self.real)**Decimal(0.5) + self.imaginary**Decimal(2))**Decimal(0.5)) / Number(2)
        return Number(A.asin(), (B+(B*B - Number(1))**Number(0.5)).ln() )
    
    def atan(self):
        result = (Number(0,1)+self) / (Number(0,1) - self)
        return Number(0,0.5) * result.ln()
        
    def cosh(self):
        if self.imaginary == 0:
            return Number(math.cosh(self.real))
        try: return Number(math.cosh(self.real) * math.cos(self.imaginary), math.sinh(self.real) * math.sin(self.imaginary))
        except: return Number("inf")
        
    def sinh(self):
        if self.imaginary == 0:
            return Number(math.sinh(self.real))
        try: return Number(math.sinh(self.real) * math.cos(self.imaginary), math.cosh(self.real) * math.sin(self.imaginary))
        except: return Number("inf")
        
    def tanh(self):
        try: return self.sinh() / self.cosh()
        except: return Number("inf")
        
    def acosh(self):
        returned = self + (self*self - Number(1))**0.5
        return returned.ln()
        
    def asinh(self):
        returned = self + (self*self + Number(1))**0.5
        return returned.ln()
    def atanh(self):
        a = (Number(1)+self).ln() - (Number(1)-self).ln()
        return Number(0.5) * a
        
    #Builtin functions
    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        return (str(self.real)+"+"+str(self.imaginary)+"i").replace("+-","-")
        
    def __abs__(self):
        return (self.real**2 + self.imaginary**2).sqrt()
    def __add__(self,other):
        return Number(self.real+other.real, self.imaginary+other.imaginary)
    def __sub__(self,other):
        return Number(self.real-other.real, self.imaginary-other.imaginary)
    def __mul__(self,other):
        if self.imaginary == 0 and other.imaginary == 0:
            return Number(self.real*other.real,"0")
        return Number( self.real*other.real - self.imaginary*other.imaginary,self.real*other.imaginary + self.imaginary*other.real )
    def __div__(self,other):
        if self.imaginary == 0 and other.imaginary == 0:
            return Number(self.real/other.real,"0")
        a = (self.real*other.real + self.imaginary*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary)
        b = (self.imaginary*other.real - self.real*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary)
        return Number(a,b)
    def __truediv__(self,other):
        if self.imaginary == 0 and other.imaginary == 0:
            return Number(self.real/other.real,"0")
        a = (self.real*other.real + self.imaginary*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary)
        b = (self.imaginary*other.real - self.real*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary)
        return Number(a,b)
    def __neg__(self):
        return Number(-self.real,-self.imaginary)
    def __pos__(self):
        return Number(self.real,self.imaginary)
    def __inverse__(self):
        return Number(1)/self
    def __mod__(self,other):#a%b = a + b * ciel(-a/b) 
        return self+ other* ((-self/other).ceil())
    def __pow__(self,other):
        if other.imaginary == 0:
            polar = self.polar()
            return self.toRect(Decimal(polar[0])**other.real, Decimal(polar[1])*other.real)
        elif other.real == 0:
            a = Number(self.real); b = Number(self.imaginary)
            c = Number(other.real); d = Number(other.imaginary)
            x = (-d * (b/a).atan()).exp() * ((a*a+b*b).ln() * d / Number(2)).cos() 
            y = Number(0,1) * (-d * (b/a).atan()).exp() * ((a*a+b*b).ln() * d / Number(2)).sin()
            return x+y

        b = other.real; c = other.imaginary
        #a^(b+c) = a^b * a^ci
        return self**(Number(b)) * self**(Number(0,1) * Number(c))
  
    def __complex__(self):
        return complex(float(self.real),float(self.imaginary))
    def __int__(self):
        return int(self.real)
    def __float__(self):
        return float(self.real)
    
    #Comparasions
    def __lt__(self,other): #>
        if self.imaginary != 0 or other.imaginary != 0:
            raise ComparasionError("Complex comparasion is not supported")
        return self.real < other.real
        
    def __le__(self,other): #>=
        if self.imaginary != 0 or other.imaginary != 0:
            raise ComparasionError("Complex comparasion is not supported")
        return self.real <= other.real
        
    def __eq__(self,other): #==
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        return False
    def __ne__(self,other): #!=
        return not self.__eq__(other)
        
    def __gt__(self,other): #<
        if self.imaginary != 0 or other.imaginary != 0:
            raise ComparasionError("Complex comparasion is not supported")
        return self.real > other.real
        
    def __ge__(self,other): #<=
        if self.imaginary != 0 or other.imaginary != 0:
            raise ComparasionError("Complex comparasion is not supported")
        return self.real >= other.real
        
