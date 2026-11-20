# 11.  A  Tabuada  magica:  Peca  ao  usuario  para  digitar  um  numero  inteiro.  Use  um  
# laco for  com  range(1,  11)  para  imprimir  a  tabuada  completa  desse  numero 
# (ex:  5  x  1  =  5  ate 5 x 10 = 50). 
numero=int(input("digite um numero :"))
for i in range(1, 11):
    print(f" {numero}x{i}={numero*i}")
