#exe01

bandas = ['AcDc', 'Black Sabbatah', 'Metallica', 'Iron Maiden']

print(bandas[0])

#exe02

names = ['Bernardo', 'Rafaela', 'Marli', 'Neneco', 'Nick', 'Tuco']

print(names[0], names[1], names[2], names[3], names[4], names[5])

print(f"Olá {names[0]}, tudo bem?")
print(f"Olá {names[1]}, como está?")
print(f"Olá {names[2]}, tudo joia?")
print(f"Olá {names[3]}, e a família?")
print(f"Olá {names[4]}, bom demais?")
print(f"Olá {names[5]}, como vai?")

#exe03

transportes = ['Carro', 'Moto', 'Bicicleta', 'Avião', 'Patinete']

print(f"Gostaria de ter um {transportes[0]}")
print(f"Gostaria de ter uma {transportes[1]}")
print(f"Gostaria de ter uma {transportes[2]}")
print(f"Gostaria de ter um {transportes[3]}")
print(f"Gostaria de ter um {transportes[4]}")

#exe04

tamanho = len(bandas)

for i in range(tamanho):
    print(bandas[i])

#exe05

tamanho_names = len(names)

for i in range(tamanho_names):
    print(f"Olá {names[i]}")

#exe06

for i in range(5):
    if i == 3:
        print("Encontrei o 3, saindo do loop")
        break
    print(i)

print("Estou fora do for")    

#exe07

for i in range(5):
    if i == 2:
        print("Pulando o 2")
        continue
    print(i)

#exe08

nomes = ['Bernardo', 'Rafaela']
idades = ['22', '21']

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

#exe09

numeros = [1,2,3,4,5]

quadrados = [numero**2 for numero in numeros]
print(quadrados)

#exe10

pares = [numero for numero in range(10) if numero % 2 ==0]
print(pares)

#exe11

pares_aninhados = [(x,y) for x in range(2) for y in range(2)]
print(pares_aninhados)

#exe12

bandas.append("Ana Castela")
print(bandas)

#exe13

bandas[-1] = "Jorge e Mateus"
print(bandas)

#exe14

bandas.insert(0, "Raul Seixas")
print(bandas)

#exe15

bandas.insert(-2, "Banda Eva")
print(bandas)