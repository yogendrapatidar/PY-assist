# qs="play gayatri mantra"
# qs=qs.lower()
# print(qs)

# pl=qs.startswith("play")
# print(pl)

# if(qs.startswith("play")):
#     nqs=qs.replace('play ','',1)
#     print(nqs)
# else:
#     print("not a music command")


def identifyMusic(questr):
    questr=questr.lower()
    if(questr.startswith("play")):
        nqs=questr.replace('play ','',1)
        return nqs
    else:
        return "no music"
    
# print(identifyMusic("hanuman chalisa"))
