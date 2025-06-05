#!/usr/bin/env python3
"""
Simple test runner script for the Personal Finance Calculator project.
"""

import sys
import os
import unittest

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_all_tests():
    """Run all tests and display results."""
    print("="*60)
    print("PERSONAL FINANCE CALCULATOR - TEST RUNNER")
    print("="*60)
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    return result.wasSuccessful()

def run_specific_tests(test_type):
    """Run specific type of tests."""
    print(f"Running {test_type} tests...")
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern=f'test_{test_type}.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
        if test_type in ['unit', 'integration', 'system']:
            run_specific_tests(test_type)
        else:
            print("Usage: python run_tests.py [unit|integration|system]")
    else:
        run_all_tests()
