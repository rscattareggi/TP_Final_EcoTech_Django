from django.test import TestCase
from .views import calcular_emisiones_carbono
class TestCalculo(TestCase):
 def test_ok(self): self.assertEqual(calcular_emisiones_carbono(100),40)
