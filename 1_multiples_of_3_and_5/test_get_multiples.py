# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

import unittest
from get_multiples import get_list_of_numbers

class TestGetMultiples(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_ranges_list = [
            [[3, 5, 6, 9], 23]
        ]
    
    def test_get_list_of_numbers(self):
        for item in self.test_ranges_list:
            self.assertEqual(sum(item[0]), item[1])

if __name__ == '__main__':
    unittest.main()