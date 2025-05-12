# Ordem de prioridade de todos os tipos de operações:
#     1° - "**" Exponenciação
#     2° - "*; /; //; %" Multiplicação e Divisões
#     3° - "+; -" Adição e Subtração
#     4° - "==; !=; <=; >=; >; <" Operações Relacionais
#     5° - "not" Operador Lógico
#     6° - "and" Operador Lógico
#     7° - "or" Operador Lógico

# Exercício 1: 
# 5 * 4 < 4 + 3 -> False
# 6 * 2 - 1 > 3 * 1 -> True
# 9 - 4 / 2 <= 7 + 1 or 5 * 2 - 3 != 6 -> True
# 9 / 3 == 3 * 3 and 2 * 3 - 1 >= 8 -> False

# Exercício 2: 
# A = 1; B = 2; C = True; D = False
# A > B and C or D -> True
# A = 10; B = 3; C = False; D = False
# A > B and C or D -> False 
# A = 5; B = 1; C = True; D = True
# A > B and C or D -> True

# Exercício 3: 
# idade = x
# salario = y
# emprestimo = True
# 
# if idade >= 18 and salario > z:
#     print(emprestimo)
# else:
#     print(not emprestimo)

# Exercício 4:
# media1 = 7
# media2 = 7
# media3 = 7
# media = (media1 + media2 + media3) / 3
# 
# if media >= 7:
#     print(f"Aprovado com média: {media}")
# else:
#     print(f"Reprovado com média: {media}")
