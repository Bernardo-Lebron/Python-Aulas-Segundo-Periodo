import unittest

#exe01

class Employee:
    def __init__(self, nome, sobrenome, salario_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual

    def give_raise(self, aumento=5000):
        self.salario_anual += aumento

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Bernardo', 'Lebron', 60000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salario_anual, 65000)

    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.salario_anual, 68000)


if __name__ == '__main__':
    unittest.main()

#exe02

class Matematica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.resultado = a + b

    def soma(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        self.resultado = self.a + self.b
        return self.resultado


class TestMatematica(unittest.TestCase):
    def setUp(self):
        self.matematica = Matematica(10, 15)

    def test_soma_defalt_raise(self):
        resultado = self.matematica.soma()
        self.assertEqual(resultado, 25)

    def test_soma_custom_raise(self):
        resultado = self.matematica.soma(30, 25)
        self.assertEqual(resultado, 55)
        

if __name__ == '__main__':
    unittest.main()