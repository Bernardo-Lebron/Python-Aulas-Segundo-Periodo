'''#exe01
def make_car(marca, modelo, **car_info):
    """Constrói um dicionário que descreve um carro."""
    
    car = {
        'marca': marca,
        'modelo': modelo,
    }

    car.update(car_info)
    return car
    

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''
#exe02

i = input("Informe a quantidade de alunos que deseja lançar as notas: ")
for i in range(int(i)):
    nome = input("Nome do aluno: ")
    nota = input("Nota do aluno: ")
    notas_alunos = {
        "nome": nome,
        "nota": nota,
    }

for i in range(int(i)):
    print(notas_alunos)