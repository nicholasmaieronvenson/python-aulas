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
