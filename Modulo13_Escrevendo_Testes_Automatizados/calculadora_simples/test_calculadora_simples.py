from calculadora import somar
import unittest

""" #  Testa soma de dois números inteiros:
if somar(2, 4) == 6:
    print("PASS")
else:
    print("FAIL")

#  Testa soma de número com zero:
if somar(0, 4) == 4:
    print("PASS")
else:
    print("FAIL")

#  Testa soma de número negativo:
if somar(-2, 0) == -2:
    print("PASS")
else:
    print("FAIL")

#  Testa soma com número float:
if somar(-2.5, 0) == -2.5:
    print("PASS")
else:
    print("FAIL") """

class TestSomar(unittest.TestCase):
    def soma_inteiro(self):
        self.assertEqual(somar(1, 1),2)

unittest.main()