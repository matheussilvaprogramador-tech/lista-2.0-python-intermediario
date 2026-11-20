#18.  O  Contador  de  Letras:  Peca  ao  usuario  para  digitar  uma  palavra  
#(ex: "abracadabra").  Use  um  for  letra  in  palavra:  para  imprimir  cada  letra  da
#palavra  em uma linha separada, contando quantas letras 'a' existem nela. 
palavra = input("Digite uma palaavra :")
contador = 0 
for letra in palavra :
    print(letra)

    if letra == "a":
        contador=contador+1
        
print (f" A letra a apareceu {contador} vezes.")


