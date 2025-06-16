# Laço de Repetição: "for"

# É uma estrutura de repetição que percorre os elementos de uma lista;
# Para cada elemento da lista, o laço executa um bloco de código;
# Faz a variável de controle assumir o valor de cada elemento da lista, um por vez;
# Break e Continue podem ser usados para alterar o fluxo do laço;

# Estrutura do laço "for":
    # for <variavel> in lista: 
    #     <bloco de código>

# Função range(n):
# Gera uma sequência com valores inteiros, que vão de 0 até n-1;
# É possível especificar um intervalo de valores:
    # range(inicio, fim): gera valores de "inicio" até "fim-1";
# É possível especificar um passo:
    # range(inicio, fim, passo): gera valores de "inicio" com um incremento de "passo" até "fim-1";

# Exercício 1:
# numero = int(input("Digite um número inteiro positivo: "))
# i = 0
# 
# for i in range(1, numero + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

# Exercício 2:
# notas = []
# n = int(input("Digite a quantidade de notas: "))
# for i in range(n):
#     nota = float(input(f"Digite a nota {i + 1}: "))
#     notas.append(nota)
#     print(f"A nota {i + 1} é: {nota}")
# media = sum(notas) / len(notas)
# print(f"A média das suas notas é: {media}")

# Exercício 3:
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]
# comum = []
# 
# for elemento in lista1:
#     if elemento in lista2:
#         comum.append(elemento)
# if len(comum) > 0:
#     print(f"Elementos comuns encontrados: {comum}")
# else:
#     print("Nenhum elemento comum encontrado.")
