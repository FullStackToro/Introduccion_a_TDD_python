import unittest

def isPalindrome(array):
    reverse = ''

    for x in range(len(array), 0, -1):
        reverse += array[x-1]
        print(reverse)
        print(array)
    if reverse.lower() == array.lower():
        return True
    else:
        return False


class isPalindromeTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def test_two(self):
        self.assertEqual(isPalindrome("rabcr"), False)

    def test_three(self):
        self.assertEqual(isPalindrome("Neuquen"), True)

    def test_four(self):
        self.assertEqual(isPalindrome("Reconocer"), True)

    def test_five(self):
        self.assertEqual(isPalindrome("palindromo"), False)

    def test_six(self):
        self.assertEqual(isPalindrome("amor a roma"), True)

if __name__ == '__main__':
    unittest.main()
