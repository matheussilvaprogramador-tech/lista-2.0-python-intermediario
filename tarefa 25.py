#25.  Cacador  de  Numeros  Primos:  Peca  um  numero  inteiro  ao  usuario.  Use  um 
#laco  for para  testar  por  quantos  números  ele  consegue  ser  dividido  com  resto 
# zero  (%).  Se  ele tiver exatamente 2 divisores (1 e ele mesmo), imprima 
# "e um Numero Primo!".

numero = int(input("Digite um numero:"))
contador =  0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador = contador + 1 

if contador == 2 :
    print("E um numero primo!")
else:
    print("Nao e um numero primmo!")
