# Matriz
# É um objeto bidimensional, formado por lista, onde todas são do mesmo tamanho.
# É representada na forma de uma lista de listas.

# Exemplos:
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Como gerar:
# L = int(input("Entre com o número de linhas: "))
# C = int(input("Entre com o número de colunas: "))
# matriz = []
# 
# for i in range(L):
#     linha = []
#     for j in range(C):
#         linha.append(int(input("Quais dados deseja adicionar: ")))
#     matriz.append(linha)
#     
# print(matriz)

# - Ex01: Exercício: Crie uma matriz de dimensões 1 x c e atribuindo valor zero para todos os elementos.
# L = int(input("Entre com o número de linhas: "))
# C = int(input("Entre com o número de colunas: "))
# matriz = []
# 
# for i in range(L):
#     linha = []
#     for j in range(C):
#         linha.append(int(input("Quais dados deseja adicionar: ")))
#     matriz.append(linha)
#     
# print(matriz)

# - Ex02: Exercício: Inicialize uma matriz de dimensões 1 x c atribuindo valores de 1 até 1 x c para os elementos da matriz.
# l = int(input("Digite o número de linhas: "))
# c = int(input("Digite o número de colunas: "))
# 
# valores = list(range(1, l * c + 1))
# matriz = []
# index = 0
# 
# for i in range(l):
#     linha = []
#     for j in range(c):
#         linha.append(valores[index])
#         indice += 1
#     matriz.append(linha)
# 
# print(matriz)

# Como acessar elementos de um matriz
# Dada uma matriz:
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matriz[0][2])
# resultado -> 3
