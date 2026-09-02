objetos = ["Vaso", "Televisão", "Laser", "Cadeira"]
pontos = 0
for objeto in objetos:
    print (f"objeto: {objetos}, pontos: {pontos}")
    destruiçao = int(input("escolha o objeto que o coots vai destruir digitando seu index: "))
    if destruiçao <0 or destruiçao>len(objetos)-1:
        print ("coots errou e não quebrou nada")
    else :
        print (f"coots quebrou o objeto {objetos[destruiçao]}")
        pontos +=100
print (f"o coots conseguiu esses pontos: {pontos}")        
    
    
