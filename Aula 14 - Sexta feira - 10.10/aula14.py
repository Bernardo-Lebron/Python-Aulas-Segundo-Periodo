#exe01

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


