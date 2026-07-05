kingCrimson = input("king cimsom ativar? (sim/não) ")
timeErase =  input("time erase ativar? (sim/não) ")
stickFinger = input("stick Finger ativar? (sim/não) ")
requiemSilverChariot = input("requiem silver chariot ativar? (sim/não) ")
goldExperience = input("gold experience ativar? (sim/não) ")
goldExperienceRequiem = input("golden experience requiem ativar? (sim/não) ")
azarDoRequiemSilverChariot = int(input("sorte do requiem silver chariot (0 a 100) "))
if kingCrimson ==  "sim" :
    print ("time erase ativado")
    if  timeErase == "sim" :
        print ("giorrno teve um pouco de problemas") 
    elif  azarDoRequiemSilverChariot >=99 :
        print ("não morreu o requiem silver chariot")
    else :
        print ("requiem silver chariot morreu")
else:
    print (" bucciarati morreu")
if kingCrimson == "não" :
    print ("giorno ganha")
else :
    print ("giorno ganha tbm pq ele é muito forte")
if requiemSilverChariot == "sim" :
    print ("diavolo se lascou")
elif goldExperience == "sim" and goldExperienceRequiem == "sim":
    print ("diavolo ficou no looping")
elif stickFinger == "sim":
    print ("bucciarati  ajudou")
