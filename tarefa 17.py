#17.  Validador  de  Nota  Escolar:  Peça  ao  professor  para  digitar  uma  nota  de  0 
#a  10. Enquanto  ele  digitar  um  número  inválido  (menor  que  0  ou  maior  que  10), 
# o  while  deve prender o programa pedindo uma nota válida. 
nota = int(input("Digite uma nota de 0 a 10 :"))

while nota < 0 or nota >10:
    print("Nota invalida! digite novamente")
    nota = int(input("digite uma nota de o a 10 :"))
print(f"Nota registrada : {nota}")


