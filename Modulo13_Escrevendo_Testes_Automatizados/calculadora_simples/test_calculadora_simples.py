from calculadora import somar, dividir, multiplicar, subtrair
import unittest


class TestSomar(unittest.TestCase):

    def test_soma_inteiro(self):
        soma = somar(1, 2)
        self.assertEqual(soma, 3)

    def test_soma_zero(self):
        self.assertEqual(somar(0, 2), 2)
    
    def test_soma_negativo(self):
        self.assertEqual(somar(0, -2), -2)
    
    def test_soma_float(self):
        self.assertEqual(somar(0.5, -2), -1.5)

class TestDividir(unittest.TestCase):
    
    def test_divisao_por_um(self):
        divide = dividir(2, 1)
        self.assertEqual(divide, 2)
    
    def test_divisao_inteiro(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_divisor_maior(self):
        self.assertEqual(dividir(2, 10), 0.2)
    
    def test_divisao_por_zero(self):
        self.assertEqual(dividir(10, 0), "Não é um número")
    
    def test_divisao_divisor_negativo(self):
        self.assertEqual(dividir(10, -2), -5)
    
    def test_divisao_dividendo_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_divisao_ambos_negativo(self):
        self.assertEqual(dividir(-10, -2), 5)
    
    def test_divisao_float(self):
        self.assertEqual(dividir(10, 0.5), 20)
    
    def test_divisao_nao_exata(self):
        self.assertEqual(dividir(3, 2), 0.5)
    
class TestMultiplicar(unittest.TestCase):

    def test_multiplicacao_por_um(self):
        self.assertEqual(multiplicar(10, 1), 10)
    
    def test_multiplicacao_ordem_nao_altera_resultado(self):
        self.assertEqual(multiplicar(2, 3), multiplicar(3, 2))
    
    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicar(123, 0), 0)
    
    def test_multiplicar_por_float(self):
        self.assertEqual(multiplicar(10, 0.5), 5)
    
    def test_multiplicar_por_negativo(self):
        self.assertEqual(multiplicar(4, -2), -8)
    
class TestSubtrair(unittest.TestCase):

    def test_subtrair_inteiro(self):
        self.assertEqual(subtrair(10, 6), 4)
    
    def test_subtrair_subtraendo_maior(self):
        self.assertEqual(subtrair(6,10), -4)
    
    def test_subtrair_negativo(self):
        self.assertEqual(subtrair(10, -10), 20)
    
    def test_subtrair_minuendo_negativo(self):
        self.assertEqual(subtrair(-10, 2), -12)
    
    def test_subtrair_ambos_negativos(self):
        self.assertEqual(subtrair(-10, -10), 0)

    def test_subtrair_por_zero(self):
        self.assertEqual(subtrair(10, 0), 10)

if __name__ == '__main__':
    unittest.main()
