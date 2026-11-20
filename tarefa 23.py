#23.  Adivinhe  o  Numero  Secreto  (Quente  ou  Frio):  Defina  um  numero  secreto  no  
#codigo (ex:  42).  Crie  um  while  onde  o  jogador  tenta  adivinhar.  Se  o  chute 
#for  maior  que  42, diga  "Chutou  alto!  Tente  um  menor.".  Se  for  menor,  diga 
#"Chutou  baixo!  Tente  um maior.". Conte quantas tentativas ele precisou ate acertar! 

numero_secreto = 42
tentativas = 0

chute = int(input("Tente adivinhar o numero secreto:"))
while chute != numero_secreto:
    tentativas = tentativas + 1

    if chute > numero_secreto:
        print ("Chute alto! Tente um menor.")
    else:
        print("Chutou baixou! Tente um maior.")


    chute = int(input("Tente novamente :"))
tentativas = tentavivas = tentativas + 1
print ("Parabens voce acertou")
print (f"Voce precisou de {tentativas} tentativas.")
