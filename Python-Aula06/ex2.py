compra = 0

while True:
    op = input('Escolha uma opção ou 0 para sair')
    if op == '1':
        compra += 0.5
    elif op == '2':
        compra += 1
    elif op == '0':
        break
    else:
        print('Códio Inválido')
print(f'o valor da compra é {compra}')
