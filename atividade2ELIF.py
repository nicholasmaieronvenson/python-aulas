notas1 = float(input("DIGITE SUA NOTA: "))
notas2 = float(input("digite sua nota: "))
notas3 = float(input("digite sua nota: "))
media = (notas1 + notas2 + notas3) /3
print (f"media = {media}")
if media > 4.9 :
    print ("passou")
elif media == 10  :
    print ("nota perfeita")
else :
    print ("reprovou")
if media >= 9.0 :
    print ("nota A") 
elif media >= 8 :
    print ("nota B")
elif media >= 7 :
    print ("nota C")
elif media >= 6 :
    print ("nota d")
else :
    print ("nota F")
