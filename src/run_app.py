#!/usr/bin/env python3
"""
Simple application runner for the Personal Finance Calculator.
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from finance_calculator.main import main

if __name__ == "__main__":
    main()
