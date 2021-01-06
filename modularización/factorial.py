import unittest

def factorial(num):
    if num == 0:
        producto=1
    elif num == 1:
        producto=1
    else:
        producto=num*factorial(num-1)
    return producto

class factorialTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(factorial(6), 720)

    def test_two(self):
        self.assertEqual(factorial(3), 6)

    def test_three(self):
        self.assertEqual(factorial(9), 362880)

    def test_four(self):
        self.assertEqual(factorial(2), 2)

if __name__ == '__main__':
    unittest.main()
