# Integration Tests Report

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
collecting ... collected 10 items

tests/test_integration.py::TestFinanceAppIntegration::test_interest_calculation_integration PASSED [ 10%]
tests/test_integration.py::TestFinanceAppIntegration::test_interest_calculation_validation_integration PASSED [ 20%]
tests/test_integration.py::TestFinanceAppIntegration::test_loan_payment_integration PASSED [ 30%]
tests/test_integration.py::TestFinanceAppIntegration::test_loan_payment_validation_integration PASSED [ 40%]
tests/test_integration.py::TestFinanceAppIntegration::test_savings_goal_integration PASSED [ 50%]
tests/test_integration.py::TestFinanceAppIntegration::test_savings_goal_validation_integration PASSED [ 60%]
tests/test_integration.py::TestComponentIntegration::test_calculator_validator_edge_cases PASSED [ 70%]
tests/test_integration.py::TestComponentIntegration::test_calculator_validator_workflow PASSED [ 80%]
tests/test_integration.py::TestComponentIntegration::test_data_type_consistency_integration PASSED [ 90%]
tests/test_integration.py::TestComponentIntegration::test_validation_error_handling_integration PASSED [100%]

============================== 10 passed in 0.02s ==============================

```

## Error Output (if any)

```
No errors reported
```

## Test Statistics

