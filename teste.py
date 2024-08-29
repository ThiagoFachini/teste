
# programa encontrar fatorial.

num = int(input("Enter a number: "))

#num = int(input("Enter a number: ")) entrada de dados

fatorial = 1

#checagem de condição e reealização da operação
if num < 0:
   print("Desculpe, não existe fatorial para números negativos")
elif num == 0:
   print("o fatorial de 0 é 1")
else:
   for i in range(1,num + 1):
       fatorial = fatorial*i
#saida de dados       
   print("o fatorial de",num,"é",fatorial)