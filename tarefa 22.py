#22.  O  Limite  de  Tentativas  (Segurança  Bancária):  Melhore  o  exercício  do  Cofre 
#(nº  12). Agora  o  usuário  tem  no  máximo  3  tentativas  para  acertar  a  senha. 
#Se  errar  as  3  vezes, o laço para e imprime "Cartão Bloqueado! Chamando os guardas!". 
senha = ""
tentativas = 0

while senha != "dragao123" and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas = tentativas + 1 

    if senha == "dragao123":
        print("confre Aberto!")
    else:
        print("Senha Incorreta, tente novamente!")

if tentativas == 3 and senha != "dragao123":
    print(" Cartao Bloqueado! Chamando os guardas!")
    