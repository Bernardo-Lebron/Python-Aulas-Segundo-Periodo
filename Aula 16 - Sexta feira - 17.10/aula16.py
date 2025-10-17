class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base


    def calcular_salario(self,):
        """Método genérico(será sobrescrito pelas classes filhas)"""

        return self.salario_base
    

class Gerente(Funcionario):
    def calcular_salario(self):
        """Gerente recebe bônus de 20% sobre o salario base"""

        return self.salario_base * 1.2
    

class Engenheiro(Funcionario):
    def calcular_salario(self):
        """Engenheiro recebe bônus de 10% sobre o salario base"""

        return self.salario_base * 1.10
    
    
#Programa principal
if __name__ == "__main__":
    funcionario = [
        Gerente("Ana", 8000),
        Gerente("Carlos", 7500),
        Engenheiro("Bruno", 6000),
        Engenheiro("Carla", 4000)
    ]

print("Salarios dos Funcionários:\n")
for f in funcionario:
    print(f"Nome: {f.nome} - Salário: R$ {f.calcular_salario():.2f}")