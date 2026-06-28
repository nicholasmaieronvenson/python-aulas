idade = int(input(" diga sua idade: "))
indicado = input("tu foi indicado ? ")
ensinoCompleto = input("voce tem ensino completo? ")
experiencia = input(" diga se voce tem  +5 anos de experiencia: ")
antecedenteCriminal = input(" você  tem antecedentes criminais? ")
if experiencia == "sim" and idade >= 18 and  antecedenteCriminal == "não" :
    print ("contratado")
elif experiencia == "não" and ensinoCompleto == "sim" or indicado == "sim" and antecedenteCriminal == "não" :
    print ("pode ir para a entrevista")
else:
    print (" obrigado pelo seu comparecimento")
