import unittest

#exe01

def inverter_string(s):
    return s[::-1]


class TestInverterString(unittest.TestCase):
    def test_string_normal(self):
        self.assertEqual(inverter_string("Python"), ("nohtyP"))

if __name__ == '__main__':
    unittest.main()

#exe02

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


class TestNumeroPrimo(unittest.TestCase):
    def test_numero_primo(self):
        self.assertTrue(eh_primo(7))
        self.assertTrue(eh_primo(10))
        self.assertTrue(eh_primo(1))
        self.assertTrue(eh_primo(101))


if __name__ == '__main__':
    unittest.main()

#exe03

class Retangulo:
    def __init__(self, base, altura,):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class TestRetangulo(unittest.TestCase):
    def test_area(self):
        r = Retangulo(10, 5)
        self.assertEqual(r.area(), 50)


class TestPerimetro(unittest.TestCase):
    def test_perimetro(self):
        r = Retangulo(10, 5)
        self.assertEqual(r.perimetro(), 30)


if __name__ == '__main__':
    unittest.main()
