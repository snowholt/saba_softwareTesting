"""
Unit Tests for Personal Finance Calculator

Unit testing focuses on testing individual functions and methods in isolation.
Each test verifies a single function's behavior with various inputs.
"""

import unittest
import math
from finance_calculator.calculator import FinanceCalculator
from finance_calculator.validator import InputValidator


class TestFinanceCalculator(unittest.TestCase):
    """Unit tests for FinanceCalculator class methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = FinanceCalculator()
    
    def test_simple_interest_calculation(self):
        """Test simple interest calculation with valid inputs."""
        # Test basic calculation
        result = self.calculator.calculate_simple_interest(1000, 5, 2)
        self.assertEqual(result, 100.0)
        
        # Test with decimal values
        result = self.calculator.calculate_simple_interest(1500.50, 4.25, 1.5)
        expected = (1500.50 * 4.25 * 1.5) / 100
        self.assertAlmostEqual(result, expected, places=2)
        
        # Test with zero values
        result = self.calculator.calculate_simple_interest(1000, 0, 2)
        self.assertEqual(result, 0.0)
        
        result = self.calculator.calculate_simple_interest(1000, 5, 0)
        self.assertEqual(result, 0.0)
    
    def test_simple_interest_negative_values(self):
        """Test simple interest calculation with negative inputs."""
        with self.assertRaises(ValueError):
            self.calculator.calculate_simple_interest(-1000, 5, 2)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_simple_interest(1000, -5, 2)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_simple_interest(1000, 5, -2)
    
    def test_compound_interest_calculation(self):
        """Test compound interest calculation with valid inputs."""
        # Test annual compounding
        result = self.calculator.calculate_compound_interest(1000, 5, 2, 1)
        expected = 1000 * (1.05) ** 2
        self.assertAlmostEqual(result, expected, places=2)
        
        # Test monthly compounding
        result = self.calculator.calculate_compound_interest(1000, 6, 1, 12)
        expected = 1000 * (1 + 0.06/12) ** 12
        self.assertAlmostEqual(result, expected, places=2)
        
        # Test with zero interest
        result = self.calculator.calculate_compound_interest(1000, 0, 2, 1)
        self.assertEqual(result, 1000.0)
    
    def test_compound_interest_invalid_inputs(self):
        """Test compound interest calculation with invalid inputs."""
        with self.assertRaises(ValueError):
            self.calculator.calculate_compound_interest(-1000, 5, 2, 1)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_compound_interest(1000, 5, 2, 0)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_compound_interest(1000, 5, 2, -1)
    
    def test_monthly_payment_calculation(self):
        """Test monthly loan payment calculation."""
        # Test standard loan
        result = self.calculator.calculate_monthly_payment(10000, 6, 5)
        # Using standard loan payment formula
        monthly_rate = 0.06 / 12
        num_payments = 5 * 12
        expected = 10000 * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                  ((1 + monthly_rate) ** num_payments - 1)
        self.assertAlmostEqual(result, expected, places=2)
        
        # Test zero interest loan
        result = self.calculator.calculate_monthly_payment(12000, 0, 2)
        expected = 12000 / (2 * 12)
        self.assertEqual(result, expected)
    
    def test_monthly_payment_invalid_inputs(self):
        """Test monthly payment calculation with invalid inputs."""
        with self.assertRaises(ValueError):
            self.calculator.calculate_monthly_payment(0, 6, 5)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_monthly_payment(10000, -1, 5)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_monthly_payment(10000, 6, 0)
    
    def test_savings_goal_calculation(self):
        """Test savings goal time calculation."""
        # Test with interest
        result = self.calculator.calculate_savings_goal(5000, 200, 3)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
        
        # Test without interest
        result = self.calculator.calculate_savings_goal(2400, 100, 0)
        expected = 2400 / (100 * 12)
        self.assertEqual(result, expected)
    
    def test_savings_goal_invalid_inputs(self):
        """Test savings goal calculation with invalid inputs."""
        with self.assertRaises(ValueError):
            self.calculator.calculate_savings_goal(0, 200, 3)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_savings_goal(5000, 0, 3)
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_savings_goal(5000, 200, -1)


class TestInputValidator(unittest.TestCase):
    """Unit tests for InputValidator class methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.validator = InputValidator()
    
    def test_validate_positive_number(self):
        """Test positive number validation."""
        # Valid positive numbers
        self.assertEqual(self.validator.validate_positive_number("100"), 100.0)
        self.assertEqual(self.validator.validate_positive_number(50.5), 50.5)
        self.assertEqual(self.validator.validate_positive_number("0.1"), 0.1)
        
        # Invalid inputs
        with self.assertRaises(ValueError):
            self.validator.validate_positive_number("0")
        
        with self.assertRaises(ValueError):
            self.validator.validate_positive_number("-10")
        
        with self.assertRaises(ValueError):
            self.validator.validate_positive_number("abc")
        
        with self.assertRaises(ValueError):
            self.validator.validate_positive_number(None)
    
    def test_validate_non_negative_number(self):
        """Test non-negative number validation."""
        # Valid non-negative numbers
        self.assertEqual(self.validator.validate_non_negative_number("0"), 0.0)
        self.assertEqual(self.validator.validate_non_negative_number("100"), 100.0)
        self.assertEqual(self.validator.validate_non_negative_number(50.5), 50.5)
        
        # Invalid inputs
        with self.assertRaises(ValueError):
            self.validator.validate_non_negative_number("-10")
        
        with self.assertRaises(ValueError):
            self.validator.validate_non_negative_number("abc")
    
    def test_validate_integer(self):
        """Test integer validation."""
        # Valid integers
        self.assertEqual(self.validator.validate_integer("5"), 5)
        self.assertEqual(self.validator.validate_integer(10), 10)
        
        # Invalid inputs
        with self.assertRaises(ValueError):
            self.validator.validate_integer("0")
        
        with self.assertRaises(ValueError):
            self.validator.validate_integer("-5")
        
        with self.assertRaises(ValueError):
            self.validator.validate_integer("5.5")
        
        with self.assertRaises(ValueError):
            self.validator.validate_integer("abc")
    
    def test_validate_loan_inputs(self):
        """Test loan input validation."""
        # Valid inputs
        amount, rate, years = self.validator.validate_loan_inputs("10000", "5.5", "3")
        self.assertEqual(amount, 10000.0)
        self.assertEqual(rate, 5.5)
        self.assertEqual(years, 3)
        
        # Invalid loan amount
        with self.assertRaises(ValueError):
            self.validator.validate_loan_inputs("0", "5.5", "3")
        
        # Invalid rate
        with self.assertRaises(ValueError):
            self.validator.validate_loan_inputs("10000", "-1", "3")
        
        # Invalid years
        with self.assertRaises(ValueError):
            self.validator.validate_loan_inputs("10000", "5.5", "0")
    
    def test_validate_savings_inputs(self):
        """Test savings input validation."""
        # Valid inputs
        target, contribution, rate = self.validator.validate_savings_inputs("5000", "200", "3")
        self.assertEqual(target, 5000.0)
        self.assertEqual(contribution, 200.0)
        self.assertEqual(rate, 3.0)
        
        # Invalid target amount
        with self.assertRaises(ValueError):
            self.validator.validate_savings_inputs("0", "200", "3")
        
        # Invalid monthly contribution
        with self.assertRaises(ValueError):
            self.validator.validate_savings_inputs("5000", "0", "3")
        
        # Invalid rate
        with self.assertRaises(ValueError):
            self.validator.validate_savings_inputs("5000", "200", "-1")


if __name__ == '__main__':
    # Run unit tests
    unittest.main(verbosity=2)
