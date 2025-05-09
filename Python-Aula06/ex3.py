numero = int(input('Digite um número'))

while True:
    i = 1
    n = int(input('Digite um número (-1 para parar)'))
    if n == -1:
        break

    qtd = 0
    while i <= n:
        if n % i == 0:
            qtd += 1
        i += 1
    if qtd == 2:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')