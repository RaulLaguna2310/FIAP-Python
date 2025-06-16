# Listas
# Uma lista em Python é uma estrutura qe armazena vários dados, que podem ou não ser do mesmo tipo;
# A estrutura de um alista é:
    # lista = [elemento1, elemento2, elemento3, ...]

# Listas são mutáveis, ou seja, podem ser alteradas após a criação;
# Acesso por meio de índices inteiros, começando do 0;

# Podemos verificar se um elemento está presente na lista usando o operador "in":
    # Esse operador retorna um valor booleano (True ou False);

# Podemos inserir elementos em uma lista usando o método append():
    # animais = []
    # animais.append("gato")

# A operação de soma em listas concatena as duas, colocando os elementos da segunda lista no final da primeira;
    # O operador de multiplicação "*" faz a concatenção se repitir;

# list.insert(indice, elemento): insere um elemento na lista em uma posição específica;
# del lista[indice]: remove o elemento na posição especificada;
# list.remove(elemento): remove o primeiro elemento encontrado na lista que seja igual ao elemento especificado;
# count(elemento): conta quantas vezes o elemento aparece na lista;
# index(elemento): retorna o índice do primeiro elemento encontrado na lista que seja igual ao elemento especificado;
# pop(indice): remove e retorna o elemento na posição especificada (ou o último elemento se nenhum índice for fornecido);
# reverse(): inverte a ordem dos elementos na lista;
# sort(): ordena os elementos da lista em ordem crescente (ou decrescente, se especificado);
# sorted(lista): retorna uma nova lista ordenada, sem modificar a lista original;
# copy(): cria uma cópia superficial da lista;
# min(lista): retorna o menor elemento da lista;
# max(lista): retorna o maior elemento da lista;
# sum(lista): retorna a soma dos elementos da lista (se forem numéricos);

# Pilhas:
# Pilhas são estruturas de dados onde se insere e retira do topo;
# Utilizando de listas como pilhas:
# pilha = [3, 4, 5]
# pilha.append(6)
# pilha.append(7)
# print(pilha)
# [3, 4, 5, 6, 7]
# print(pilha.pop())
# print(pilha)
# pilha = [3, 4, 5, 6]
# print(pilha.pop())
# pilha = [3, 4, 5]

# Filas:
# Filas são estruturas de dados onde se insere no fim e se retira do início;
# Utilizando de listas como filas:
# Fila = [ “João”, “Maria”]
# Fila.append(“José”)
# Fila.pop(0)
# “João”
# print(Fila)
# [ “Maria”, “José”]