# Os laços de repetição são utilizados para delimitar um número de intruções ou 
# comando que deve ser executado mais de uma vez;
# Utiliza uma condição para determinar se deve continuar ou não a execução;

# While:
    # O bloco será repetido enquanto a condição for verdadeira;
    # Após a execução do bloco, a condição é verificada novamente;
    # while <condição>:
    #    <bloco de código>

    # A condição é uma expressão que pode ser avaliada como verdadeira ou falsa (Booleano);
    # Somente quando a condição se tornar falsa, o laço é interrompido e o 
    # programa continua a execução do código após o laço;
    # Se a condição já for falsa, o bloco de código não será executado;
    # Deve haver algum processo dentro do laço que altere a condição para 
    # falsa em algum momento, para evitar um loop infinito; 

# Exercício 1:
# i = 2
# j = 4
# n = 0
 
# print(f"Os valores de cada variável são: \n i: {i}; \n j: {j}; \n n: {n}")
# while i < 10:
#     n = i + j
#     i += n
#     print(f"Os valores de cada variável após a ultima execução são: \n i: {i}; \n j: {j}; \n n: {n}")
# print(f"Os valores finais de cada variável são: \n i: {i}; \n j: {j}; \n n: {n}")

# Exercício 2:
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

# Exercício 3:
# i = 50
# while i <= 100:
#     print(i)
#     i += 1

# Exercício 4:
# contagem = 10
#
# print(f"Contagem regressiva: ")
# while contagem > 0:
#     print(contagem)
#     contagem -= 1
# print("Fogo!")

# Exercício 5:
# numero = int(input("Digite um número inteiro positivo: "))
# i = 1
# 
# while i <= numero:
#     if i % 2 == 0:
#         print(f"O números pares de 1 até {numero} são: {i}")
#     i += 1

# Exercício 6:
# numero = int(input("Digite um número inteiro positivo: "))
# i = 1
# 
# while i <= numero:
#     if i % 2 != 0:
#         print(f"O números ímpares de 1 até {numero} são: {i}")
#     i += 1

# Exercício 7:
# numero = int(input("Digite um número inteiro positivo: "))
# i = 0
# 
# print(f"A tabuada do {numero} é:")
# while i <= 10:
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")
#     i += 1

# Exercício 8:
# numero = int(input("Digite um número inteiro positivo: "))
# numeroInicial = int(input("Digite o número inicial do intervalo: "))
# numeroFinal = int(input("Digite o número final do intervalo: "))
# 
# print(f"A tabuada do {numero} no intervalo de {numeroInicial} a {numeroFinal} é:")
# while numeroInicial <= numeroFinal:
#     resultado = numero * numeroInicial
#     print(f"{numero} x {numeroInicial} = {resultado}")
#     numeroInicial += 1
