seuNumero = 0
numeroSecreto = 8
while numeroSecreto != seuNumero:
    seuNumero = int(input("digite o seu numero: " ))
    if seuNumero == numeroSecreto:
        print ("acertou miséravi")
    elif seuNumero < numeroSecreto :
        print ("tente um número maior")
    else:
        print ("tente um número menor")
    
