#24.  O  Relogio  Digital  (Lacos  Aninhados):  Crie  um  simulador  de  relogio  usando 
#dois laços  for  (um  dentro  do  outro).  O  laço  de  fora  conta  as  horas  
#de  0  a  2,  e  o  laço  de dentro conta os minutos de 0 a 59. Imprima no 
#formato 00:01, 00:02... ate 02:59. 

for hora in range (3):
    for minuto in range (60):
        print(f" {hora:2d}:{minuto:2d}")
