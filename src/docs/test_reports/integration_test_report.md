# Integration Tests Report
Generated on: 2025-06-05 10:42:06

## Summary
============================================================
INTEGRATION TEST SUMMARY
============================================================
Tests run: 10
Failures: 0
Errors: 0
Success rate: 100.0%


## Detailed Output
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

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

```

## Integration Test Coverage
Integration tests validate component interactions:
- Calculator and validator integration
- Main application flow testing
- Component communication verification
