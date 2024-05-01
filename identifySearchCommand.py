def identifySearchC(questr):
    questr=questr.lower()
    if(questr.startswith("google")):
        nqs=questr.replace('google ','',1)
        return nqs
    else:
        return "not google command"
    
# print(identifySearchC("search hanuman chalisa"))