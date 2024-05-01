def identifyOpenC(questr):
    questr=questr.upper()
    if(questr.startswith("OPEN")):
        nqs=questr.replace('OPEN ','',1)
        return nqs
    else:
        return "not open command"
    
# print(identifyOpenC("open word"))