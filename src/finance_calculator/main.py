"""
Main application interface for the Personal Finance Calculator.
Provides a simple command-line interface for financial calculations.
"""

from finance_calculator.calculator import FinanceCalculator
from finance_calculator.validator import InputValidator


class FinanceApp:
    """Main application class that coordinates calculator and validator."""
    
    def __init__(self):
        self.calculator = FinanceCalculator()
        self.validator = InputValidator()
    
    def calculate_loan_payment(self, loan_amount, annual_rate, years):
        """
        Calculate monthly loan payment with input validation.
        
        Args:
            loan_amount: Loan amount (will be validated)
            annual_rate: Annual interest rate (will be validated)
            years: Loan term in years (will be validated)
            
        Returns:
            dict: Result containing monthly payment or error information
        """
        try:
            # Validate inputs
            validated_amount, validated_rate, validated_years = \
                self.validator.validate_loan_inputs(loan_amount, annual_rate, years)
            
            # Calculate payment
            monthly_payment = self.calculator.calculate_monthly_payment(
                validated_amount, validated_rate, validated_years
            )
            
            return {
                'success': True,
                'monthly_payment': monthly_payment,
                'total_payment': monthly_payment * validated_years * 12,
                'total_interest': (monthly_payment * validated_years * 12) - validated_amount
            }
            
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def calculate_savings_time(self, target_amount, monthly_contribution, annual_rate):
        """
        Calculate time to reach savings goal with input validation.
        
        Args:
            target_amount: Target savings amount (will be validated)
            monthly_contribution: Monthly savings contribution (will be validated)
            annual_rate: Annual interest rate (will be validated)
            
        Returns:
            dict: Result containing time to goal or error information
        """
        try:
            # Validate inputs
            validated_target, validated_contribution, validated_rate = \
                self.validator.validate_savings_inputs(target_amount, monthly_contribution, annual_rate)
            
            # Calculate time to goal
            years_to_goal = self.calculator.calculate_savings_goal(
                validated_target, validated_contribution, validated_rate
            )
            
            return {
                'success': True,
                'years_to_goal': years_to_goal,
                'months_to_goal': years_to_goal * 12,
                'total_contributions': validated_contribution * years_to_goal * 12
            }
            
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def calculate_interest(self, principal, rate, time, compound=False, frequency=1):
        """
        Calculate simple or compound interest with input validation.
        
        Args:
            principal: Principal amount (will be validated)
            rate: Interest rate (will be validated)
            time: Time period (will be validated)
            compound: Whether to calculate compound interest
            frequency: Compounding frequency (for compound interest)
            
        Returns:
            dict: Result containing interest calculation or error information
        """
        try:
            # Validate inputs
            validated_principal = self.validator.validate_positive_number(principal, "Principal")
            validated_rate = self.validator.validate_non_negative_number(rate, "Interest rate")
            validated_time = self.validator.validate_positive_number(time, "Time period")
            
            if compound:
                validated_frequency = self.validator.validate_integer(frequency, "Compound frequency")
                final_amount = self.calculator.calculate_compound_interest(
                    validated_principal, validated_rate, validated_time, validated_frequency
                )
                interest_earned = final_amount - validated_principal
                
                return {
                    'success': True,
                    'type': 'compound',
                    'final_amount': final_amount,
                    'interest_earned': round(interest_earned, 2)
                }
            else:
                interest_earned = self.calculator.calculate_simple_interest(
                    validated_principal, validated_rate, validated_time
                )
                
                return {
                    'success': True,
                    'type': 'simple',
                    'interest_earned': interest_earned,
                    'final_amount': validated_principal + interest_earned
                }
                
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }


def main():
    """Simple command-line interface for demonstration purposes."""
    app = FinanceApp()
    
    print("=== Personal Finance Calculator ===")
    print("Simple demonstration of financial calculations")
    
    # Example calculations
    print("\n1. Loan Payment Calculation:")
    loan_result = app.calculate_loan_payment(10000, 5.5, 3)
    if loan_result['success']:
        print(f"Monthly Payment: ${loan_result['monthly_payment']:.2f}")
        print(f"Total Interest: ${loan_result['total_interest']:.2f}")
    else:
        print(f"Error: {loan_result['error']}")
    
    print("\n2. Savings Goal Calculation:")
    savings_result = app.calculate_savings_time(5000, 200, 3.0)
    if savings_result['success']:
        print(f"Time to reach goal: {savings_result['years_to_goal']:.1f} years")
        print(f"Total contributions: ${savings_result['total_contributions']:.2f}")
    else:
        print(f"Error: {savings_result['error']}")
    
    print("\n3. Interest Calculation:")
    interest_result = app.calculate_interest(1000, 4.0, 2, compound=True, frequency=12)
    if interest_result['success']:
        print(f"Final amount: ${interest_result['final_amount']:.2f}")
        print(f"Interest earned: ${interest_result['interest_earned']:.2f}")
    else:
        print(f"Error: {interest_result['error']}")


if __name__ == "__main__":
    main()
