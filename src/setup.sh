#!/bin/bash
# Setup script for Personal Finance Calculator Testing Project

echo "Setting up Personal Finance Calculator Testing Environment..."

# Set PYTHONPATH to include current directory
export PYTHONPATH="$PWD:$PYTHONPATH"

echo "PYTHONPATH set to: $PYTHONPATH"
echo ""
echo "Available commands:"
echo "1. Run application:        python run_app.py"
echo "2. Run all tests:          python run_tests.py"
echo "3. Run unit tests:         python run_tests.py unit"
echo "4. Run integration tests:  python run_tests.py integration" 
echo "5. Run system tests:       python run_tests.py system"
echo ""
echo "Alternative methods:"
echo "1. Run app directly:       PYTHONPATH=. python finance_calculator/main.py"
echo "2. Run tests directly:     PYTHONPATH=. python -m unittest discover tests -v"
echo ""
echo "Setup complete! You can now run the commands above."
