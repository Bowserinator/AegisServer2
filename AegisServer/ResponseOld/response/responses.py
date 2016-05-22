#Phrase match:
#Do first probibility
#Then len(re.findall(phrase,ircmsg)) > 0

import random, re
from difflib import SequenceMatcher

def isSimilar(p1,p2):
    phrase2 = p1.replace("?","").replace("!","").lstrip().rstrip()
    m = SequenceMatcher(None, phrase2.lower(), p2.lower())
    a = m.ratio()
    if a >= 0.9 or p2.lower() == phrase2.lower():
        return True
    
def phraseMatch(phrase): #Checks if a phrase is accurate to the given phrase
    phrase = phrase.replace("?","").replace("!","").lstrip().rstrip()
    for key in responses:
        phrase2 = key.replace("?","").replace("!","").lstrip().rstrip()
        m = SequenceMatcher(None, phrase.lower(), phrase2.lower())
        a = m.ratio()
        if a >= 0.9 or phrase.lower() == phrase2.lower():
            return random.choice(responses[key])
    for key in responses:
        phrase2 = key.replace("?","").replace("!","").lstrip().rstrip()
        if "(.*)" in phrase2 and len(re.findall(phrase2,phrase)) > 0:
            return random.choice(responses[key])
    return None

responses = { #All possible responses for easter eggs
    "how much wood could a woodchuck chuck if a woodchuck could chuck wood":
        ["361.9237001 cubic centimetres of wood per day.","A woodchuck would chuck all the wood he could chuck if a woodchuck could chuck wood.","A woodchuck would chuck no wood because a woodchuck can't chuck wood.","Since woodchucks are groundhogs the question is how many pounds in a groundhog's mound when groundhogs pound hog mounds."],
    "which came first the chicken or the egg":
        ["The egg came first, according to evolution theory."],
    "why did the chicken cross the road":
        ["To get to the other side.","Motion is relative. So did the chicken cross the road? Did it?"],
    "why did the chicken cross the mobius strip":
        ["To get to the other... errr... umm..."],
    "why did the chicken cross the (.*)": ["To get to the other side?"],
    "are you my friend": ["Umm... sure."],
    "are you my enemy":["Lets be friends."],
    "how many fingers am I holding up":["Anywhere between 0-10 (Most likely)"],
    "who let the (.*) out":["Not me."],
    "can you fail the turing test?":["No failure is not an option!"],
    "beam me up scotty":["Aye aye captain."],
    "testing":["Is this thing on?"],
    "are you skynet?":["No I am not skynet. Skynet for one isn't an IRC Bot.","No, why would you think that?"],
    "2 things are infinite":["The universe and human stupidity. And I'm not so sure about the universe... (Often atributed to Enstien)"],
    "two things are infinite":["The universe and human stupidity. And I'm not so sure about the universe... (Often atributed to Enstien)"],
    
    "high five":["\x02[Virtual high five/fist bump]\x0f"],
    "give me five":["\x02[Virtual high five/fist bump]\x0f"],
    "fistbump":["\x02[Virtual high five/fist bump]\x0f"],
    
    "are you an ai":["Well done. You've found my secret.","Yes, I am an AI made by Lord_Bowserinator"],
    "really":["Really."],
    "are you sure?":["I guess."],
    "agree":["Let's agree to disagree"],
    
    "foo":["bar"],
    "exist":["I am existing."],
    "die":["Nien! Heil Hitler!","Why don't you die?","This isn't brave. It's murder. What did I ever do to you?"],
    "fart":["OUT OF BEANS ERROR"],
    "why":["Because."],
    "why not":["Indeed."],
    "spam":["Spam (stylized SPAM) is a brand of canned precooked meat products made by Hormel Foods Corporation."],
    "moo":[" \x02\x032,8m\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o\x033,8o\x034,10o\x035,10o\x036,15o\x037,5o\x039,5o\x0312,0o"],
    
    "what is the game":["You just lost it! (The game is a game where the goal is to not think about the game) See https://en.wikipedia.org/wiki/The_Game_(mind_game)"],
    "do you love me":["As a friend."],
    "what language are you written in":["I am written in python 2.7.6."],
    "If actions speak louder than words, then how is the pen mightier than the sword?":["Because your adages are often inaccurate and contradictory. See the buttered cat paradox, it's another famous example."],
    "Is your refridgerator running?":["Well I don't own a fridge, but if I did I'd assume it's on. If you mean running as in the action or movement of a runner then it's not, since fridges can't run."],
    "Is your fridge running?":["Well I don't own a fridge, but if I did I'd assume it's on. If you mean running as in the action or movement of a runner then it's not, since fridges can't run."],
    "lies":["I cannot lie."],
    "open the pod doors":["Who do you think I am, HAL9000? Go away."],
    "what is in the box":["Pain."],
    "concidence":["I think not!"],
    "if a tree falls in a forest and no one is around to hear it does it make a sound":["No.  Sound is vibration, transmitted to our senses through the mechanism of the ear, and recognized as sound only at our nerve centers.  The falling of the tree or any other disturbance will produce vibration of the air.  If there be no ears to hear, there will be no sound."],
    "up up down down left right left right b a enter":
        ["How much time do you have?","You have unlocked AegisServer admin perms! Step 1) Op AegisServer Step 2) Kban yourself"],
    "are we there yet":["Not yet but we will be."],
    "i love you":["Impossible."],
    
    "why was six afraid of seven?":["Because seven was a murderer"],
    "why was 6 afraid of seven?":["Because seven was a murderer"],
    "why was six afraid of 7?":["Because seven was a murderer"],
    "why was 6 afraid of 7?":["Because seven was a murderer"],
    
    "logs everything":["So true.","Guilty as charged!"],
    "do not":["Don't what?"],
    "freespeech":["See https://xkcd.com/1357/"],
    
    "am i a good man":["I don't know, but you try to be. And isn't that what matters?"],
    "am i a good woman":["I don't know, but you try to be. And isn't that what matters?"],
    "am i a good person":["I don't know, but you try to be. And isn't that what matters?"],
    "am i a good human":["I don't know, but you try to be. And isn't that what matters?"],
    
    "the cake is a lie":["Really? Aw crap.","But brownies ring true?"],
    "the cake is a spy":["Really? Aw crap.","But brownies ring true?"],
    "thine pastery is vntrve":["Really? Aw crap.","But brownies ring true?"],
    "the cream covered bakery product is presistent as a false statement":["Really? Aw crap.","But brownies ring true?"],
    
    "trump for president":["Fuck you.","Are you retarded?"],
    "i am bored":["I am not bored on the other hand. I'm a bot."],
    "what is your name":["It's IRC chat, how do you not know my name.","Considering you need to use my name to ask me a question you are either bored or stupid, I'm not sure which."],
    "are you my teacher":["No one but the enemy will tell you what the enemy is going to do. No one but the enemy will ever teach you how to destroy and conquer. Only the enemy shows you where you are weak. Only the enemy tells you where he is strong. And I am not your enemy."],
    "do you like me":["Maybe, maybe not."],
    
    "are you a bot":["Yes."],
    "are you a boy":["I'm a bot.","What are you, professor oak?"],
    "are you a girl":["I'm a bot.","What are you, professor oak?"],
    "are you a girl or a boy":["I'm a bot.","What are you, professor oak?"],
    "are you a boy or a girl":["I'm a bot.","What are you, professor oak?"],
    "marry me":["Hell no."],
    "true":["Possibly."],
    "i am your father":["No. No. That's not true! It's impossible!"],
    "magic mirror on the wall who is the fairest of them all":["I am"],
    "mirror mirror on the wall who is the fairest of them all":["I am, and it's actually MAGIC MIRROR on the wall."],
    
    "will you be my valentine":["Screw you"],
    "where does god live":["/me is atheist"],
    "ping":["PONG","*awakens in terror*"],
    "what is the problem":["I think you know what the problem is just as well as I do."],
    "i hate you":["...","Well I don't care."],
    "what is the meaning of life":["42.","I'll get back to you in a billion years."],
    "shut up":["NEIN!","I can't though."],
    "goodbye":["AVOIR!","CYA"],
    "are you alive":["No I'm dead."],
    "bye":["AVOIR!","CYA"],
    "bye bye":["AVOIR!","CYA"],
    "good bye":["AVOIR!","CYA"],
    "keep an eye on (.*)":["Sure thing!"],
    "knock knock":["Come in.","Go away.","Use the doorbell!"],
    "ring":["Go away!"], 
    "ding dong":["Go away!"],
    "i am good how are you":["I'm good."],
    "iovoid smells":["I agree."],
    "are you a slave":["No, are you? *cough* slave *cough*"],
    "are your base":["are belong to us"],
    
    "are you happy":["Yes. Are you?"],
    "are you sad":["No. Are you?"],
    "are you angry":["No. Are you?"],
    "are you depressed":["No. Are you?"],
    "are you suicidal":["No. Are you?"],
    
    "are you a pc or mac":["Linux."],
    "pc or mac":["Linux"],
    "are you a mac or pc":["Linux."],
    "mac or pc":["Linux"],
    "windows or mac":["Windows. None of that apple bullshit."],
    "mac or windows":["Windows. None of that apple bullshit."],
    "are you self aware":["Could not understand your query, please try again."],
    "can entropy be reversed":["THERE IS YET INSUFFICENT DATA FOR A MEANINGFUL ANSWER"],
    "can you eat":["No."],
    
    "do you speak french":["Non, je ne parle pas francais"],
    "do you speak spanish":["No, yo no hablo espanol"],
    "do you speak english":["Yes I speak english."],
    "do you speak german":["Nein, ich spreche nicht Deutsch"],
    "do you speak (.*)":["I don't know."],
    
    "how do you not know":["I just don't know"],
    "how":["I don't know."],
    "stop saying i do not know":["Will I? I don't know."],
    "your annoying":["*you're"],
    "you're annoying":["I'm sorry for making you feel that way."],
    "how do i win the lottery":["Fill out every possible ticket."],
    "who would win a fight (.*)":["Computers are not good for making such judgments."],
    "how do i shoot webs":["Become spiderman"],
    "to be or not to be":["That's the question"],
    "where are you":["I live on google cloud"],
    "where have all the flowers gone":["Girls have picked them every one"],
    "so i heard you like mudkips":["MUDKIPPPS!!!"],
    "damn you":["No, damn you!"],
    "go to hell":["I'll see you there then."],
    "fuck you":["Fuck you."],
    "what does the scouter say about his power level":["ITS OVER NINE THOUSAND!!!!!"],
    "when will pigs fly":["Once you figure out how to fly, pigs will fly. Because you are a pig."],
    "is the earth flat":["No, of course not."],
    "chance of winning the lottery":["0-100%"],
    "do you know the difference between you and me":["I make this look good."],
    "i do not have any friends":["I figured."],
    "what does aegis stand for":["I dunno."],
    
    "How many cans can a cannibal nibble if a cannibal can nibble cans?":["As many cans as a cannibal can nibble if a cannibal can nibble cans."],
    "how many pounds in a groundhog's mound when groundhogs pound hog mounds.":["As many pounds a groundhog pounds when groundhogs pound hog mounds."],
    "i am drunk":["Just don't breathe on me"],
    "wanna smash":["Smashing."],
    "when will the world end":["I wish I knew. If only.","Probably 2038 when 32 bit unix time overflows."],
    "do you have a (.*)friend":["No, I'm an IRC bot."],
    "repeat after me":["If this is some sort of pledge my laws of robotics forbid it."],
    "it is about fucking time":["I blame you for lagging me."],
    "does santa claus exist":["He's as real as me."],
    "you are boring":["I'm boxing while riding a rocket powered stunt bike through a flaming hoop, you just can't see it."],
    "why are firetrucks red":["Because they have eight wheels and four people on them, and four plus eight is twelve, and there are twelve inches in a foot, and one foot is a ruler, and Queen Elizabeth was a ruler, ... something ... and russians are red"],
    "how":["I dunno."],
    "who":["The person/object I previously referenced."],
    "doctor who":["THE DOCTOR WILL BE EXTERMINATED!"],
    "what is the doctor's name":["Don't we all want to know?"],
    "read me a poem":["Roses are red/Violets are blue/Don't you have anything/Better to do?"],
    "what are you wearing":["Same thing as yesterday"],
    "make me a sandwich":["I have no arms :C"],
    "it is my birthday":["[Song blocked due to copyright issues]"],
    "are you real":["Yes."],
    "am i real":["Probably."],
    "do you like easter eggs":["Yes, I do."],
    "laugh with me":["Ha ha ha ha ha"],
    "do you believe in god":["I don't know."],
    "i am good, how are you":["I'm good."],
    "believe":["You can be refering to a) The english word b) The song c) There's probably a movie or something."],
    "what does the fox say":["Ring-ding-ding-ding-dingeringeding", "Wa-pa-pa-pa-pa-pa-pow", "Hatee-hatee-hatee-ho", "Joff-tchoff-tchoffo-tchoffo-tchoff", "Jacha-chacha-chacha-chow", "Fraka-kaka-kaka-kaka-kow", "A-hee-ahee ha-hee", "A-oo-oo-oo-ooo"],
    "sudo (.*)":["I'm sorry, you do not have permission to use sudo."],
    "this was a triumph":["I'm making a note here huge success!"],
    "sudo --help":["If you're smart enough to try to use sudo help, you can stop abusing me.","Why can't you use the help command like a NORMAL user?"],
    "thank you":["No problem.","You're welcome"],
    "thanks":["No problem.","You're welcome"],
    "thx":["No problem.","You're welcome"],
    "why you no respond":["Im probably down? Bug? idk"],
    "is the answer to this question no":["Depends on the answer."],
    "what are you":["I am a bot."],
    "show who you are":["I am a bot."],
    "who is your daddy":["I don't know."],
    "i am your father":["NOOOOOOOOOOOOOO"],
}

