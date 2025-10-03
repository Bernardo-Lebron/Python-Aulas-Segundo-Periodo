#exe01

rios = {
    "Rio Nilo" : "Egito",
    "Rio Amazonas" : "Brasil",
    "Rio Yangtzé" : "China"
}

for rio, pais in rios.items():
    print(f"O {rio} esta localizado no país: {pais}!".format())

for rio in rios.keys():
    print(rio)

for pais in rios.values():
    print(pais)

#exe02

respostas = {
    "João": "python",
    "Maria": "C",
    "Pedro": "Java",
}

pessoas = ['João', 'Ana', 'Pedro', 'Carla', 'Maria', 'Beatriz']

for pessoa in pessoas:
    if pessoa in respostas:
        print(f"Obrigado por participar da pesquisa {pessoa}!")
    else:
        print(f"{pessoa}, você ainda não respondeu a enquete")

#exe03

Nick = {
    "tipo" : "Cachorro",
    "dono" : "Lebron"
}

Geremias = {
    "tipo" : "Gato",
    "dono" : "Rafaela"
}

Sextafeira = {
    "tipo" : "Papagaio",
    "dono" : "Lica"
}

pets = [Nick, Geremias, Sextafeira]

for pet in pets:
    print(f"{pet["dono"]} tem um {pet["tipo"]}".format())

#exe04

favorite_places = {
    "Bernardo": ["Carmópolis", "Belo Horizonte", "Maceió"],
    "Rafaela": ["Carmópolis", "Salvador", "Rio de Janeiro"],
    "Nick": ["Quintal", "Terreiro", "Roça"]
}

for nome, lugares in favorite_places.items():
    print(f"\nOs lugares favoritos de {nome} são: ")
    for lugar in lugares:
        print(f"- {lugar}")