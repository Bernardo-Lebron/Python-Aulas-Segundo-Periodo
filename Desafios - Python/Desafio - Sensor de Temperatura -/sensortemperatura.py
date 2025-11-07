import unittest
import random
from unittest.mock import patch


class SensorTemperatura:
    def __init__(self):
        self.temperatura = None


    def ler_temperatura(self):
        """Simula leitura aleatória entre -10 e 50 °C"""

        self.temperatura = random.uniform(-10, 50)
        print(f"[INFO] Temperatura atual: {self.temperatura:.2f}°C")
        return self.temperatura


    def em_alerta(self):
        """Retorna True se a temperatura for superior a 40 °C"""
        
        if self.temperatura is None:
            self.ler_temperatura()
        alerta = self.temperatura > 40
        print(f"[ALERTA] {'SIM' if alerta else 'NÃO'} (Temperatura: {self.temperatura:.2f}°C)")
        return alerta


class TestSensorTemperatura(unittest.TestCase):

    @patch('random.uniform', return_value=25.0)
    def test_temperatura_normal(self, mock_random):
        """Temperatura normal: deve ser 25°C e sem alerta"""
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        print(f"[TESTE] Temperatura simulada: {temp:.2f}°C")
        self.assertEqual(temp, 25.0)
        self.assertFalse(sensor.em_alerta())

    @patch('random.uniform', return_value=40.0)
    def test_limite_sem_alerta(self, mock_random):
        """Temperatura no limite: 40°C — não deve ativar alerta"""
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        print(f"[TESTE] Temperatura simulada: {temp:.2f}°C")
        self.assertEqual(temp, 40.0)
        self.assertFalse(sensor.em_alerta())

    @patch('random.uniform', return_value=41.0)
    def test_acima_limite_alerta(self, mock_random):
        """Temperatura acima do limite: 41°C — deve ativar alerta"""
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        print(f"[TESTE] Temperatura simulada: {temp:.2f}°C")
        self.assertEqual(temp, 41.0)
        self.assertTrue(sensor.em_alerta())

    @patch('random.uniform', return_value=-5.0)
    def test_temperatura_negativa(self, mock_random):
        """Temperatura negativa: -5°C — não deve ativar alerta"""
        sensor = SensorTemperatura()
        temp = sensor.ler_temperatura()
        print(f"[TESTE] Temperatura simulada: {temp:.2f}°C")
        self.assertEqual(temp, -5.0)
        self.assertFalse(sensor.em_alerta())


if __name__ == "__main__":
    unittest.main()

    