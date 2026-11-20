#O  DESAFIO  DO  CHEFÃO  (O  Simulador  de  Fliperama):  Crie  um  sistema  completo de
#máquina de fliperama usando while True:. O jogador começa com 5 fichas. A  cada  rodada,  
#o  menu  pergunta:  1  -  Jogar  Corrida  (custa  1  ficha),  2  -  Jogar Luta 
#(custa 2 fichas), 3 - Comprar mais fichas, 4 - Sair. O  sistema  deve  impedir  o 
#jogador  de  jogar  se  ele  não  tiver  fichas  suficientes para aquela máquina (if). 
#Quando  o  jogador  escolher  jogar,  rode  um  mini-loop  for  de  3  segundos 
#("Jogando...  Fase  1...  Fase  2...  Fase  3!")  antes  de  voltar  ao  menu  principal. 
#O programa  só  encerra  se  ele  escolher  4  ou  se  as  fichas  zerarem  e  ele 
#não quiser comprar mais! 

fichas = 5

while True:
    print("\n===== FLIPERAMA =====")
    print("Fichas disponíveis:", fichas)
    print("1 - Jogar Corrida (1 ficha)")
    print("2 - Jogar Luta (2 fichas)")
    print("3 - Comprar mais fichas")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if fichas >= 1:
            fichas = fichas - 1

            for i in range(1, 4):
                print("Jogando... Fase", i)

            print("Fim do jogo!")

        else:
            print("Você não tem fichas suficientes!")

    elif opcao == 2:
        if fichas >= 2:
            fichas = fichas - 2

            for i in range(1, 4):
                print("Jogando... Fase", i)

            print("Fim do jogo!")

        else:
            print("Você não tem fichas suficientes!")

    elif opcao == 3:
        quantidade = int(input("Quantas fichas deseja comprar? "))
        fichas = fichas + quantidade
        print("Fichas adicionadas!")

    elif opcao == 4:
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida!")

    if fichas == 0:
        resposta = input("Suas fichas acabaram! Deseja comprar mais? (S/N): ").upper()

        if resposta == "N":
            print("Fliperama encerrado!")
            break