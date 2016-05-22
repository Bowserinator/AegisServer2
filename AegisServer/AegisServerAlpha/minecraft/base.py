class Base(object):
    def __init__(self,x,y,z,users=[],world="overworld",biome=None,type=None,name=""):
        self.x = x
        self.y = y
        self.z = z
        self.biome = biome
        self.type = type
        self.users = users
        self.name = name
        

#Also has farms, which are bases with name of thing, ie "enderman farm as name"
bases = [
    Base(-65,65,-214,["iovoid","bwbellairs","robotronmc","bowserinator","chessking","chessking345","jeda","jedayoshi","nberry","nberry13"],"overworld","Plains","Open air","Azure"),
    Base(-2700,65,-1500,["cracker64","jacob1","jacob614"],"overworld","Mushroom","Open Air","jacob base"),
    Base(-860,65,1260,["Smitr","Ximon","Simon","thewaxmann"],"overworld","Savannah","Open air","waxmann base"),
    Base(1200,65,-770,["Sg_voltage"],"overworld","Ocean","Floating island","voltage base"),
    
    #The farms
    Base(-1690,65,669,[],"overworld","Ocean","Open air","guardian farm"),
    Base(257,65,0,[],"end","End","Open air","enderman farm"),
    Base(257,65,0,[],"end","End","Open air","endermen farm"),
    Base(-74,65,-72,[],"nether","Nether","House","end portal"),
]