def identifyCloseC(questr):
    questr=questr.upper()
    if(questr.startswith("CLOSE")):
        nqs=questr.replace('CLOSE ','',1)
        return nqs
    else:
        return "not close command"
    
# print(identifyCloseC("close word"))