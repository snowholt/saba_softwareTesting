# Unit Tests Report
Generated on: 2025-06-05 10:42:06

## Summary
============================================================
UNIT TEST SUMMARY
============================================================
Tests run: 13
Failures: 0
Errors: 0
Success rate: 100.0%


## Detailed Output
```
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
Ran 13 tests in 0.001s

OK

```

## Unit Test Coverage
Unit tests validate individual functions in isolation:
- Calculator functions (simple interest, compound interest, loan payment)
- Validator functions (input validation, error handling)
- Edge cases and boundary conditions
