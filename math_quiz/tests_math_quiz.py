import unittest
from math_quiz import Number_Generator, Operator_Generator, Problem_Solution_Generator


class TestMathGame(unittest.TestCase):

    def test_Number_Generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(700):  # Test a large number of random values
            rand_num = Number_Generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Operator_Generator(self):
        # Test if Operator_Generator returns one of the valid operators
        valid_operators = {'+', '-', '*'}
        for _ in range(700):  # Test a large number of outputs
            operator = Operator_Generator()
            self.assertIn(operator, valid_operators)

    def test_Problem_Solution_Generator(self):
        # Define test cases for Problem_Solution_Generator
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 4, '-', '10 - 4', 6),
            (3, 3, '*', '3 * 3', 9),
            (8, 5, '+', '8 + 5', 13),
            (7, 2, '-', '7 - 2', 5),
            (6, 6, '*', '6 * 6', 36)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = Problem_Solution_Generator(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
