import math
#exe01

a = [1,2,3,4,5,6,7]
b = a
c = a[:]
b[0] = -1

print(a)
print(b)
print(c)

#exe02

n = int(input("Informe a quantidade de termos: "))

valores = []

for i in range(n):
    numero = int(input(f"Informe o {i+1} valor: "))
    valores.append(numero)

media = sum(valores)/n

soma = 0

for x in valores:
    soma +=(x-media)**2

desvio_padrao = math.sqrt(soma/(n-1))

print(f"A media dos dados é: {media}")
print(f"O desvio padrão dos dados é: {desvio_padrao}")

#exe03

a = set()
b = set()

qtd_a = int(input("informe quantos numeros deseja adicionar no conjunto 'a': "))

for i in range(qtd_a):
    num = input(f"Informe o {i+1}º numero que deseja adicionar: ")
    a.add(num)

qtd_b = int(input("informe quantos numeros deseja adicionar no conjunto 'a': "))

for i in range(qtd_b):
    num = input(f"Informe o {i+1}º numero que deseja adicionar: ")
    b.add(num)

print(f"A intereseção dos conjutos é {a&b}")

#exe04

qtd_a = list(map(int, input("informe uma sequencia de numeros deseja adicionar no conjunto 'a': ").split()))

qtd_b = list(map(int, input("informe uma sequencia de numeros deseja adicionar no conjunto 'b': ").split()))

seq_completa = qtd_a + qtd_b

seq_completa.sort()

print(f"lista ordenada: {seq_completa}")

#exe05

n1 = float(input("Informe 1ª nota: "))
n2 = float(input("Informe 2ª nota: "))
n3 = float(input("Informe 3ª nota: "))

var = int(input("\n1-media aritimetica \n2-media ponderada \n3-media harmonica\n\nInforme qual função deseja executar: "))

match var:
    case 1:
        aritimetica = (n1+n2+n3)/3
        print(aritimetica)
    case 2:
        ponderada = ((n1*3)+(n2*3)+(n3*4))/(3+3+4)
        print(ponderada)
    case 3:
        harmonica = 3/((1/n1)+(1/n2)+(1/n3))
        print(harmonica)
    case _:
        print("Opção inválida!")