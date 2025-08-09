# Exercício 1 - Receba números do usuário e exiba o resultado da conta "2a x 3b":

# a = float(input("Digite o primeiro número:"))
# b = float(input("Digite o segundo número:"))

# resultado = 2 * a * 3 * b

# print(f"O valor de 2x{a}x3x{b} = {resultado}")

# Exercício 2 - Simule uma fila, o usuário escolhe se quer adicionar ou executar . (Exibir qual posição da fila a demanda entrará):

# demandas = []
# while True:
#     print("Você deseja: \n 1 - Adicionar uma demanda; \n 2 - Executar uma demanda; \n 0 - Sair;")
#     op = int(input("Digite o número da opção desejada:"))
#     if op == 1:
#         demanda = input("Digite o nome da demanda que desaja adicionar: ")
#         demandas.append(demanda)
#         print(f"Sua demanda foi adicionada na posição: {len(demandas)}.")
#     elif op == 2:
#         demanda = input("Digite a posição que a demanda que quer executar: ")
#         demandas.pop(int(demanda) - 1)
#         print(f"A demanda na posição {demanda} foi executada.")
#     elif op == 0:
#         break
#     else:
#         print("Opção inválida, reiniciando o fluxo...")
#         break
    
