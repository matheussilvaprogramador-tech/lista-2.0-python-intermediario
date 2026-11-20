#14.  Somador  de  Moedas:  Peça  para  o  usuário  digitar  quantas  moedas  encontrou 
#em  5 baús  diferentes  (usando  um  for  de  5  voltas).  A  cada  volta,  
#some  o  valor  em  uma variável total_ouro e, no final, mostre a riqueza acumulada. 
total_ouro = 0
for i in range(5):
    moedas= int(input("Quantas moedas voce encontrou:"))
    total_ouro=total_ouro+moedas
print(f"total de moedas :{total_ouro}")
