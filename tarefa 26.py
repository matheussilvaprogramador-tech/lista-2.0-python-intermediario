#26.  A  Sequencia  de  Fibonacci:  A  famosa  sequencia  matematica  da  natureza 
# (0,  1,  1, 2,  3,  5,  8,  13...),  onde  o  proximo  numero  e  sempre  a  soma  dos  
# dois  anteriores.  Peca um numero N e use um for para gerar os primeiros N termos dessa 
# sequencia. 

n = int(input("Quantos termos deseja mostra :"))
a = 0
b = 1
for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo
