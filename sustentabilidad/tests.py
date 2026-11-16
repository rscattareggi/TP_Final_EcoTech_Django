import unittest

from .views import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_normal(self):

        resultado = calcular_emisiones_carbono(
            1000
        )

        self.assertEqual(
            resultado,
            400.0
        )

    def test_calculo_factor_personalizado(self):

        resultado = calcular_emisiones_carbono(
            1000,
            0.5
        )

        self.assertEqual(
            resultado,
            500.0
        )

    def test_consumo_negativo(self):

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-100)
