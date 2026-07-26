import random
enregiaDaIA = 100
nomeDOprota = input("diga seu nome pequeno coagúlo: ")
energiadoProta = 100
jogando = True
while energiadoProta > 0 and  enregiaDaIA > 0 and jogando == True:
    print (f"energia minha: {energiadoProta} e energia da IA: {enregiaDaIA}")
    print ("opçao 1: ataque basico")
    print ("opção 2: curar")
    print ("opção 3: ataque arriscado")
    print ("opção 4: DESISTIR")
    acao =int(input(f"digite o que deseja fazer {nomeDOprota}: "))
    if acao == 1:
       enregiaDaIA -= random.randint (0,7)
    elif acao == 2:
       energiadoProta += random.randint(0,15) 
    elif acao == 3:
      if  enregiaDaIA % 2 == 0 :
         print ("acertou o golpe")
         enregiaDaIA -= random.randint (20,40)
      else:
         print ("errou e se machucou tentando")
         energiadoProta -=15
    elif acao == 4:
      jogando = False
      print ("voce desistiu")
    else:
       print("opção invalida")
if energiadoProta <1 or jogando == False:
   print ("voce perdeu")
else:
   print  ("voce ganhou")
         
            
