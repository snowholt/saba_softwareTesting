"""
Input validation module for the Personal Finance Calculator.
Handles user input validation and data sanitization.
"""


class InputValidator:
    """Validates user inputs for financial calculations."""
    
    @staticmethod
    def validate_positive_number(value, field_name="Value"):
        """
        Validate that a value is a positive number.
        
        Args:
            value: The value to validate
            field_name (str): Name of the field for error messages
            
        Returns:
            float: The validated number
            
        Raises:
            ValueError: If value is not a positive number
        """
        try:
            num_value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a valid number")
        
        if num_value <= 0:
            raise ValueError(f"{field_name} must be positive")
        
        return num_value
    
    @staticmethod
    def validate_non_negative_number(value, field_name="Value"):
        """
        Validate that a value is a non-negative number.
        
        Args:
            value: The value to validate
            field_name (str): Name of the field for error messages
            
        Returns:
            float: The validated number
            
        Raises:
            ValueError: If value is not a non-negative number
        """
        try:
            num_value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a valid number")
        
        if num_value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        
        return num_value
    
    @staticmethod
    def validate_integer(value, field_name="Value"):
        """
        Validate that a value is a positive integer.
        
        Args:
            value: The value to validate
            field_name (str): Name of the field for error messages
            
        Returns:
            int: The validated integer
            
        Raises:
            ValueError: If value is not a positive integer
        """
        try:
            int_value = int(value)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a valid integer")
        
        if int_value <= 0:
            raise ValueError(f"{field_name} must be positive")
        
        return int_value
    
    def validate_loan_inputs(self, loan_amount, annual_rate, years):
        """
        Validate loan calculation inputs.
        
        Args:
            loan_amount: Loan amount to validate
            annual_rate: Interest rate to validate
            years: Loan term to validate
            
        Returns:
            tuple: (validated_loan_amount, validated_rate, validated_years)
        """
        validated_amount = self.validate_positive_number(loan_amount, "Loan amount")
        validated_rate = self.validate_non_negative_number(annual_rate, "Interest rate")
        validated_years = self.validate_integer(years, "Loan term")
        
        return validated_amount, validated_rate, validated_years
    
    def validate_savings_inputs(self, target_amount, monthly_contribution, annual_rate):
        """
        Validate savings goal calculation inputs.
        
        Args:
            target_amount: Target savings amount to validate
            monthly_contribution: Monthly contribution to validate
            annual_rate: Interest rate to validate
            
        Returns:
            tuple: (validated_target, validated_contribution, validated_rate)
        """
        validated_target = self.validate_positive_number(target_amount, "Target amount")
        validated_contribution = self.validate_positive_number(monthly_contribution, "Monthly contribution")
        validated_rate = self.validate_non_negative_number(annual_rate, "Interest rate")
        
        return validated_target, validated_contribution, validated_rate
