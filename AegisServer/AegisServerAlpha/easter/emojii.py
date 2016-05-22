#Solves emjoiis based on description and emjoii itself.

#TODO:
#Texting forms of words, ie thx

#SOCIAL MEDIA ANALYSSI?

class Emojii(object):
    def __init__(self,e,name,usage,common):
        self.common = common #The most common occurence 
        if type(e) == str:
            e = e.split(" ")
            
        #Recreate all emjoiis with nose and different eyes
        e2 = []
        for i in e: 
            e2.append(i)
            e2.append(i.replace(":","="))
            if len(i) in [2,3]: 
                e2.append(i[-2] + ">" + i[-1])
                e2.append(i[-2] + "-" + i[-1])
                e2.append(i[-2] + "c" + i[-1])
                i = i.replace(":","=")
                e2.append(i[-2] + ">" + i[-1])
                e2.append(i[-2] + "-" + i[-1])
                e2.append(i[-2] + "c" + i[-1])
        self.e = e2
        self.name = name
        self.usage = usage
        
emojiis = [
    Emojii(":) :] :} 8D :o","Smile, smilely","Used to express happiness.",":)"),
    Emojii(":D 8D xD XD :3 BD","Laughing, big grin face","Used to express laughter and amusment.",":D"),
    Emojii(":))","Very happy, double chin","Used to express extreme happiness or a double chin.",":))"),
    Emojii(":[ :( :C :< :{","Frown, sad","Used to express sadness.",":("),
    Emojii(";(","Sarcastic frown","Used to express sadness with sarcasm, commonly misunderstood.",";("),
    Emojii(":'(","Crying","Used to express extreme sadness, crying.",":'("),
    Emojii(":')","Tears of happiness","Used to express extreme happiness, joyful crying.",":')"),
    Emojii("D:< D: D8 D; DX v.v D': V_V v_v V.V","Horror, disgust, sadness","Used to express horror, disgust, sadness or great dismay.","D:"),
    Emojii(">:O :O :o 8O O-O O_O o-o o_o o_O O_o","Suprise, shock, yawn.","Used to express suprised, shocked or yawning.",":O"),
    Emojii(":* ('}{')","Couple kissing","Used to express kissing.",":*"),
    Emojii(">:P :P XP :p :b d:","Tongue sticking out","Used to express cheerfulness or playfulness.",":P"),
    Emojii(">:/ >:\\ :. :\\ :/ :L :S >.<","Skeptical, annoyed, undecided, uneasy, hesitant","Used to express annoyance, uneasiness or being skeptical or unsure.",":/"),
    Emojii(":|","Straight face, emotionless, indecision, no expression","Used to show seriousness or indecision",":|"),
    Emojii(":$","Embarrased, blushing","Used to show embarrassment",":$"),
    Emojii(":X :#","Sealed lips, wearing braces","Used to show sealed lips or braces.",":#"),
    Emojii("0:) 0:3 0;)","Angel, halo, saint, innocent","Used to show innocence and goodwill.","0:)"),
    Emojii(">:) >;) (:< >:} >:] [:< {:<","Evil","Used to show malicious desires.",">:)"),
    Emojii("}:) }:D 3:) 3:D","Devil, demon","Used to express extreme evil desires.","}:)"),
    Emojii("o/\o ^5 >->^^<_<","High five","Used to express applause.","o/\o"),
    Emojii("|;) |O","Bored, cool","Used to express bordem.","|O"),
    Emojii(":J","Tongue in cheek","Used to imply that a statement or other production is humorously or otherwise not seriously intended, and it should not be taken at face value.",":J"),
    Emojii(":&","Tongue tied","Used when you are too embarrassed to speak.",":&"),
    Emojii("#) #D","Partied all night","Used to show extreme partying.","#)"),
    Emojii("%)","Drunk","Used to show being drunk or otherwise unable to control one's behavior.","%)"),
    Emojii(":###... :-###...","Being sick, vomitting, throwing up","Used to show vomitting or being sick.",":###..."),
    Emojii("<:|","Dunce, dumb, dunce-like","Used to repersent stupidity.","<:|"),
    Emojii("\o/ \0/","Cheer, yay","Used to repersent cheering.","\o/"),
    Emojii("*\o/* *\0/*","Cheerleader","Used to repersent a cheerleader.","*\o/*"),
    Emojii("@}--;-'--- @>-->--","Rose","Used to repersent a rose, flower or love.","@}--;-'---"),
    Emojii("~(_8^(I)","Homer Simpson","Used to repersent Homer Simpson.","~(_8^(I)"),
    Emojii("5:) ~:\\","Elvis Presley","Used to repersent Elvis Presley.","5:-)"),
    Emojii("//0-0\\\\","John Lennon","Used to repersent John Lennon.","//0-0\\\\"),
    Emojii("*<|:) *<|:-)","Santa, Santa Claus","Used to repersent Santa Claus.","*<|:-)"),
    Emojii("=:o]","Bill Clinton","Used to repersent Bill Clinton.","=:o]"),
    Emojii("':) 7:^]","Ronald Regan","Used to repersent Ronald Regan.","':-)"),
    Emojii("<3","Heart","Used to express love or emotion.","<3"),
    Emojii("</3","Broken heart, heartbreak","Used to express heartbreak.","</3"),
    Emojii("-_-","Seriously, not amused.","Used to repersent not amusment.","-_-"),
    Emojii("(o|o)","Ultraman","Used to express ultraman.","(o|o)"),
    Emojii("(-_-)zzz","Sleep, snore","Used to express sleeping.","(-_-)zzz"),
    Emojii("(>_<) >_<","Troubled, disturbed","Used to express being troubled or distrubed.",">_<"),
    Emojii("(';')","Baby","Used to express a baby.","(';')"),
]


