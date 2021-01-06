import unittest

def fibonacci(num):
    if num == 1:
        num_fibonacci=0
    elif num == 2:
        num_fibonacci=1
    else:
        num_fibonacci=fibonacci(num-1)+fibonacci(num-2)
    return num_fibonacci


class fibonacciTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fibonacci(5), 3)

    def test_two(self):
        self.assertEqual(fibonacci(8), 13)

    def test_three(self):
        self.assertEqual(fibonacci(10), 34)

    def test_four(self):
        self.assertEqual(fibonacci(11), 55)

if __name__ == '__main__':
    unittest.main()