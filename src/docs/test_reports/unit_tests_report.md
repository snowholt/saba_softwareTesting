# Unit Tests Report

**Generated:** 2025-06-05 10:16:26
**Project:** Personal Finance Calculator
**Test Framework:** pytest

## Test Execution Summary

**Exit Code:** 0
**Status:** PASSED

## Test Output

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.4.0, pluggy-1.6.0 -- /home/snowholt/coding/python/saba_softwareTesting/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.12.3', 'Platform': 'Linux-6.11.0-26-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '8.4.0', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'benchmark': '5.1.0', 'html': '4.1.1', 'cov': '6.1.1'}}
benchmark: 5.1.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/snowholt/coding/python/saba_softwareTesting/src
plugins: metadata-3.1.1, benchmark-5.1.0, html-4.1.1, cov-6.1.1
collecting ... collected 13 items

tests/test_unit.py::TestFinanceCalculator::test_compound_interest_calculation PASSED [  7%]
tests/test_unit.py::TestFinanceCalculator::test_compound_interest_invalid_inputs PASSED [ 15%]
tests/test_unit.py::TestFinanceCalculator::test_monthly_payment_calculation PASSED [ 23%]
tests/test_unit.py::TestFinanceCalculator::test_monthly_payment_invalid_inputs PASSED [ 30%]
tests/test_unit.py::TestFinanceCalculator::test_savings_goal_calculation PASSED [ 38%]
tests/test_unit.py::TestFinanceCalculator::test_savings_goal_invalid_inputs PASSED [ 46%]
tests/test_unit.py::TestFinanceCalculator::test_simple_interest_calculation PASSED [ 53%]
tests/test_unit.py::TestFinanceCalculator::test_simple_interest_negative_values PASSED [ 61%]
tests/test_unit.py::TestInputValidator::test_validate_integer PASSED     [ 69%]
tests/test_unit.py::TestInputValidator::test_validate_loan_inputs PASSED [ 76%]
tests/test_unit.py::TestInputValidator::test_validate_non_negative_number PASSED [ 84%]
tests/test_unit.py::TestInputValidator::test_validate_positive_number PASSED [ 92%]
tests/test_unit.py::TestInputValidator::test_validate_savings_inputs PASSED [100%]

============================== 13 passed in 0.02s ==============================

```

## Error Output (if any)

```
No errors reported
```

## Test Statistics

