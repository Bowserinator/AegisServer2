

def romanNumeral(num): 
    #Converts romanNumerals to int
    #Credit to http://codereview.stackexchange.com/questions/5091/converting-roman-numerals-to-integers-and-vice-versa
    #For the code
    
    string = num.upper()
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:
        continueyes=True
        while continueyes:
            if len(string)>=len(pair[0]):
                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]
                else: 
                    continueyes=False
            else: 
                continueyes=False
    return returnint