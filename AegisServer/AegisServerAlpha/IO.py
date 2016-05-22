

class Output(object):
    def __init__(self,input_int,output):
        self.input_int = input_int
        self.output = output #an array, ie [["name","poop"]]
        
        """Special codes:
            [image|urlhere] - Display image
            [url|urlhere] - Make link
            [song|songurlhere] - Play song"""
        
    def __str__(self):
        if type(self.output[0]) != str and type(self.output[0]) != int and type(self.output[0]) != float:
            addStr = []
            for key in self.output:
                addStr.append( "\x02"+key[0].replace("\n","").replace("\r","")+"\x0f: " + key[1].replace("\n","").replace("\r",""))
        else:    addStr = [a.replace("\n","").replace("\r","") for a in self.output]
        return "\x02Input: \x0f" + self.input_int + " \x02Output: \x0f" + (" | ".join(addStr)).replace(" |  | "," | ")