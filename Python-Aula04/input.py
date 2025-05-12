# Input: é uma função "input()" que realiza a leitura de dados a partir do teclado,
# ou seja, aguarda que o úsuario digite um valor, aperte a tecla <enter> 
# e atribui o valor digitado a um objeto na memória. 
# x = input("Digite algo:")

# Exercício 1:
# nome = input("Digite o seu nome:")

# Exercício 2:
# nome = input("Digite o seu nome:")
# idade = input("Digite a sua idade:")
# print(f"Olá meu nome é {nome} e tenho {idade} anos!")

# Exercício 3:
# num1 = int(input("Digite um número inteiro:"))
# num2 = int(input("Digite outro número inteiro:"))
# soma = num1 + num2
# print(f"A soma entre {num1} e {num2} é {soma}!")

# O input sempre retorna valores do tipo "string", porém isso pode ser convertido
# Alguns tipos de dados podem ser convertidos para outros, para fazer isso utilizamos:
# - "int()" -> converte para o tipo int (número inteiro)
# - "float()" -> converte para o tipo float (número decimal)
# - "str()" -> converte para o tipo str (string)
# - "bool()" -> converte para o tipo bool (booleano)

# Exercício 4: 
# ano = int(input("Digite os anos de serviço:"))
# valorPorAno = float(input("Digite o valor recebido:"))
# bonus = ano * valorPorAno
# print(f"O bônus adiquirido é de R${bonus}")

# Exercício 5:
# metros = float(input("Digite a quantidade de metros que deseja converter:"))
# conversaoMil = metros * 1000
# print(f"{metros} metros são equivalentes a {conversaoMil} milímetros")

# Exercício 6:
# dias = int(input("Dias:"))
# horas = int(input("Horas:"))
# minutos = int(input("Minutos:"))
# segundos = int(input("Segundos:"))
# 
# diasHora = dias * 24
# horasTotais = diasHora + horas
# horasMinuto = horasTotais * 60
# minutosTotais = horasMinuto + minutos
# minutosSegundo = minutosTotais * 60
# segundosTotais = minutosTotais + segundos
# 
# print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos \nsão equivalentes á: {segundosTotais} segundos.")

# Exercício 7:
# salario = float(input("Digite o salário:"))
# porcentagemAumento = int(input("Digite a porcentagem do aumento:"))
# salarioNovo = ((porcentagemAumento / 100) * salario) + salario
# print(f"Com esse valor de aumento: {porcentagemAumento}%\n seu novo salário é de R${salarioNovo}")

# Exercício 8:
# preco = float(input("Digite o prço da mercadoria:"))
# desconto = int(input("Digite o valor do desconto:"))
# precoNovo = ((desconto / 100) * preco) - preco
# print(f"Com esse valor de desconto: {desconto}%\n o preço fica: R${precoNovo}")

# Exercício 9: 
# distancia = int(input("Digite a distância a ser percorrida:"))
# velocidadeMedia = float(input("Digite a velocidade média:"))
# tempo = distancia / velocidadeMedia
# print(f"Essa viagem de distância: {distancia}km e se mantida a velocidade média de: {velocidadeMedia}km/hr\n será necessário {tempo} horas para a conclusão do trajeto.")

# Exercício 10:
# grausC = int(input("Digite os graus (C):"))
# grCEmFR = ((9 * grausC) / 5) + 32
# print(f"{grausC} C° em Fahrenheit equivale à {grCEmFR} F°")

# Exercício 11:
# diasAluguel = int(input("Qunatidade de dias que o carro foi alugado:"))
# kmsPercorridos = float(input("Digite quantos KMs foram percorridos pelo carro:"))
# valorPorDiaAlugado = diasAluguel * 60
# valorPorKmRodado = kmsPercorridos * 0.15
# valorTotal = valorPorDiaAlugado + valorPorKmRodado
# print(f"O valor total pelo aluguel e KMs rodadas é de R${valorTotal}")

# Exercício 12:
#qntCigDia = int(input("Digite quantos cigarros você fuma por dia:"))
#qntAnoFum = int(input("Digite a quantos anos você fuma:"))
#
#totalDias = qntAnoFum * 365 -> Total de dias fumados
#totalCigarros = qntCigDia * totalDias -> Total de cigarros fumados
#minutosPerdidos = totalCigarros * 10 -> Minutos de vida perdidos
#diasPerdidos = minutosPerdidos / 1440 -> Conversão de minutos perdidos para dias perdidos
#print(f"Você já perdeu {diasPerdidos} dias de vida")

# Exercício 13:
# num1 = x
# num2 = y
# 
# if num1 != num2:
#     print("True")
# else:
#     print("False")


