#29.  O  Fatorial  Explosivo:  Na  matemática,  o  fatorial  de  5  (5!) 
#é  5  x  4  x  3  x  2  x  1  =  120. Peça  um  número  positivo  ao  usuário  e  use 
#um  laço  (for  ou  while)  para  calcular  e mostrar o fatorial dele. 

numero = int(input("Digite um número positivo: "))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial = fatorial * i

print("O fatorial é:", fatorial)