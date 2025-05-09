# Tipos de Dados:
# Inteiros(int) -> 1; 2; 3...
# Decimal(float) -> 1.23; 345.8; 94.27...

# Tipo Lógico:
# Booleano (True or False) -> mais usados na verificação de resultados de expressões relacionais e lógicas
# - Expressões Relacionais -> são aquelas que realizam uma comparação entre duas expressões e retornam:
# - False, se o resultado for falso; True, se o resultado for verdadeiro

# Função que retorna o tipo de determinada variável: 
# type(variavel)

# Representação dos números em diferentes bases:
# Base decimal:
# - 531 = 5 * 10^2 + 3 * 10^1 * 10^0
# - 1024 = ???
# Base binária (0 ou 1):
# - 1010 = ??? (10 na base decimal)
# Base octal: 
# - 123 = ??? (83 em decimal)

# Exercício 1:
# dia = 1
# horas = 3
# minutos = 46
# segundos = 40

# diaHora = dia * 24
# horasTotais = diaHora + horas
# horasMin = horasTotais * 60
# minTotais = horasMin + minutos
# minSeg = minTotais * 60
# segTotais = minSeg + segundos
# print(segTotais)

# Exercícios 2:
# segundos = 87426
# minTotais = segundos / 60
# horaTotais = minTotais / 60
# print(f"Horas: {horaTotais}, Minutos: {minTotais}, Segundos: {segundos}")

# Exercício 3:
#numero = 12345
#produto = 1
# 
#for digito in str(numero):
#    produto = produto * int(digito) 
# - (também pode ser escrito assim -> produto *= int(digito)
#print(produto)

