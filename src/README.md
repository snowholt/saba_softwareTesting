# Personal Finance Calculator - Software Testing Project

A simple Python project demonstrating **Unit Testing**, **Integration Testing**, and **System Testing** methodologies.

## 📋 Project Overview

This project implements a basic Personal Finance Calculator with comprehensive testing to demonstrate different levels of software testing. The calculator performs common financial calculations such as loan payments, compound interest, and savings goals.

## 🏗️ Project Structure

```
src/
├── finance_calculator/
│   ├── __init__.py          # Package initialization
│   ├── calculator.py        # Core calculation functions
│   ├── validator.py         # Input validation logic
│   └── main.py             # Main application interface
├── tests/
│   ├── __init__.py         # Test package initialization
│   ├── test_unit.py        # Unit tests
│   ├── test_integration.py # Integration tests
│   └── test_system.py      # System tests
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## 🔧 Features

### Core Functionality
- **Simple Interest Calculation**: Calculate simple interest on investments
- **Compound Interest Calculation**: Calculate compound interest with different frequencies
- **Loan Payment Calculator**: Calculate monthly payments for loans
- **Savings Goal Calculator**: Determine time needed to reach savings targets
- **Input Validation**: Comprehensive validation of user inputs

## 🧪 Testing Methodology

### 1. Unit Testing (`test_unit.py`)
**Purpose**: Test individual functions and methods in isolation.

**Tests Include**:
- ✅ Individual calculation functions (simple interest, compound interest, loan payments)
- ✅ Input validation methods
- ✅ Edge cases and boundary conditions
- ✅ Error handling for invalid inputs
- ✅ Mathematical accuracy verification

**Example**:
```python
def test_simple_interest_calculation(self):
    result = self.calculator.calculate_simple_interest(1000, 5, 2)
    self.assertEqual(result, 100.0)  # (1000 * 5 * 2) / 100 = 100
```

### 2. Integration Testing (`test_integration.py`)
**Purpose**: Test how different components work together.

**Tests Include**:
- ✅ Calculator + Validator integration
- ✅ Main App coordination of components
- ✅ Data flow between modules
- ✅ Component interaction workflows
- ✅ End-to-end calculation processes

**Example**:
```python
def test_loan_payment_integration(self):
    # Tests validator → calculator → result formatting workflow
    result = self.app.calculate_loan_payment("15000", "4.5", "4")
    self.assertTrue(result['success'])
    self.assertIn('monthly_payment', result)
```

### 3. System Testing (`test_system.py`)
**Purpose**: Test the complete application from end-user perspective.

**Tests Include**:
- ✅ Complete user workflows
- ✅ System behavior under various conditions
- ✅ Error handling and recovery
- ✅ Performance characteristics
- ✅ Data integrity across operations
- ✅ User experience consistency

**Example**:
```python
def test_complete_financial_planning_workflow(self):
    # Tests realistic user scenario combining multiple features
    savings_result = self.app.calculate_savings_time("50000", "800", "2.5")
    loan_result = self.app.calculate_loan_payment("200000", "4.5", "30")
    # Verify realistic financial planning results
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
2. **Navigate to the project directory**:
   ```bash
   cd saba_softwareTesting/src
   ```

3. **Install dependencies** (optional, for enhanced testing):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**Method 1: Using the runner script (Recommended)**
```bash
# Simple runner script that handles paths automatically
python run_app.py
```

**Method 2: Direct execution with PYTHONPATH**
```bash
# Set Python path and run directly
PYTHONPATH=. python finance_calculator/main.py
```

**Method 3: Using module execution**
```bash
# Run as module (may require package installation)
python -m finance_calculator.main
```

**Expected Output**:
```
=== Personal Finance Calculator ===
Simple demonstration of financial calculations

1. Loan Payment Calculation:
Monthly Payment: $306.66
Total Interest: $1,039.76

2. Savings Goal Calculation:
Time to reach goal: 2.1 years
Total contributions: $5,040.00

3. Interest Calculation:
Final amount: $1,083.14
Interest earned: $83.14
```

## 🧪 Running Tests

### Run All Tests

**Method 1: Using the test runner script (Recommended)**
```bash
# Simple test runner that handles paths automatically
python run_tests.py
```

**Method 2: Using unittest with PYTHONPATH**
```bash
# Set Python path and run with unittest
PYTHONPATH=. python -m unittest discover tests -v
```

**Method 3: Using pytest (if installed)**
```bash
# Using pytest with proper path
PYTHONPATH=. pytest tests/ -v
```

### Run Specific Test Types

**Using the test runner:**
```bash
python run_tests.py unit         # Unit tests only
python run_tests.py integration  # Integration tests only
python run_tests.py system       # System tests only
```

**Using unittest directly:**

**Using unittest directly:**
```bash
PYTHONPATH=. python -m unittest tests.test_unit -v
PYTHONPATH=. python -m unittest tests.test_integration -v
PYTHONPATH=. python -m unittest tests.test_system -v
```

### Test Coverage Analysis
```bash
# Generate coverage report (if coverage package is installed)
coverage run -m pytest tests/
coverage report
coverage html  # Generates HTML report
```

## 📊 Test Results Summary

### Expected Test Counts:
- **Unit Tests**: ~20 test methods
- **Integration Tests**: ~8 test methods  
- **System Tests**: ~8 test methods
- **Total Tests**: ~36 test methods

### Test Coverage Areas:
- ✅ Mathematical calculations
- ✅ Input validation
- ✅ Error handling
- ✅ Component integration
- ✅ User workflows
- ✅ Edge cases and boundaries
- ✅ Performance characteristics

## 📈 Sample Test Output

```
test_calculate_compound_interest (test_unit.TestFinanceCalculator) ... ok
test_calculate_monthly_payment (test_unit.TestFinanceCalculator) ... ok
test_loan_payment_integration (test_integration.TestFinanceAppIntegration) ... ok
test_complete_loan_analysis_workflow (test_system.TestFinanceAppSystem) ... ok

----------------------------------------------------------------------
Ran 36 tests in 0.123s

OK
```

## 🎯 Learning Objectives Demonstrated

1. **Unit Testing**: Testing individual components in isolation
2. **Integration Testing**: Testing component interactions and data flow
3. **System Testing**: Testing complete user scenarios and system behavior
4. **Test Organization**: Proper test structure and documentation
5. **Error Handling**: Comprehensive validation and error management
6. **Code Coverage**: Ensuring adequate test coverage across the codebase

## 📝 Key Testing Concepts Illustrated

### Test Isolation
- Each test is independent and can run in any order
- Test fixtures (`setUp()`) ensure consistent test environment

### Test Categories
- **Positive Testing**: Testing with valid inputs
- **Negative Testing**: Testing with invalid inputs
- **Boundary Testing**: Testing edge cases and limits
- **Performance Testing**: Basic performance characteristics

### Assertion Types
- **Equality**: `assertEqual()`, `assertAlmostEqual()`
- **Boolean**: `assertTrue()`, `assertFalse()`
- **Exceptions**: `assertRaises()`
- **Comparisons**: `assertGreater()`, `assertLess()`

## 🔍 Code Quality Features

- **Type Hints**: Clear function signatures (could be added for enhancement)
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Proper exception handling with meaningful messages
- **Validation**: Input validation before processing
- **Separation of Concerns**: Clear separation between calculation, validation, and interface

## 📚 Further Enhancements

This basic project can be extended with:
- **Mock Testing**: Using `unittest.mock` for external dependencies
- **Parameterized Tests**: Testing multiple inputs with single test methods
- **Test Data Management**: External test data files
- **Continuous Integration**: Automated testing on code changes
- **Performance Benchmarking**: Detailed performance testing
- **GUI Testing**: If a graphical interface is added

## 👨‍🎓 Assignment Completion

This project demonstrates:
- ✅ **Simple Python Project** (achievable in 1 hour)
- ✅ **Unit Testing** implementation and examples
- ✅ **Integration Testing** implementation and examples  
- ✅ **System Testing** implementation and examples
- ✅ **Documentation** with clear explanations
- ✅ **Structured Code** with proper organization
- ✅ **Real-world Application** (financial calculations)

Perfect for demonstrating software testing concepts in an academic setting!

---

**Author**: Student  
**Course**: Software Testing  
**Date**: June 2025
