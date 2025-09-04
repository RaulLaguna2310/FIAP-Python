import math
# List Comprehentions
# Forma simples de criar listas
# Formato -> list = [expression for item in iterable if condition == True]

# Exemplos:

# L = [x for x in range(10)]
# retorna -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# L = [x * 2 for x in [0, 1, 2, 3]]
# retorna -> [0, 2, 4, 6]

# P = [x for x in range(10) if x % 2 == 0]
# retorna -> [0, 2, 4, 6, 8]

# H = [z for z in range(0,10) if math.sqrt(z) % 1 == 0]
# retorna -> [0, 1, 4, 9]

# Exercícios:

# - Ex01: Crie uma lista com os quadrados dos números de 1 a 10.

# listQuad = [i**2 for i in range(1, 11)]
# print(listQuad)

# - Ex02: Gere uma lista contendo apenas os números pares de 1 a 20.

# listPares = [x for x in range(1, 21) if x % 2 == 0]
# print(listPares)

# - Ex03: Crie uma lista contendo o comprimento de cada palavra na lista ["Python", "List", "Comprehension", "Exercícios"].

# lista = ["Python", "List", "Comprehension", "Exercícios"]
# contarLen = [len(i) for i in lista]
# print(contarLen)

# - Ex04: Dada a lista de palavras ["maçã", "banana", "uva", "morango", "abacaxi"], crie uma nova lista contendo apenas as palavras com mais de 5 letras.

# lista = ["maçã", "banana", "uva", "morango", "abacaxi"]
# contarLen = [i for i in lista if len(i) > 5]
# print(contarLen)

# - Ex05: Converta uma lista de temperaturas em Celsius [0, 10, 20, 30, 40] para Fahrenheit usando a fórmula F = C * 9/5 + 32.

# lista = [0, 10, 20, 30, 40]
# converter = [i * (9/5) + 32 for i in lista]
# print(converter)

# - Ex06: Gere uma lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz".

# lista = ["Fizz" if x % 3 == 0 else x for x in range(1, 21)]
# print(lista)

