# Comando Condicional é aquele que decide se um determinado bloco de comandos deve ser
# executado ou não, a partir do resultado de uma expressão relacional ou lógica;
# Blocos de comandos são um conjunto de instruções agrupadas, devem ser identados
# dentro de um comando anterior seguido de ":";
# A decisão é composta de uma condição e um ou mais resultados;
# E para isso utilizamos o "if" e o "else";
# - Estrutura: if <condição>:
#                   <bloco de comandos 1>
#              else:
#                   <bloco de comandos 2>

# Exercício 1:
# velocidade = 90
# 
# if velocidade > 80:
#     valorExcedente = velocidade - 80
#     valorMulta = valorExcedente * 5
#     print(f"Você foi multado, valor a ser pago é de R${valorMulta}")
# if velocidade < 80:
#     print("Você não foi multado")

# Exercício 2:
# num1 = 1
# num2 = 2
# num3 = 3
# 
#
# if num1 >= num2 and num1 >= num3:
#     maior = num1
# elif num2 >= num1 and num2 >= num3:
#     maior = num2
# else:
#     maior = num3
# 
#
# if num1 <= num2 and num1 <= num3:
#     menor = num1
# elif num2 <= num1 and num2 <= num3:
#     menor = num2
# else:
#     menor = num3
# 
# 
# print("Maior número:", maior)
# print("Menor número:", menor)

# Exercício 3:
# salarioAtual = float(input("Digite o valor de seu salário"))
# 
# if salarioAtual > 1250.00:
#     novoSalario = ((10 / 100) * salarioAtual) + salarioAtual
# elif salarioAtual <= 1250.00:
#     novoSalario = ((15 / 100) * salarioAtual) + salarioAtual
# 
# print(f"Seu novo salário é de: R${novoSalario}")


