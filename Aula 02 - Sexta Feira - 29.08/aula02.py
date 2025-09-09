from decimal import Decimal

#exe01

nome = 'Lebron'
idade = 21

print("Idade:" + str(idade), "\nNome:" + nome, end="\n\n") 

#exe02

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"{nome}, tem {idade} anos\n")

#exe03

letra = 'A'

print(letra)
print(type(letra))
print(len(letra), end="\n\n")

#exe04

x = 10

print(x)
print(x>5)
print(x==0, end="\n\n")

#exe05

pi = 3.14159

print(type(pi))
print(pi, end="\n\n")

#exe06

y = Decimal("0.1") + Decimal("0.2")

print(f"{y:.10f}")

z = 0.1 + 0.2

print(f"{z:.10f}", end="\n\n")