import time

# Exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0]

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero

print("O Maior número da lista é ", maior_numero)

# Exemplo 2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]

for numero in my_list:
    if numero > maior:
        maior = numero

print("Maior valor:", maior)

# Exemplo 3
ultima_lista = my_list[:]
mel = ultima_lista[0]

for numero in ultima_lista[1:]:
    if numero > mel:
        mel = numero

print("Maior valor:", mel)

# Exemplo 4
frutas = ["abacaxi", "maça", "pera", "mamao", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    if frutas[i] == elemento:
        achado = True
        break

if achado:
    print("Elemento encontrado no índice", i)
else:
    print("NÃO ENCONTRADO!!!")

# Exemplo 5
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in apostados:
    if numero in sorteados:
        acertos += 1

print("Número de acertos:", acertos)

# Exemplo 6
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original:", lista)

# Lista de apoio
vistos = []

# Iterar
for numero in lista[::-1]:  # Inverter a lista para percorrer do fim ao início
    if numero in vistos:
        lista.remove(numero)
    else:
        vistos.append(numero)

print("Lista modificada:", lista)

# Matriz tridimensional
cubo = [[["1,2,3"], ["2,3,1"], ["3,2,1"]],[["4,5,6"], ["5,6,4"], ["6,5,4"]],[["7","8","9"],["8","9","7"],["9","8","7"]]]

print(cubo)
print(cubo[1])
print(cubo[1],[0])
print(cubo[1],[0],[2])

time.sleep(1)
