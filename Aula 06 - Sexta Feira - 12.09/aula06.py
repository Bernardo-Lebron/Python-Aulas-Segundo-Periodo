#exe01

numeros = [1, 2, 3, 4, 5]

del numeros[-1]

print(numeros)

#exe02

numeros = [1, 2, 3, 4, 5]

retirado =  numeros.pop(-1)

print(numeros)
print(retirado)

#exe03

nomes = []

for i in range(8):
    nome = input("Informe um convidado: ")
    if nome == 'q':
        break
    nomes.append(nome)

tamanho = len(nomes) 

nao_confirmaram = []

for i in range(tamanho):
    desconvidar = input("Digite um nome que não confirmou (se todos confimara aperte enter): ")
    if bool(desconvidar) == False:
        break
    if desconvidar in nomes:
        nomes.remove(desconvidar)
        nao_confirmaram.append(desconvidar)
        convidar = input("Deseja convidar outra pessoa no lugar? (digite o nome ou enter para não): ")
        if convidar:
            nomes.append(convidar)

for nome in nomes:
    print(f"{nome}, você está convidado!")

for pessoa in nao_confirmaram:
    print(f"O convidado {pessoa} não poderá comparecer")