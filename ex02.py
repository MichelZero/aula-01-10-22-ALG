#
# autor: michel
# data: 01/11/2022

# exemplo de fatorial (sem recursão):
# recursão é feita com função.
# https://pt.wikipedia.org/wiki/Fatorial

# 0! = 1
# 1! = 1
# 5! = 120 -> 1*2*3*4*5

######  1  #######
""" 
numero = int(input("informar um valor positivo: "))
valor = numero

fat = 1
while (numero > 0):
  fat = fat * numero # ex 5! -> 5 * 4 * ... = 120
  numero = numero - 1

print(f'o valor [{valor}!] = {fat}')
"""



######  2  #######
# entrada de dados
numero = int(input("informar um valor positivo: "))
valor = numero
fat = 1

# processamento
if (numero < 0):
  pass
elif (numero >= 0):
  while (numero > 0):
    fat = fat * numero # ex 5! -> 5 * 4 * ... = 120
    numero = numero - 1
  else:
    print(f'o valor [{valor}!] = {fat}')
