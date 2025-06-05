# All Tests Report
Generated on: 2025-06-05 10:33:17

## Test Execution Summary

**Test Statistics:**
- Tests run: 31
- Failures: 0
- Errors: 0
- Success rate: 100.0%

## Detailed Test Output
```
test_calculator_validator_edge_cases (test_integration.TestComponentIntegration.test_calculator_validator_edge_cases)
Test edge cases in calculator-validator integration. ... ok
test_calculator_validator_workflow (test_integration.TestComponentIntegration.test_calculator_validator_workflow)
Test typical workflow of validation followed by calculation. ... ok
test_data_type_consistency_integration (test_integration.TestComponentIntegration.test_data_type_consistency_integration)
Test that data types are consistent between validator and calculator. ... ok
test_validation_error_handling_integration (test_integration.TestComponentIntegration.test_validation_error_handling_integration)
Test that validation errors are properly handled before calculation. ... ok
test_interest_calculation_integration (test_integration.TestFinanceAppIntegration.test_interest_calculation_integration)
Test complete interest calculation workflow. ... ok
test_interest_calculation_validation_integration (test_integration.TestFinanceAppIntegration.test_interest_calculation_validation_integration)
Test interest calculation with invalid inputs. ... ok
test_loan_payment_integration (test_integration.TestFinanceAppIntegration.test_loan_payment_integration)
Test complete loan payment calculation workflow. ... ok
test_loan_payment_validation_integration (test_integration.TestFinanceAppIntegration.test_loan_payment_validation_integration)
Test loan payment calculation with invalid inputs. ... ok
test_savings_goal_integration (test_integration.TestFinanceAppIntegration.test_savings_goal_integration)
Test complete savings goal calculation workflow. ... ok
test_savings_goal_validation_integration (test_integration.TestFinanceAppIntegration.test_savings_goal_validation_integration)
Test savings goal calculation with invalid inputs. ... ok
test_complete_financial_planning_workflow (test_system.TestFinanceAppSystem.test_complete_financial_planning_workflow)
Test complete financial planning workflow combining multiple calculations. ... ok
test_complete_loan_analysis_workflow (test_system.TestFinanceAppSystem.test_complete_loan_analysis_workflow)
Test complete loan analysis workflow from user perspective. ... ok
test_main_application_execution (test_system.TestFinanceAppSystem.test_main_application_execution)
Test the main application execution. ... ok
test_system_boundary_conditions (test_system.TestFinanceAppSystem.test_system_boundary_conditions)
Test system behavior at boundary conditions. ... ok
test_system_data_integrity (test_system.TestFinanceAppSystem.test_system_data_integrity)
Test that the system maintains data integrity throughout operations. ... ok
test_system_error_handling_and_recovery (test_system.TestFinanceAppSystem.test_system_error_handling_and_recovery)
Test system-wide error handling and user experience. ... ok
test_system_performance_basic (test_system.TestFinanceAppSystem.test_system_performance_basic)
Test basic system performance characteristics. ... ok
test_user_experience_consistency (test_system.TestFinanceAppSystem.test_user_experience_consistency)
Test that the system provides consistent user experience. ... ok
test_compound_interest_calculation (test_unit.TestFinanceCalculator.test_compound_interest_calculation)
Test compound interest calculation with valid inputs. ... ok
test_compound_interest_invalid_inputs (test_unit.TestFinanceCalculator.test_compound_interest_invalid_inputs)
Test compound interest calculation with invalid inputs. ... ok
test_monthly_payment_calculation (test_unit.TestFinanceCalculator.test_monthly_payment_calculation)
Test monthly loan payment calculation. ... ok
test_monthly_payment_invalid_inputs (test_unit.TestFinanceCalculator.test_monthly_payment_invalid_inputs)
Test monthly payment calculation with invalid inputs. ... ok
test_savings_goal_calculation (test_unit.TestFinanceCalculator.test_savings_goal_calculation)
Test savings goal time calculation. ... ok
test_savings_goal_invalid_inputs (test_unit.TestFinanceCalculator.test_savings_goal_invalid_inputs)
Test savings goal calculation with invalid inputs. ... ok
test_simple_interest_calculation (test_unit.TestFinanceCalculator.test_simple_interest_calculation)
Test simple interest calculation with valid inputs. ... ok
test_simple_interest_negative_values (test_unit.TestFinanceCalculator.test_simple_interest_negative_values)
Test simple interest calculation with negative inputs. ... ok
test_validate_integer (test_unit.TestInputValidator.test_validate_integer)
Test integer validation. ... ok
test_validate_loan_inputs (test_unit.TestInputValidator.test_validate_loan_inputs)
Test loan input validation. ... ok
test_validate_non_negative_number (test_unit.TestInputValidator.test_validate_non_negative_number)
Test non-negative number validation. ... ok
test_validate_positive_number (test_unit.TestInputValidator.test_validate_positive_number)
Test positive number validation. ... ok
test_validate_savings_inputs (test_unit.TestInputValidator.test_validate_savings_inputs)
Test savings input validation. ... ok

----------------------------------------------------------------------
Ran 31 tests in 0.002s

OK

```

## Test Results Analysis
- **Total Tests Executed**: 31
- **Successful Tests**: 31
- **Failed Tests**: 0
- **Error Tests**: 0
- **Success Rate**: 100.0%

## Test Categories Covered
- Unit Tests: Individual function testing
- Integration Tests: Component interaction testing
- System Tests: End-to-end workflow testing

## Test Coverage Areas
- Mathematical calculations (simple interest, compound interest, loan payments)
- Input validation and sanitization
- Error handling and edge cases
- Component integration workflows
- System behavior and performance
- User experience consistency
