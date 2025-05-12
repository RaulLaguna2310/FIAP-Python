# Estruturas Aninhadas (if, else e elif)
# Exemplos:

# Ex 1 (if):
# if n >= 90:
# conceito = ‘A’
# if n < 90 and n >= 70:
# conceito = ‘B’
# if n < 70 and n >= 50:
# conceito = ‘C’
# if n < 50:
# conceito = ‘D’

# Ex 2 (if e else):
# if n >= 90:
#   conceito = ‘A’
# else:
#   if n >= 70:
#       conceito = ‘B’
#   else:
#       if n >= 50:
#           conceito = ‘C’
#       else:
#           conceito = ‘D’

# Ex 3 (if, else e elif):
# if n >= 90:
#   conceito = ‘A’
# elif n >= 70:
#   conceito = ‘B’
# elif n >= 50:
#   conceito = ‘C’
# else:
#   conceito = ‘D’

# Exercício 1:
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# operacao = input("Digite a operação desejada (+, -, *, /): ")

# if operacao == "+":
#     resultado = num1 + num2
#     print("Resultado da soma:", resultado)
# elif operacao == "-":
#     resultado = num1 - num2
#     print("Resultado da subtração:", resultado)
# elif operacao == "*":
#     resultado = num1 * num2
#     print("Resultado da multiplicação:", resultado)
# elif operacao == "/":
#     if num2 != 0:
#         resultado = num1 / num2
#         print("Resultado da divisão:", resultado)
#     else:
#         print("Erro: divisão por zero!")
# else:
#     print("Operação inválida!")

# Exercício 2:

#valor_casa = float(input("Digite o valor da casa: "))
#salario = float(input("Digite seu salário: "))
#anos = int(input("Em quantos anos pretende pagar? "))

# meses = anos * 12
# prestacao = valor_casa / meses
# limite = salario * 0.3

# if prestacao <= limite:
#     print(f"Empréstimo aprovado! Prestação: R${prestacao:.2f}")
# else:
#     print(f"Empréstimo negado! Prestação de R${prestacao:.2f} excede 30% do salário (R${limite:.2f})")

# Exercício 3:
# kwh = float(input("Quantidade de kWh consumida: "))
# tipo = input("Tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()

# if tipo == "R":  # Residencial
#     if kwh <= 500:
#         preco_kwh = 0.40
#     else:
#         preco_kwh = 0.65
# elif tipo == "C":  # Comercial
#     if kwh <= 1000:
#         preco_kwh = 0.55
#     else:
#         preco_kwh = 0.60
# elif tipo == "I":  # Industrial
#     if kwh <= 5000:
#         preco_kwh = 0.55
#     else:
#         preco_kwh = 0.60
# else:
#     print("Tipo de instalação inválido!")
#     preco_kwh = 0
# if preco_kwh > 0:
#     total = kwh * preco_kwh
#     print(f"Preço a pagar: R${total:.2f}")

# Exercício 4:
# valor_inicial = float(input("Digite o valor inicial: "))
# razao = float(input("Digite a razão da PG: "))

# termo1 = valor_inicial
# termo2 = termo1 * razao
# termo3 = termo2 * razao
# termo4 = termo3 * razao

# print("Quatro primeiros termos da PG:")
# print(f"{termo1:.2f}, {termo2:.2f}, {termo3:.2f}, {termo4:.2f}")

# Exercício 5:
# nota1 = float(input("Digite a nota do 1º semestre: "))
# nota2 = float(input("Digite a nota do 2º semestre: "))

# media = (nota1 + nota2) / 2

# if media >= 6.0:
#     print(f"Aprovado com média {media:.2f}")
# else:
#     print(f"Reprovado com média {media:.2f}")

# Exercício 6:
# x = float(input("Digite o valor de x: "))

# if x < 2:
#     y = 1
# elif x < 3.5:
#     y = 2
# elif x < 5:
#     y = 3
# else:
#     y = -10 * x + 28

# print(f"y({x}) = {y}")

# Exercício 7:
# idade = int(input("Digite a idade da pessoa: "))
# estudante = input("Possui carteira de estudante? (s/n): ").lower()

# if idade >= 65 or idade < 21 or estudante == 's':
#     print("Tem direito à meia-entrada.")
# else:
#     print("Não tem direito à meia-entrada.")

# Exercício 8:
# codigo = input("Digite o código da mercadoria: ")
# preco = float(input("Digite o preço da mercadoria: R$ "))

# if codigo == '00':
#     preco = preco * 0.90  # Aplica 10% de desconto

# print(f"Preço final: R${preco:.2f}")

# Exercício 9: 
# x = int(input("Digite um número inteiro: "))

# if x > 0:
#     print("positivo")
# elif x < 0:
#     print("negativo")
# else:
#     print("0")