import unittest
from fibonacci import fibonacci
from fibonacci import words2numgreat3

"""
Call the number sequence of the fibonacci sequence and show what value it is in integers and numbers
"""


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        fib_sequence_value = 13
        fib_value = fibonacci(fib_sequence_value)
        fib_big_word = words2numgreat3(fib_value)
        print(str(fib_value) + ' - ' + fib_big_word)


if __name__ == '__main__':
    unittest.main()