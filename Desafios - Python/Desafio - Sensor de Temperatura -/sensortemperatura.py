import unittest
import random
from unittest.mock import patch

class SensorTemperatura:
    def __init__(self):
        self.temperatura = None


    def ler_temperatura(self):
        """Gera uma temperatura aleatória entre -10 e 50°C"""

        self.temperatura = random.uniform(-10, 50)
        return self.temperatura


    def em_alerta(self):
        """Retorna True se a temperatura for superior a 40°C"""

        if self.temperatura is None:
            self.ler_temperatura()
        return self.temperatura > 40


class TestSensorTemperatura(unittest.TestCase):
    @patch('random.uniform', return_value=25.0)
    def test_temperatura_normal(self, mock_random):
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        self.assertEqual(temp, 25.0)
        self.assertFalse(sensor.em_alerta()) 


    @patch('random.uniform', return_value=40.0)
    def test_limite_sem_alerta(self, mock_random):
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        self.assertEqual(temp, 40.0)
        self.assertFalse(sensor.em_alerta())


    @patch('random.uniform', return_value=41.0)
    def test_acima_limite_alerta(self, mock_random):
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        self.assertEqual(temp, 41.0)
        self.assertTrue(sensor.em_alerta())


    @patch('random.uniform', return_value=-5.0)
    def test_temperatura_negativa(self, mock_random):
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        self.assertEqual(temp, -5.0)
        self.assertFalse(sensor.em_alerta())


if __name__ == "__main__":
    unittest.main()