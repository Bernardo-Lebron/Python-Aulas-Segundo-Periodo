'''
#exe01

class Restaurante():
    def __init__(self, nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha


    def descreve_restaurante(self):
        print(f"O nome do restaurante é {self.nome.title()} e seu tipo de cozinha é {self.cozinha}")


    def restaurante_aberto(self):
        horario = int(input("Que horas são? "))
        if (horario >= 18):
            print("O restaurante está aberto!")
        else:
            print("O restaurante está fechado!")


restaurante = Restaurante("Carone", "Italiana")
print("\n")
restaurante.descreve_restaurante()
print("\n")
restaurante.restaurante_aberto()
print("\n")

#exe02

class Cliente():
    def __init__(self, first_name, last_name, cpf, historico):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.historico = historico


    def describe_client(self):
        print(f"Nome: {self.first_name}\nSobrenome: {self.last_name}\nCPF: {self.cpf}")

    
    def greet_client(self):
        print(f"Seja bem vindo {self.first_name}")


    def mostrar_historico(self):
        print("historico de pedidos:")
        for i in self.historico:
            print(f" - {i}")


lista = ["Pizza", "Hamburguer", "Refrigerante"]

cliente = Cliente("Bernardo", "Lebron", "139.861.326-60", lista)

cliente.describe_client()
cliente.greet_client()
cliente.mostrar_historico()
'''
#exe03

class Restaurante():
    def __init__(self, nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha


    def descreve_restaurante(self):
        print(f"O nome do restaurante é {self.nome.title()} e seu tipo de cozinha é {self.cozinha}")


    def restaurante_aberto(self):
        horario = int(input("Que horas são? "))
        if (horario >= 18):
            print("O restaurante está aberto!")
        else:
            print("O restaurante está fechado!")


    def number_served(self):
        numero = int(input("Quantos clientes o restaurante atendeu até agora? "))
        print(f"{numero} clientes!")


restaurante = Restaurante("Carone", "Italiana")
restaurante.descreve_restaurante()
restaurante.restaurante_aberto()
restaurante.number_served()
