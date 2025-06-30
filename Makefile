.PHONY: help install install-dev test lint format clean build upload upload-test docs

help:
	@echo "Available commands:"
	@echo "  install      Install the package"
	@echo "  install-dev  Install in development mode with dev dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build distribution packages"
	@echo "  upload-test  Upload to test.pypi.org"
	@echo "  upload       Upload to pypi.org"
	@echo "  docs         Generate documentation"

install:
	pip install .

install-dev:
	pip install -e .[dev]

test:
	pytest tests/ -v --cov=auto_prompt_generation --cov-report=term-missing

lint:
	flake8 auto_prompt_generation/ tests/ examples/
	mypy auto_prompt_generation/

format:
	black auto_prompt_generation/ tests/ examples/
	isort auto_prompt_generation/ tests/ examples/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

build: clean
	python -m build

upload-test: build
	python -m twine upload --repository testpypi dist/*

upload: build
	python -m twine upload dist/*

docs:
	@echo "Documentation is in README.md"
	@echo "Consider adding Sphinx documentation for more comprehensive docs"

# Git operations
git-setup:
	git init
	git add .
	git commit -m "Initial commit: Auto Prompt Generation package"

git-tag:
	git tag -a v0.1.0 -m "Version 0.1.0"
	git push origin v0.1.0
