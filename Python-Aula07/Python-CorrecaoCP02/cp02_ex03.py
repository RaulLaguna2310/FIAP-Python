while True:
    n = int(input("Digite e veja se pe perfeito:"))
    if n == 0:
        break
    i = 1
    soma = 0
    while i < n:
        if n%i == 0:
            soma += i
        i += 1

    if soma == n:
        print(f'{n} é um numero perfeito')
    else:
        print(f'{n} é imperfeito')