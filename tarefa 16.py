#16.  A  Barra  de  Stamina  (Energia):  O  herói  começa  com  energia  =  100.  Crie  
#um  while que  rode  enquanto  a  energia  for  maior  que  0.  A  cada  volta,  pergunte 
# se  o  herói  quer "correr"  (gasta  20  de  energia)  ou  "pular"  (gasta  15  de 
# energia).  Quando  a  energia acabar, mostre "O herói desmaiou de cansaço!". 
energia = 100
while energia > 0:
    acao = input("voce que corre ou pular ?:")

    if acao == "corre":
        energia = energia - 20
        print(f" energia : {energia}")

    elif acao == "pular":
        energia = energia - 15
        print(f" energia:{energia}")
print(" O heroi desmaio de cansaço!")



