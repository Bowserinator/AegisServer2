

class User(object):
    def __init__(self,name):
        self.name = name
        self.timers = [] #Timers are like [ {"type":"alarm|countdown|timer","sound":true, "time":0:00} ] 
        self.call = "" #What to call the bot
        self.todo = [] #TODO list
        self.lists = [] #Lists to keep, like {"name":"Shopping1","list":[]}
        self.ranking = 0 #Loses/gains with insults and good queries