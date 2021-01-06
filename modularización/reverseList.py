import unittest

def reverseList(array):
    reverse = []
    for x in range(len(array), 0, -1):
        reverse.append(array[x-1])
    return reverse

class reverseListTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def test_two(self):
        self.assertEqual(reverseList([3, 3, 8]), [8, 3, 3])

    def test_three(self):
        self.assertEqual(reverseList([5, 3, 1]), [1, 3, 5])

    def test_four(self):
        self.assertEqual(reverseList(["a", "b", "c", "d"]), ["d", "c", "b", "a"])

if __name__ == '__main__':
    unittest.main()

