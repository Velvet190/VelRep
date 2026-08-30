def addition(*nombres):
    res = 0
    for nombre in nombres:
        res += nombre
    return(res)

def afficher_infos(**infos):
    print(infos)