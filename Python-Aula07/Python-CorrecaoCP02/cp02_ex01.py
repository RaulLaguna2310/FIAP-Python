print(f'{'1':6s}{'maçã':8s}{12.90:12.2f}')
print(f'{'2':6s}{'uva':8s}{9.30:12.2f}')
print(f'{'3':6s}{'banana':8s}{3.5:12.2f}')
print(f'{'4':6s}{'melancia':8s}{7.00:12.2f}')
print(f'{'5':6s}{'kiwi':8s}{37.50:12.2f}')

'''codigo fruta preço/kg
1 maçã 12.90
2 uva 9.30
3 banana 3.50
4 melancia 7.00
5 kiwi 37.50
'''

while True:
    op = input("Escolha o código da fruta desejada ou 0 para sair:")
    if op == '0':
        break
    elif op == '1':
        txt = 12.90
    elif op == '2':
        txt = 9.30
    elif op == '3':
        txt = 3.5
    elif op == '4':
        txt = 7
    elif op == '5':
        txt = 37.50
    else:
        print('Código Inválido')
    qtd = float(input("Digite a qtd (em kg):"))
    valor += qtd * txt

print(f'O valor total da sua compra é R${valor:.2f}')