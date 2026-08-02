listaDeAlunos = ["ALBERTO" , "BOLINHO" , "CURURU" , "CRISTIANO RONADO R7" , "DIO"]
print (f" você deve escolher entre os 5 alunos para saber o numero deles na chamda {listaDeAlunos}")
numeroDoAluno =     int(input("fale o numero do aluno do aluno: "))
if numeroDoAluno <0:
    print ("pode numero negativo não man ☝️​")
elif numeroDoAluno >len(listaDeAlunos):
    print ("pode numero grande  nao man ☝️ ")
else:
    print (f"{listaDeAlunos[numeroDoAluno]}")








