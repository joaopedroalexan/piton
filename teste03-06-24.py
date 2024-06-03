import time

#Biblioteca para retonar um número inteiro aleatorio
# from random import randint as rd
# sorteado = rd(-100, 100)# sorteia um número de -100 a 100

# print(sorteado)

#criando uma lista de numeros inteiros aleatorios
# lista = [rd(1,6) for i in range (1, 11)]
# lista2 = [x for x in range(1, 11)]
# lista3 = ["rolo compressor!!!" for f in range(1, 5)]
# print(lista)
# print(lista2)
# print(lista3)

#criando lista par
# par = [i for i in range(10) if i%2 == 0]
# print(par)

#povoando uma lista com "input"
# listaUsuario = [input("digite um numero: ")for p in range(5)]

# print(listaUsuario)

# Ultilizando o metodo split (cada palavra se torna um elemento da lista)_
# nome = "mickey mouse"
# print(nome)
# print(nome.split())
# print(nome)

# #aplicando o "split" com o input
# notas = [n for n in input("notas: ").split()]
# print(notas)

# notas2 = [float(n) for n in input("notas: ").split(",")]
# print(notas2)

# listaMista = [17, 70.5, "Sem Mundial", True]
# # print(listaMista)

# #Manipulação / fatiamento de lista
# veiculos1 = ["carro", "bicicleta","motor"]
# print("veiculos1: ", veiculos1)


# #copiando todo o conteudo de uma lista para outra
# veiculos2 = veiculos1[:]
# del veiculos1[2]
# print("veiculos 1: ", veiculos1)
# print("Veiculos2: ", veiculos2)

# #copiando parte do conteudo de uma lista
# veiculos3 = veiculos2[0:1]
# print(veiculos3)

# veiculos3 = veiculos1[1:-1]
# print(veiculos3)

# veiculos4 = veiculos2[0:-1]
# print(veiculos4)

# veiculos5 = veiculos2[-1:1]
# print(veiculos5)

# my_list = ["A", "b", "c", "d", "e", "f"]
# print(my_list)
# new_list = my_list[:3]
# print(new_list)
# new_list_fim = my_list[3:]
# print(new_list_fim)

# del my_list[1:3]
# print(my_list)
# del my_list[:]
# print(my_list)

naosei =["A", "b", "18", "15"]
print ("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)

time.sleep(1)