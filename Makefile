# Makefile for PyEgen development

.PHONY: help install install-dev test lint format clean build upload upload-test

help:		## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:	## Install package
	pip install .

install-dev:	## Install package in development mode with dev dependencies
	pip install -e ".[dev]"

test:		## Run tests
	python -m pytest tests/ -v

test-cov:	## Run tests with coverage
	python -m pytest tests/ -v --cov=pyegen --cov-report=html --cov-report=term

lint:		## Run linting checks
	flake8 pyegen/ tests/
	mypy pyegen/

format:		## Format code
	black pyegen/ tests/ examples.py
	isort pyegen/ tests/ examples.py

clean:		## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build:		## Build package
	python -m build

upload-test:	## Upload to TestPyPI
	python -m twine upload --repository testpypi dist/*

upload:		## Upload to PyPI
	python -m twine upload dist/*

check:		## Run all checks (lint, test)
	make lint
	make test

all:		## Format, lint, test, and build
	make format
	make lint
	make test
	make build
