#
# autor: michel
# data: 01/11/2022

# # 1 - Programa que imprime a quantidade de números 
# pares de 100 até 200, incluindo-os, tb a soma dos impares.
# com entrada de dados pelo usuário.

# contadora e acumuladora 
# contar e soma
# fixo e variável
# contarPares e somarImpares

# número par -> valor MOD 2 == 0 (valor % 2 == 0)
# número impar -> valor nãoMOD 2 == 0 (valor % 2 != 0) ! -> negativa

# numInicio = int(input("informe o valor inicial"))
# numFim = int(input("informe o valor final"))

numInicio = 100
numFim = 200
contaPar = 0
somaImpar = 0

while (numInicio <= numFim): # se for verdade, True
  
  if (numInicio % 2 == 0): # se o MOD for Zero, é par
    contaPar = contaPar + 1 # contaPar += 1 
  elif (numInicio % 2 != 0): # se o MOD for diferente de Zero, é impar
    somaImpar += numInicio # somaImpar = somaImpar + numInicio
  
  numInicio += 1
  
print(f"quantidade de par = {contaPar}; soma dos impares = {somaImpar}.")