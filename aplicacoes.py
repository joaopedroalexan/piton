import time

lista = [17,3,11,5,1,9,7,15,18]
maior_numero = lista[0]

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]
print("O Maior numero da lista é ", maior_numero)

#Exemplo2
my_list = [17,3,11,5,1,9,7,15,18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)

#Exemplo3:
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = i
print("maior valor 3: ", mel)

frutas = ["abacaxi","maça","pera","mamao","uva","melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("elemento encontrado no indice ", i)
else:
    print("NÃO ENCONTRADO!!!")
time.sleep