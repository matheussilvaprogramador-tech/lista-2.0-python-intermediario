#19.  A  Escada  de  Asteriscos:  Peca  um  numero  N  ao  usuario.  Use  um  laco  for 
#para desenhar  uma  escada  no  terminal  usando  o  símbolo  *  (ex:  se  digitar  4,  
#imprime  *  na linha 1, ** na linha 2, *** na linha 3, **** na linha 4). 

numero = int(input("Digite um numeor : "))
for i in range(numero):
    print("*" * (i + 1))

