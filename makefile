# Define your Python interpreter
PYTHON = python3

# Define the testing and linting tools
PYTEST = $(PYTHON) -m pytest
PYLINT = $(PYTHON) -m pylint

# Define your source files and test files
SRC_FILES = $(shell find ./task_manager -name "*.py" -not -path "./venv/*")
TEST_FILES = $(shell find ./tests -name "test_*.py")  # Update to target tests directory

# Default target
.PHONY: all
all: lint test

# Run pylint
.PHONY: lint
lint:
	@echo "Running pylint..."
	$(PYLINT) $(SRC_FILES)

# Run pytest
.PHONY: test
test:
	@echo "Running pytest..."
	$(PYTEST) $(TEST_FILES)

# Clean up (optional)
.PHONY: clean
clean:
	@echo "Cleaning up..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Help target
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  make lint      - Run pylint on source files"
	@echo "  make test      - Run pytest on test files in ./tests directory"
	@echo "  make clean     - Remove .pyc files and __pycache__ directories"
	@echo "  make all       - Run both lint and test"
	@echo "  make help      - Show this help message"
