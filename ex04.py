#
# autor: michel
# data: 01/11/2022

# programa que gerar número aleatórios e somar:

# importando a class random
from random import randint

# entrada de dados
numero = int(input("informe quantos sorteios: "))
soma = 0
contador = 1

# processamento
while (contador <= numero):
  numSorteado = randint(1, 10)
  print(f"número sorteado [{contador}] foi {numSorteado}")
  soma = soma + numSorteado
  contador = contador + 1
  
# saída
print(f"a soma é: {soma}")