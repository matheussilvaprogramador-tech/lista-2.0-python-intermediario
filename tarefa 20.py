#20.  O  Caixa  de  Supermercado:  Crie  um  programa  que  pede  o  preco  de  varios 
#produtos  usando  while.  O  caixa  continua  somando  os  precos  ate  que  o  operador  
# digite 0 (zero). Quando digitar 0, o loop para e mostra o valor total da compra. 

total = 0 
preco = float(input("Digite o preco do produto (0 paara finalizar): "))

while preco != 0:
    total = total + preco
    preco = float(input("Digite o preco do produto (0 para finalizar :)"))
print(f"Total da compra: R$ {total : 2f}")




# total = 0

# preco = float(input("Digite o preco do produto (0 para finalizar): "))

# while preco != 0:
#     total = total + preco
#     preco = float(input("Digite o preco do produto (0 para finalizar): "))

# print(f"Total da compra: R$ {total:.2f}")