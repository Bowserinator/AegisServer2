import transport, brew
import data

brew = brew.brew()

def phraseText(text, username): #Match text query
    text = text.replace("my",username).replace("me",username)
    
    result = transport.phraseInput(text,username)
    if result: 
        result2 = ""
        for x in result[0]: result2 += " ".join(x) + " | "
        return {"output":result2, "input":result[1]}
    
    result = data.phraseData(text)
    if result: return {"input":text,"output":result}
    
    elif "brew" in text:
        result = brew.brew(text.split("brew")[1])
        if result["name"] != "" and result["possible"]: 
            return {"output": "\x02Time\x0f" + " | " + str(result["time"]) + " seconds  " + "\x02Steps\x0f| " + ", ".join(result["steps" ]), 
                    "input": "Brew a {0}".format(result["name"]) }
        return {"input":"Brew an [invalid] potion", "output":"<Unable to brew>"}