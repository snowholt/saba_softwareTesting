"""
System Tests for Personal Finance Calculator

System testing focuses on testing the complete application from an end-user perspective.
These tests verify that the entire system works correctly as a whole, including
user workflows, error handling, and overall system behavior.
"""

import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from finance_calculator.main import FinanceApp, main


class TestFinanceAppSystem(unittest.TestCase):
    """System tests for the complete Finance Application."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = FinanceApp()
    
    def test_complete_loan_analysis_workflow(self):
        """Test complete loan analysis workflow from user perspective."""
        # Simulate user wanting to analyze a car loan
        loan_scenarios = [
            {"amount": "25000", "rate": "3.9", "years": "5"},    # Good credit
            {"amount": "25000", "rate": "7.2", "years": "5"},    # Average credit
            {"amount": "25000", "rate": "12.5", "years": "5"},   # Poor credit
        ]
        
        results = []
        for scenario in loan_scenarios:
            result = self.app.calculate_loan_payment(
                scenario["amount"], scenario["rate"], scenario["years"]
            )
            results.append(result)
        
        # Verify all calculations succeeded
        for result in results:
            self.assertTrue(result['success'], "Loan calculation should succeed")
            self.assertIn('monthly_payment', result)
            self.assertIn('total_payment', result)
            self.assertIn('total_interest', result)
        
        # Verify that higher interest rates result in higher payments
        self.assertLess(results[0]['monthly_payment'], results[1]['monthly_payment'])
        self.assertLess(results[1]['monthly_payment'], results[2]['monthly_payment'])
        
        # Verify that higher interest rates result in more total interest
        self.assertLess(results[0]['total_interest'], results[1]['total_interest'])
        self.assertLess(results[1]['total_interest'], results[2]['total_interest'])
    
    def test_complete_financial_planning_workflow(self):
        """Test complete financial planning workflow combining multiple calculations."""
        # User scenario: Someone planning to save for a house down payment
        # and comparing with taking a loan
        
        # Step 1: Calculate how long to save for down payment
        savings_result = self.app.calculate_savings_time("50000", "800", "2.5")
        self.assertTrue(savings_result['success'])
        
        # Step 2: Calculate mortgage payment for the house
        loan_result = self.app.calculate_loan_payment("200000", "4.5", "30")
        self.assertTrue(loan_result['success'])
        
        # Step 3: Calculate compound interest on current savings
        interest_result = self.app.calculate_interest("10000", "3.0", "5", compound=True, frequency=12)
        self.assertTrue(interest_result['success'])
        
        # Verify realistic financial planning results
        self.assertGreater(savings_result['years_to_goal'], 0)
        self.assertLess(savings_result['years_to_goal'], 15)  # Reasonable timeframe
        
        self.assertGreater(loan_result['monthly_payment'], 500)    # Reasonable mortgage payment
        self.assertLess(loan_result['monthly_payment'], 2000)     # Not unreasonably high
        
        self.assertGreater(interest_result['final_amount'], 10000)  # Should grow
        self.assertLess(interest_result['final_amount'], 15000)     # Reasonable growth
    
    def test_system_error_handling_and_recovery(self):
        """Test system-wide error handling and user experience."""
        # Test various error scenarios that a user might encounter
        
        # Scenario 1: User enters completely invalid data
        invalid_inputs = [
            {"amount": "abc", "rate": "5", "years": "3"},
            {"amount": "10000", "rate": "xyz", "years": "3"},
            {"amount": "10000", "rate": "5", "years": "abc"},
            {"amount": "", "rate": "5", "years": "3"},
            {"amount": None, "rate": "5", "years": "3"},
        ]
        
        for invalid_input in invalid_inputs:
            result = self.app.calculate_loan_payment(
                invalid_input["amount"], 
                invalid_input["rate"], 
                invalid_input["years"]
            )
            self.assertFalse(result['success'], f"Should fail for input: {invalid_input}")
            self.assertIn('error', result)
            self.assertIsInstance(result['error'], str)
            self.assertGreater(len(result['error']), 0)
        
        # Scenario 2: User enters unrealistic but valid data
        unrealistic_inputs = [
            {"amount": "-1000", "rate": "5", "years": "3"},    # Negative loan
            {"amount": "10000", "rate": "-5", "years": "3"},   # Negative interest
            {"amount": "10000", "rate": "5", "years": "0"},    # Zero years
        ]
        
        for unrealistic_input in unrealistic_inputs:
            result = self.app.calculate_loan_payment(
                unrealistic_input["amount"], 
                unrealistic_input["rate"], 
                unrealistic_input["years"]
            )
            self.assertFalse(result['success'])
            self.assertIn('error', result)
    
    def test_system_boundary_conditions(self):
        """Test system behavior at boundary conditions."""
        # Test minimum valid values
        min_result = self.app.calculate_loan_payment("1", "0", "1")
        self.assertTrue(min_result['success'])
        self.assertEqual(min_result['monthly_payment'], 1.0/12)  # $1 loan, 0% interest, 1 year
        
        # Test very large values (should still work)
        large_result = self.app.calculate_loan_payment("1000000", "15", "30")
        self.assertTrue(large_result['success'])
        self.assertGreater(large_result['monthly_payment'], 10000)  # Should be substantial
        
        # Test very small interest rates
        small_rate_result = self.app.calculate_loan_payment("10000", "0.01", "5")
        self.assertTrue(small_rate_result['success'])
        
        # Test savings with very small amounts
        small_savings_result = self.app.calculate_savings_time("100", "10", "1")
        self.assertTrue(small_savings_result['success'])
        self.assertLess(small_savings_result['years_to_goal'], 1)  # Should be less than a year
    
    def test_user_experience_consistency(self):
        """Test that the system provides consistent user experience."""
        # All successful operations should have consistent structure
        loan_result = self.app.calculate_loan_payment("15000", "4.5", "3")
        savings_result = self.app.calculate_savings_time("5000", "200", "3")
        interest_result = self.app.calculate_interest("1000", "4", "2")
        
        # All should have success field
        self.assertIn('success', loan_result)
        self.assertIn('success', savings_result)
        self.assertIn('success', interest_result)
        
        # All successful results should be True
        self.assertTrue(loan_result['success'])
        self.assertTrue(savings_result['success'])
        self.assertTrue(interest_result['success'])
        
        # All should have meaningful data
        self.assertGreater(len(loan_result), 1)      # More than just success
        self.assertGreater(len(savings_result), 1)   # More than just success
        self.assertGreater(len(interest_result), 1)  # More than just success
        
        # Test that error responses are also consistent
        error_result1 = self.app.calculate_loan_payment("-1000", "4.5", "3")
        error_result2 = self.app.calculate_savings_time("0", "200", "3")
        
        self.assertFalse(error_result1['success'])
        self.assertFalse(error_result2['success'])
        self.assertIn('error', error_result1)
        self.assertIn('error', error_result2)
    
    def test_main_application_execution(self):
        """Test the main application execution."""
        # Capture output from main function
        captured_output = StringIO()
        
        try:
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            
            # Verify that main function produces expected output
            self.assertIn("Personal Finance Calculator", output)
            self.assertIn("Loan Payment Calculation", output)
            self.assertIn("Savings Goal Calculation", output)
            self.assertIn("Interest Calculation", output)
            
            # Verify that calculations are shown
            self.assertIn("Monthly Payment", output)
            self.assertIn("Time to reach goal", output)
            self.assertIn("Final amount", output)
            
        except Exception as e:
            self.fail(f"Main application execution failed: {e}")
    
    def test_system_performance_basic(self):
        """Test basic system performance characteristics."""
        import time
        
        # Test that calculations complete in reasonable time
        start_time = time.time()
        
        # Perform multiple calculations
        for i in range(100):
            self.app.calculate_loan_payment("10000", "5", "3")
            self.app.calculate_savings_time("5000", "200", "3")
            self.app.calculate_interest("1000", "4", "2")
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Should complete 300 calculations in well under a second
        self.assertLess(execution_time, 1.0, "System performance is too slow")
    
    def test_system_data_integrity(self):
        """Test that the system maintains data integrity throughout operations."""
        # Test that repeated calculations with same inputs give same results
        inputs = ("12000", "4.2", "4")
        
        result1 = self.app.calculate_loan_payment(*inputs)
        result2 = self.app.calculate_loan_payment(*inputs)
        result3 = self.app.calculate_loan_payment(*inputs)
        
        # All results should be identical
        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)
        
        # Test that calculations are mathematically consistent
        loan_result = self.app.calculate_loan_payment("10000", "6", "5")
        
        if loan_result['success']:
            # Total payment should equal monthly payment * number of months
            expected_total = loan_result['monthly_payment'] * 5 * 12
            self.assertAlmostEqual(loan_result['total_payment'], expected_total, places=2)
            
            # Total interest should equal total payment minus principal
            expected_interest = loan_result['total_payment'] - 10000
            self.assertAlmostEqual(loan_result['total_interest'], expected_interest, places=2)


if __name__ == '__main__':
    # Run system tests
    unittest.main(verbosity=2)
