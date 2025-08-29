from decimal import Decimal


#####

nome = 'Lebron'
idade = 21

print("Idade:" + str(idade), "\nNome:" + nome, end="\n\n") 

#####

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"{nome}, tem {idade} anos\n")

#####

letra = 'A'

print(letra)
print(type(letra))
print(len(letra), end="\n\n")

#####

x = 10

print(x)
print(x>5)
print(x==0, end="\n\n")

#####

pi = 3.14159

print(type(pi))
print(pi, end="\n\n")

#####

y = Decimal("0.1") + Decimal("0.2")

print(f"{y:.10f}")

z = 0.1 + 0.2

print(f"{z:.10f}", end="\n\n")

#####

