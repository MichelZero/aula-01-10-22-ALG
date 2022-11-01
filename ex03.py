##
# autor: michel
# data: 01/11/2022

# menu
# variavel1 = "123" (entrada)
# variavel2 = '3' (entrada)
#
# variavel1 == 123 (False)
# variavel1 == "123" (True)
# variavel2 in variavel1 (True)
# variavel2 in 123 (não pode, são coisas diferentes, False)

confirmar = 's'

while True:
  if (confirmar in "Ss"): 
    nome = input("informe o nome do usuário: ")
    senha = input("informe a senha: ")
    
    print("erro de senha ou nome")
  
  confirmar = input("gostaria de continuar? (s/n) ")
  if confirmar in "Nn":
    break

print("fim do programa!")