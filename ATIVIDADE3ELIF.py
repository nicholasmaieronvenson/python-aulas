vip = input("você é vip? ")
idade = int(input("digite sua idade: "))
ingresso = input("você tem ingresso? ")
autorizaçâo = input("você tem autorizacão? ")
if idade < 12 :
    print ("nao pode entrar")
elif idade >= 18  and (vip == "sim" or ingresso == "sim") :
    print  ("pode entrar")
elif idade < 18 and autorizaçâo == "sim" and (vip == "sim" or ingresso == "sim") :
    print ("pode entrae")
else:
    print ("NÃO PODE ENTRAR")
