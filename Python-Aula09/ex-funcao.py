# Ex 01:
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# def soma(a, b):
#     res = a + b
#     return res

# print(f"O resultado da soma é: {soma(num1, num2)}")

# Ex 02:

def lerNotas(n):
    l = []
    for i in range(n):
        l.append(float(input("Digite a nota: ")))
    return l

print(lerNotas(5))

def mostra_nota(notas):
    for i in notas:
        print(i)

a = lerNotas(5)
mostra_nota(a)

def media_nota(notas):
    soma = 0
    for i in notas:
        soma += i 
        return soma / len(notas)
    
media_final = media_nota(lerNotas(3))
print(media_final)
