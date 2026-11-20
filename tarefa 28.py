#28.  Simulador  de  Juros  do  Cofrinho:  O  aluno  guardou  100  moedas  no  banco 
#mágico que  rende  10%  ao  mês.  Pergunte  quantos  meses  ele  vai  deixar  o  dinheiro
# lá  e  use  um for para calcular e mostrar o saldo atualizado mês a mês (juros compostos). 

saldo = 100

meses = int(input("Quantos meses deseja deixar o dinheiro no banco? "))

for i in range(1, meses + 1):
    saldo = saldo * 1.10
    print(f"Saldo do mês {i}: {saldo:.2f} moedas")