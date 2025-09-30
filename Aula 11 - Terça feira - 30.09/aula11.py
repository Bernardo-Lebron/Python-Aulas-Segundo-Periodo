from random import randint

#exe01
cadastro = {}

while True:
    cadastro['CPF'] = input('Digite o CPF: ')
    cadastro['ID'] = input('Digite o ID: ')
    cadastro['CEP'] = input('Digite o CEP: ')
    cadastro['Cidade natal'] = input('Digite a cidade natal: ')
    cadastro['Telefone'] = input('Digite o telefone: ')
    var = input('Deseja continuar? (S/N): ')
    if var.upper() == 'N':
        break

print('Cadastro realizado com sucesso!')
print(cadastro)

#exe02

estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil)

#exe04

user_0 = {'username': 'miziphi', 'first': 'Guido', 'last': 'Pantuza', 'idade': 40}

for i, value in user_0.items():
    print('\nKey: {}'.format(i))
    print('Value: {}'.format(value))

#exe05

user_0 = {'username': 'miziphi', 'first': 'Guido', 'last': 'Pantuza', 'idade': 40}

for i in user_0.keys():
    print("\nKey: {}".format(i), end=' ')

#exe06

user_0 = {'username': 'miziphi', 'first': 'Guido', 'last': 'Pantuza', 'idade': 40}

for i in user_0.values():
    print("Valor: {}".format(i))

#exe07

fav_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'c', 'phil': 'python', }

print('As linguagens citadas foram: ')

for language in set(fav_languages.values()): 
    print(language.title())

#exe08

notas = {
    "Nick" : randint(1,10),
    "Bernardo": randint(1,10),
    "Rafaela": randint(1,10),
    "Junio": randint(1,10),
    "Marli": randint(1,10)
}

print(notas)

media = sum(notas.values())/ len(notas)

if media < 6:
    print("Rever metodologia!")
elif media == 6:
    print("Por pocuo!")
elif media > 6 and media < 8:
    print("Satisfatório!") 
elif media >= 8:
    print("Aí sim!")

#exe09

glossario = {
    "append" : "Adiciona um elemento ao final da lista",
    "pop" : "Remove e retorna o último elemento da lista (ou de um índice específico)",
    "insert" : "Insere um elemento em uma posição especifica na lista",
    "sort" : "Ordena a lista em ordem crescente por padrão",
    "remove" : "Remove a primeira ocorrência de um valor especificado na lista"
}

for palavra, significado in glossario.items():
    print(f"{palavra}:\n\t{significado}\n")

