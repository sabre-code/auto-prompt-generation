# Project Structure

This document describes the structure of the auto-prompt-generation package.

```
auto-prompt-generation/
├── auto_prompt_generation/          # Main package directory
│   ├── __init__.py                 # Package initialization and exports
│   ├── core.py                     # Core functionality (moved from original file)
│   └── cli.py                      # Command line interface
├── tests/                          # Test directory
│   ├── __init__.py                 # Test package init
│   ├── conftest.py                 # Test configuration and fixtures
│   ├── test_core.py                # Tests for core functionality
│   └── test_cli.py                 # Tests for CLI
├── examples/                       # Example scripts
│   ├── simple_example.py           # Basic usage example
│   └── basic_usage.py              # Comprehensive examples
├── docs/                           # Documentation directory
├── .github/                        # GitHub specific files
│   └── workflows/
│       └── ci.yml                  # CI/CD pipeline
├── README.md                       # Main documentation
├── LICENSE                         # MIT License
├── setup.py                        # Setup script (for backward compatibility)
├── pyproject.toml                  # Modern Python packaging configuration
├── requirements.txt                # Production dependencies
├── requirements-dev.txt            # Development dependencies
├── MANIFEST.in                     # Package manifest
├── Makefile                        # Development commands
├── .gitignore                      # Git ignore rules
└── auto_prompt_generation_original.py  # Original file (backup)
```

## Key Files

### Package Files
- `auto_prompt_generation/__init__.py`: Main package entry point
- `auto_prompt_generation/core.py`: Core classes and functionality
- `auto_prompt_generation/cli.py`: Command line interface

### Configuration Files
- `pyproject.toml`: Modern Python packaging standard
- `setup.py`: Traditional setup script for compatibility
- `requirements.txt`: Runtime dependencies
- `requirements-dev.txt`: Development dependencies

### Documentation
- `README.md`: Comprehensive documentation with examples
- `LICENSE`: MIT license
- `docs/`: Additional documentation (expandable)

### Development Tools
- `Makefile`: Common development commands
- `.github/workflows/ci.yml`: GitHub Actions CI/CD
- `tests/`: Test suite with pytest
- `.gitignore`: Git exclusion rules

## Installation Commands

```bash
# Install from local directory
pip install -e .

# Install from git repository
pip install git+https://github.com/sabre-code/auto-prompt-generation.git

# Install with development dependencies
pip install -e .[dev]
```

## Development Commands

```bash
# Run tests
make test

# Format code
make format

# Lint code
make lint

# Build package
make build

# Clean build artifacts
make clean
```
