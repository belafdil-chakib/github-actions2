import unittest
from square import square  # Import the function you want to test

class TestSquareFunction(unittest.TestCase):
    
    def test_square_positive(self):
        """
        Test the square function with a positive integer.
        """
        result = square(5)
        expected = 25
        self.assertEqual(result, expected)
    
    def test_square_zero(self):
        """
        Test the square function with zero.
        """
        result = square(0)
        expected = 0
        self.assertEqual(result, expected)
    
    def test_square_negative(self):
        """
        Test the square function with a negative integer.
        """
        result = square(-4)
        expected = 16
        self.assertEqual(result, expected)
    
    def test_square_float(self):
        """
        Test the square function with a floating-point number.
        """
        result = square(3.5)
        expected = 12.25
        self.assertEqual(result, expected)
    
    def test_square_large_number(self):
        """
        Test the square function with a large integer.
        """
        result = square(1000000)
        expected = 1000000000000
        self.assertEqual(result, expected)
    
    def test_square_invalid_input(self):
        """
        Test the square function with an invalid input (like a string).
        Expecting a TypeError to be raised.
        """
        with self.assertRaises(TypeError):
            square("string")

if __name__ == '__main__':
    unittest.main()
