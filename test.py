import unittest

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()


"""
TEST RESULTS:

The unit test checks whether the sum function correctly adds the
numbers in the list [1, 2, 3]. The expected answer is 6. If the test
passes, it means the function returned the expected result and is
working correctly for this test case. If the test fails, it means the
function returned a different result than what was expected.
"""
