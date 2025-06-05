"""
Integration Tests for Personal Finance Calculator

Integration testing focuses on testing how different components work together.
These tests verify that calculator, validator, and main app components 
integrate correctly and data flows properly between them.
"""

import unittest
from finance_calculator.main import FinanceApp
from finance_calculator.calculator import FinanceCalculator
from finance_calculator.validator import InputValidator


class TestFinanceAppIntegration(unittest.TestCase):
    """Integration tests for FinanceApp class that combines calculator and validator."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = FinanceApp()
    
    def test_loan_payment_integration(self):
        """Test complete loan payment calculation workflow."""
        # Test successful calculation with valid inputs
        result = self.app.calculate_loan_payment("15000", "4.5", "4")
        
        self.assertTrue(result['success'])
        self.assertIn('monthly_payment', result)
        self.assertIn('total_payment', result)
        self.assertIn('total_interest', result)
        
        # Verify calculations are reasonable
        self.assertGreater(result['monthly_payment'], 0)
        self.assertGreater(result['total_payment'], 15000)  # Should be more than principal
        self.assertGreater(result['total_interest'], 0)    # Should have some interest
        
        # Verify total payment equals monthly payment * months
        expected_total = result['monthly_payment'] * 4 * 12
        self.assertAlmostEqual(result['total_payment'], expected_total, places=2)
        
        # Verify total interest calculation
        expected_interest = result['total_payment'] - 15000
        self.assertAlmostEqual(result['total_interest'], expected_interest, places=2)
    
    def test_loan_payment_validation_integration(self):
        """Test loan payment calculation with invalid inputs."""
        # Test with negative loan amount
        result = self.app.calculate_loan_payment("-5000", "4.5", "4")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        self.assertIn('positive', result['error'].lower())
        
        # Test with negative interest rate
        result = self.app.calculate_loan_payment("15000", "-1", "4")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with invalid years
        result = self.app.calculate_loan_payment("15000", "4.5", "0")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with non-numeric input
        result = self.app.calculate_loan_payment("abc", "4.5", "4")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
    
    def test_savings_goal_integration(self):
        """Test complete savings goal calculation workflow."""
        # Test successful calculation with valid inputs
        result = self.app.calculate_savings_time("8000", "300", "2.5")
        
        self.assertTrue(result['success'])
        self.assertIn('years_to_goal', result)
        self.assertIn('months_to_goal', result)
        self.assertIn('total_contributions', result)
        
        # Verify calculations are reasonable
        self.assertGreater(result['years_to_goal'], 0)
        self.assertGreater(result['months_to_goal'], 0)
        self.assertGreater(result['total_contributions'], 0)
        
        # Verify months = years * 12
        expected_months = result['years_to_goal'] * 12
        self.assertAlmostEqual(result['months_to_goal'], expected_months, places=1)
        
        # Verify total contributions calculation
        expected_contributions = 300 * result['years_to_goal'] * 12
        self.assertAlmostEqual(result['total_contributions'], expected_contributions, places=2)
    
    def test_savings_goal_validation_integration(self):
        """Test savings goal calculation with invalid inputs."""
        # Test with zero target amount
        result = self.app.calculate_savings_time("0", "300", "2.5")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with zero monthly contribution
        result = self.app.calculate_savings_time("8000", "0", "2.5")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with negative interest rate
        result = self.app.calculate_savings_time("8000", "300", "-1")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
    
    def test_interest_calculation_integration(self):
        """Test complete interest calculation workflow."""
        # Test simple interest calculation
        result = self.app.calculate_interest("2000", "3.5", "2", compound=False)
        
        self.assertTrue(result['success'])
        self.assertEqual(result['type'], 'simple')
        self.assertIn('interest_earned', result)
        self.assertIn('final_amount', result)
        
        # Verify simple interest calculation
        expected_interest = (2000 * 3.5 * 2) / 100
        self.assertEqual(result['interest_earned'], expected_interest)
        self.assertEqual(result['final_amount'], 2000 + expected_interest)
        
        # Test compound interest calculation
        result = self.app.calculate_interest("2000", "3.5", "2", compound=True, frequency=4)
        
        self.assertTrue(result['success'])
        self.assertEqual(result['type'], 'compound')
        self.assertIn('interest_earned', result)
        self.assertIn('final_amount', result)
        
        # Verify compound interest gives higher return than simple interest
        self.assertGreater(result['interest_earned'], expected_interest)
        self.assertGreater(result['final_amount'], 2000 + expected_interest)
    
    def test_interest_calculation_validation_integration(self):
        """Test interest calculation with invalid inputs."""
        # Test with negative principal
        result = self.app.calculate_interest("-1000", "3.5", "2")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with negative rate
        result = self.app.calculate_interest("2000", "-1", "2")
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        
        # Test with invalid compound frequency
        result = self.app.calculate_interest("2000", "3.5", "2", compound=True, frequency=0)
        self.assertFalse(result['success'])
        self.assertIn('error', result)


class TestComponentIntegration(unittest.TestCase):
    """Test integration between Calculator and Validator components."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = FinanceCalculator()
        self.validator = InputValidator()
    
    def test_calculator_validator_workflow(self):
        """Test typical workflow of validation followed by calculation."""
        # Test loan calculation workflow
        try:
            # Step 1: Validate inputs
            amount, rate, years = self.validator.validate_loan_inputs("12000", "5.0", "3")
            
            # Step 2: Perform calculation with validated inputs
            payment = self.calculator.calculate_monthly_payment(amount, rate, years)
            
            # Verify successful integration
            self.assertIsInstance(payment, float)
            self.assertGreater(payment, 0)
            
        except ValueError as e:
            self.fail(f"Integration workflow failed: {e}")
    
    def test_validation_error_handling_integration(self):
        """Test that validation errors are properly handled before calculation."""
        # Test that invalid inputs are caught by validator before reaching calculator
        with self.assertRaises(ValueError):
            # This should fail at validation step
            amount, rate, years = self.validator.validate_loan_inputs("-1000", "5.0", "3")
            # This line should not be reached
            self.calculator.calculate_monthly_payment(amount, rate, years)
    
    def test_calculator_validator_edge_cases(self):
        """Test edge cases in calculator-validator integration."""
        # Test zero interest rate integration
        try:
            amount, rate, years = self.validator.validate_loan_inputs("10000", "0", "2")
            payment = self.calculator.calculate_monthly_payment(amount, rate, years)
            
            # With 0% interest, payment should be principal / months
            expected = 10000 / (2 * 12)
            self.assertEqual(payment, expected)
            
        except ValueError as e:
            self.fail(f"Zero interest integration failed: {e}")
    
    def test_data_type_consistency_integration(self):
        """Test that data types are consistent between validator and calculator."""
        # Validate inputs (returns floats/ints)
        amount, rate, years = self.validator.validate_loan_inputs("15000.50", "4.25", "5")
        
        # Verify data types
        self.assertIsInstance(amount, float)
        self.assertIsInstance(rate, float)
        self.assertIsInstance(years, int)
        
        # Calculator should handle these types correctly
        payment = self.calculator.calculate_monthly_payment(amount, rate, years)
        self.assertIsInstance(payment, float)


if __name__ == '__main__':
    # Run integration tests
    unittest.main(verbosity=2)
