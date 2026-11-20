#21.  Batalha  de  Turnos  (Herói  vs.  Goblin):  O  Herói  tem  100  de  vida  e  o 
# Goblin  tem  80. Crie  um  loop  while  que  dure  enquanto  ambos  estiverem  vivos  
# (vida_heroi  >  0  and vida_goblin  >  0).  A  cada  turno,  peça  para  o  jogador  
# escolher:  1-Atacar  (tira  15  do Goblin)  ou  2-Curar  (recupera  10  do  Herói).  O 
# Goblin  sempre  contra-ataca  tirando  12 de vida. Mostre quem venceu no final! 

vida_heroi = 100
vida_goblin = 80

while vida_heroi > 0 and vida_goblin > 0:
    escolha = input("Escolha 1- atacar ou 2-Curar:")
    if escolha =="1":
        vida_goblin = vida_goblin - 15
        print(" Voce atacou o goblin!")

    elif escolha =="2":
        vida_heroi = vida_heroi + 10
        print("Voce recuperou 10 de vida!")

    vida_heroi = vida_heroi - 12

    print(f"Vida do Heroi:{vida_heroi}")
    print(f"Vida do Goblin: {vida_goblin}")

    if vida_heroi <= 0:
        print("O Goblin venceu!")

    else:
        print("O Heroi venceu!")
