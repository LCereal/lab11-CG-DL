# https://github.com/LCereal/lab11-CG-DL
# Partner 1: Cyryl Gildore
# Partner 2: David Losada

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 5)
        self.assertEqual(mul(2, 15), 30)
        self.assertEqual(mul(4, 3), 12)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(6, 3), 2)
        self.assertAlmostEqual(div(6, 2), 3)
        self.assertAlmostEqual(div(6, 1), 6)
                
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(7, 24), 25)
                

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(64), 8)
        self.assertEqual(square_root(100), 10)
                

# Do not touch this
if __name__ == "__main__":
    unittest.main()