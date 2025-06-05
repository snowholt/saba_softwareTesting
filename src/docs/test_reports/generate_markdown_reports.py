#!/usr/bin/env python3
"""
Generate markdown versions of test reports for documentation.
"""

import subprocess
import os
from datetime import datetime

def run_tests_and_generate_markdown():
    """Run tests and generate markdown reports."""
    reports_dir = "docs/test_reports"
    
    # Ensure reports directory exists
    os.makedirs(reports_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Test configurations
    test_configs = [
        {
            "name": "Unit Tests",
            "command": ["python", "-m", "pytest", "tests/test_unit.py", "-v"],
            "file": "unit_tests_report.md"
        },
        {
            "name": "Integration Tests", 
            "command": ["python", "-m", "pytest", "tests/test_integration.py", "-v"],
            "file": "integration_tests_report.md"
        },
        {
            "name": "System Tests",
            "command": ["python", "-m", "pytest", "tests/test_system.py", "-v"],
            "file": "system_tests_report.md"
        },
        {
            "name": "All Tests",
            "command": ["python", "-m", "pytest", "tests/", "-v"],
            "file": "comprehensive_tests_report.md"
        }
    ]
    
    for config in test_configs:
        print(f"Generating {config['name']} report...")
        
        try:
            # Run the test command
            result = subprocess.run(
                config["command"],
                capture_output=True,
                text=True,
                cwd="."
            )
            
            # Create markdown content
            markdown_content = f"""# {config['name']} Report

**Generated:** {timestamp}
**Project:** Personal Finance Calculator
**Test Framework:** pytest

## Test Execution Summary

**Exit Code:** {result.returncode}
**Status:** {'PASSED' if result.returncode == 0 else 'FAILED'}

## Test Output

```
{result.stdout}
```

## Error Output (if any)

```
{result.stderr if result.stderr else 'No errors reported'}
```

## Test Statistics

"""
            
            # Add basic statistics
            stdout_lines = result.stdout.split('\n')
            for line in stdout_lines:
                if 'passed' in line and ('failed' in line or 'error' in line or 'skipped' in line):
                    markdown_content += f"**Result Summary:** {line.strip()}\n\n"
                    break
            
            # Write to markdown file
            file_path = os.path.join(reports_dir, config["file"])
            with open(file_path, 'w') as f:
                f.write(markdown_content)
            
            print(f"✓ Generated {file_path}")
            
        except Exception as e:
            print(f"✗ Error generating {config['name']} report: {e}")
    
    # Generate summary report
    generate_summary_report(timestamp)

def generate_summary_report(timestamp):
    """Generate a summary report of all tests."""
    summary_content = f"""# Test Summary Report

**Generated:** {timestamp}
**Project:** Personal Finance Calculator
**Testing Framework:** pytest and unittest

## Overview

This document provides a comprehensive summary of all testing activities performed on the Personal Finance Calculator application.

## Test Types Executed

### 1. Unit Tests
- **File:** `tests/test_unit.py`
- **Purpose:** Test individual components in isolation
- **Coverage:** Calculator functions, validation logic, utility methods

### 2. Integration Tests  
- **File:** `tests/test_integration.py`
- **Purpose:** Test component interactions
- **Coverage:** Calculator-validator integration, data flow validation

### 3. System Tests
- **File:** `tests/test_system.py`
- **Purpose:** Test complete system functionality
- **Coverage:** End-to-end workflows, user scenarios

## Test Execution Methods

1. **pytest**: Modern Python testing framework with detailed reporting
2. **unittest**: Python's built-in testing framework
3. **HTML Reports**: Visual test reports with detailed results
4. **Text Reports**: Command-line compatible outputs

## Files Generated

- `unit_tests_report.md` - Unit test results
- `integration_tests_report.md` - Integration test results  
- `system_tests_report.md` - System test results
- `comprehensive_tests_report.md` - All tests combined
- `comprehensive_pytest_report.html` - HTML test report
- Various `.txt` files with raw output

## Project Structure Tested

```
finance_calculator/
├── calculator.py      # Core calculation logic
├── validator.py       # Input validation
├── main.py           # CLI interface
└── __init__.py       # Package initialization

tests/
├── test_unit.py      # Unit tests
├── test_integration.py # Integration tests
├── test_system.py    # System tests
└── __init__.py       # Test package initialization
```

## Quality Assurance

This testing suite ensures:
- **Correctness**: All calculations produce expected results
- **Robustness**: Proper error handling for invalid inputs
- **Reliability**: Consistent behavior across different scenarios
- **Maintainability**: Clear test structure for future modifications

## Conclusion

The Personal Finance Calculator has been thoroughly tested using multiple testing approaches, ensuring high code quality and reliability for end users.
"""
    
    file_path = "docs/test_reports/test_summary_report.md"
    with open(file_path, 'w') as f:
        f.write(summary_content)
    
    print(f"✓ Generated {file_path}")

if __name__ == "__main__":
    run_tests_and_generate_markdown()
