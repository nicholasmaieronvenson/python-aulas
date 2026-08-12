corredores = ["jhonny" , "gyro" , "diego"]
escolha  =   int(input("quem lidera a corrida? 0 = jhonny, 1 = gyro , 2 = diego ?  "))
if escolha == 0:
  print(f"O novo líder é {corredores[0]}!")
elif escolha == 1:
  print (f"o novo lider é {corredores[1]}!")
elif escolha == 2:
  print(f"O novo líder é {corredores[2]}!")
else:
  print("Posição inválida na corrida")
