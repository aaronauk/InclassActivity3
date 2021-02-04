import sys
import unittest
import calculator

#In function calculator(a,b,c):
#a, b - numbers
#c - choice
#choice 1 - add
#choice 2 - subtract
#choice 3 - multiply
#choice 4 - divide

#To compile and run: python3 test_calculator.py

class TestCalculator(unittest.TestCase):
    #Addition Test Cases
    #test positive
    def test_add(self):
        self.assertEqual(calculator.calculator(5, 5, 1), 10)

    #test invalid
    def test_addInvalid(self):
        self.assertEqual(calculator.calculator("six", 4, 1), None)

    #test float
    def test_addFloat(self):
        self.assertAlmostEqual(calculator.calculator(3.5, 6.6, 1), 10.1)

    #test negative
    def test_addNegative(self):
        self.assertAlmostEqual(calculator.calculator(-2, 4.5, 1), 2.5)

    #Subtraction Test Cases
    #test positive
    def test_subtract(self):
        self.assertEqual(calculator.calculator(6, 4, 2), 2)

    #test invalid
    def test_subtractInvalid(self):
        self.assertEqual(calculator.calculator("four", 4, 2), None)

    #test float
    def test_subtractFloat(self):
        self.assertAlmostEqual(calculator.calculator(11.5, -4, 2), 15.5)

    #test negative
    def test_subtractNegative(self):
        self.assertAlmostEqual(calculator.calculator(-12, 7, 2), -19)

     #Multiplication Test Cases
    #test positive
    def test_multiply(self):
        self.assertEqual(calculator.calculator(4, 2, 3), 8)

    #test invalid
    def test_multiplyInvalid(self):
        self.assertEqual(calculator.calculator("nine", 2, 3), None)

    #test float
    def test_multiplyFloat(self):
        self.assertAlmostEqual(calculator.calculator(2.4, 6.5, 3), 15.6)

    #test negative
    def test_multiplyNegative(self):
        self.assertAlmostEqual(calculator.calculator(5, -2, 3), -10)


    #Division Test Cases
    #test positive
    def test_divide(self):
        self.assertEqual(calculator.calculator(4, 2, 4), 2)

    #test invalid
    def test_divideInvalid(self):
        self.assertEqual(calculator.calculator("twelve", 4, 4), None)

    #test divide by zero
    def test_divideByZero(self):
        self.assertEqual(calculator.calculator(5, 0, 4), None)

    #test float
    def test_divideFloat(self):
        self.assertAlmostEqual(calculator.calculator(9, 2, 4), 4.5)

    #test negative
    def test_divideNegative(self):
        self.assertAlmostEqual(calculator.calculator(4,-2, 4), -2)

    #Choice Test Cases
    #test invalid choice
    def test_choiceInvalid(self):
        self.assertEqual(calculator.calculator(4, 3, 5), None)


if __name__ == "__main__":
    unittest.main()