import unittest
import math

def monedas(num):
    total=[]
    valor_moneda=[25, 10, 5, 1]
    temp = num
    for x in range (len(valor_moneda)):
        total.append(math.trunc(temp/valor_moneda[x]))
        temp=temp-total[x]*valor_moneda[x]
    print(num, temp, valor_moneda[x],total)
    return total

class monedasTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(monedas(87), [3, 1, 0, 2])

    def test_two(self):
        self.assertEqual(monedas(125), [5, 0, 0, 0])

    def test_three(self):
        self.assertEqual(monedas(132), [5, 0, 1, 2])

    def test_four(self):
        self.assertEqual(monedas(542), [21, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()
