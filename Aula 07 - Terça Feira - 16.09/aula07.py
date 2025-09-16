#exe01

from random import randint

numeros = []

for i in range(20):
    numero = randint(1,80)
    numeros.append(numero)

print(numeros)

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
print(f"Amplitude: {max(numeros) - min(numeros)}")
print(f"Soma de todos os números: {sum(numeros)}")
print(f"Média de todos os números: {sum(numeros)/len(numeros)}")
print(f"Média dos 10 primeiros elementos: {sum(numeros[0:10])/len(numeros[0:10])}")
print(f"Maior número dos 10 últimos elementos: {max(numeros[10:20])}")
print(f"Menor número dos 10 últimos elementos: {min(numeros[10:20])}") 

print("\n")

#exe02

pizzas = ["Calabresa", "Portuguesa", "Mussarela"]

for i in range(len(pizzas)):
    print(f"Gosto de pizza de {pizzas[i]}!")

print("Eu realmente adoro pizza!")

print("\n")

#exe03

animais = ["Cachorro", "Gato", "Periquito"]

for i in range(len(animais)):
    print(f"Um {animais[i]} seria um ótimo animal de estimação")

print("Qualquer um desses animais seria um ótimo animal de estimação!")   

print("\n")

#exe04

for numero in range(1,21):
    print(numero ,end=" ")

print("\n")

#exe05

lista = range(1,1000001)

for i in lista:
    print(i)

print(f"Maximo: {max(lista)}")
print(f"Mínimo: {min(lista)}")
print(f"Soma: {sum(lista)}")

print("\n")

#exe06

impares = []

for impares in range(1,20,2):
    print(impares, end=" ")

print("\n")

#exe07

multiplos_de_tres = list(range(3,31,3))

for numero in multiplos_de_tres:
    print(f"{numero}", end=" ")

print("\n")

#exe08

for i in range(1, 11):
    print(i**3, end=" ")