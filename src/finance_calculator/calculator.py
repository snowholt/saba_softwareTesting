"""
Core calculation functions for the Personal Finance Calculator.
Contains simple financial calculation methods for testing demonstration.
"""

import math


class FinanceCalculator:
    """Main calculator class with basic financial operations."""
    
    def calculate_simple_interest(self, principal, rate, time):
        """
        Calculate simple interest.
        
        Args:
            principal (float): Principal amount
            rate (float): Interest rate (as percentage, e.g., 5 for 5%)
            time (float): Time period in years
            
        Returns:
            float: Simple interest amount
        """
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Values must be non-negative")
        
        return (principal * rate * time) / 100
    
    def calculate_compound_interest(self, principal, rate, time, compound_frequency=1):
        """
        Calculate compound interest.
        
        Args:
            principal (float): Principal amount
            rate (float): Annual interest rate (as percentage)
            time (float): Time period in years
            compound_frequency (int): How many times interest compounds per year
            
        Returns:
            float: Final amount after compound interest
        """
        if principal < 0 or rate < 0 or time < 0 or compound_frequency <= 0:
            raise ValueError("Invalid input values")
        
        rate_decimal = rate / 100
        amount = principal * (1 + rate_decimal / compound_frequency) ** (compound_frequency * time)
        return round(amount, 2)
    
    def calculate_monthly_payment(self, loan_amount, annual_rate, years):
        """
        Calculate monthly loan payment using the standard loan formula.
        
        Args:
            loan_amount (float): Total loan amount
            annual_rate (float): Annual interest rate (as percentage)
            years (int): Loan term in years
            
        Returns:
            float: Monthly payment amount
        """
        if loan_amount <= 0 or annual_rate < 0 or years <= 0:
            raise ValueError("Invalid loan parameters")
        
        if annual_rate == 0:
            return loan_amount / (years * 12)
        
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                         ((1 + monthly_rate) ** num_payments - 1)
        
        return round(monthly_payment, 2)
    
    def calculate_savings_goal(self, target_amount, monthly_contribution, annual_rate):
        """
        Calculate how long it takes to reach a savings goal.
        
        Args:
            target_amount (float): Target savings amount
            monthly_contribution (float): Monthly savings contribution
            annual_rate (float): Annual interest rate (as percentage)
            
        Returns:
            float: Time in years to reach the goal
        """
        if target_amount <= 0 or monthly_contribution <= 0 or annual_rate < 0:
            raise ValueError("Invalid savings parameters")
        
        if annual_rate == 0:
            return target_amount / (monthly_contribution * 12)
        
        monthly_rate = annual_rate / 100 / 12
        
        # Using the future value of annuity formula solved for time
        if monthly_rate > 0:
            months = math.log(1 + (target_amount * monthly_rate) / monthly_contribution) / \
                    math.log(1 + monthly_rate)
            return round(months / 12, 2)
        
        return target_amount / (monthly_contribution * 12)
