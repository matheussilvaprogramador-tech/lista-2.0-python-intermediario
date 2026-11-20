#27.  O  Elevador  Inteligente:  Um  predio  tem  10  andares.  O  elevador  comeca  no 
#andar  0. Crie  um  menu  em  while  perguntando  para  qual  andar  o  usuario  quer  ir 
# (ou  -1  para sair).  Use  um  laco  for  interno  para  simular  o  elevador  passando  
# andar  por  andar (subindo ou descendo) ate chegar no destino escolhido! 


andar = 0

while True:
    destino = int(input("Para qual andar deseja ir? (0 a 10 ou -1 para sair): "))

    if destino == -1:
        print("Elevador encerrado!")
        break

    if destino < 0 or destino > 10:
        print("Andar inválido!")

    elif destino > andar:
        for i in range(andar + 1, destino + 1):
            print("Subindo para o andar:", i)

        andar = destino

    elif destino < andar:
        for i in range(andar - 1, destino - 1, -1):
            print("Descendo para o andar:", i)

        andar = destino

    else:
        print("Você já está nesse andar!")