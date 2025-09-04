# Lambda
# É uma forma mais simples, nessa notação apenas funções mais simples podem ser definidas.
# -  Formato -> x = lambda<parâmetros>: <código com return>

# Exemplos:
# a = lambda x: x * 2
# a(2)

# b = lambda x, y: x * y
# b(2, 3)

# c = lambda x: x.lower()
# c('OLÁ')

# Exercícios:
# - Ex01: Crie uma função lambda que retorne a soma de 3 números
# soma = lambda x, y, z: x + y + z
# soma(2, 2, 2)

# --------------------------------------------------------------

# - Ex02: Crie uma função lambda para inverter uma string
# invertSt = lambda string: string[::-1]
# invertSt('lápis')

# --------------------------------------------------------------

# - Ex03: Crie uma função lambda que verifica se a string é um palíndromo
# vfPalindromo = lambda palavra: palavra == palavra[::-1]
# vfPalindromo("arara")
