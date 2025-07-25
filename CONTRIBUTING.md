# Contributing to PyEgen

Thank you for your interest in contributing to PyEgen! This guide will help you get started.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/brycewang-stanford/pyegen.git
   cd pyegen
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=pyegen

# Run specific test file
python -m pytest tests/test_core.py
```

## Code Style

This project uses several tools to maintain code quality:

```bash
# Format code with black
black pyegen/ tests/

# Sort imports with isort
isort pyegen/ tests/

# Check code style with flake8
flake8 pyegen/ tests/

# Type checking with mypy
mypy pyegen/
```

## Adding New Functions

When adding new functions:

1. Add the function to `pyegen/core.py`
2. Include comprehensive docstrings with examples
3. Add the function to `pyegen/__init__.py`
4. Write tests in `tests/test_core.py`
5. Update the README.md with usage examples

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-function`)
3. Make your changes
4. Run tests and style checks
5. Commit your changes (`git commit -m 'Add new function'`)
6. Push to your fork (`git push origin feature/new-function`)
7. Open a Pull Request

## Questions?

Feel free to open an issue for any questions or suggestions!
