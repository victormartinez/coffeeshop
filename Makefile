PROJECT_NAME = coffeeshop
TEST_FOLDER = tests

.PHONY:default
default: help

.PHONY: help
help:
	@echo "All Commands:"
	@echo "	Code Style:"
	@echo "		check - Check format style."
	@echo "		format - Format code style."
	@echo "		typecheck - Check types in code"
	@echo "	Env:"
	@echo "		clean - Remove temp files."
	@echo "		run-server - Run server responsible for handling guest requests."
	@echo "		run-client FILEPATH="filepath - Parse filepath and send content to server."
	@echo "		test - Run tests."
	@echo "		coverage - Run tests and gather coverage data."


.PHONY: format
format:
	@echo ""
	@echo "FORMATTING CODE:"
	@echo ""
	black -l 88 -t py310 --skip-string-normalization --preview $(PROJECT_NAME) $(TEST_FOLDER)
	unify --in-place --recursive --quote '"' $(PROJECT_NAME) $(TEST_FOLDER)
	isort --profile black .

	@echo ""
	@echo "CHECKING CODE STILL NEEDS FORMATTING:"
	@echo ""
	black -l 88 -t py310 --skip-string-normalization --preview --check $(PROJECT_NAME) $(TEST_FOLDER)

	@echo ""
	@echo "CHECKING TYPING"
	@echo ""
	@make typecheck

	@echo ""
	@echo "CHECKING CODE STYLE"
	@echo ""
	flake8 $(PROJECT_NAME) $(TEST_FOLDER)

	@echo ""
	@echo "ENSURE DOUBLE QUOTES"
	@echo ""
	unify --check-only --recursive --quote '"' $(PROJECT_NAME) $(TEST_FOLDER)

	@echo ""
	@echo "SORT IMPORTS"
	@echo ""
	isort --profile black -c .

	@echo ""
	@echo "CHECKING SECURITY ISSUES"
	@echo ""
	bandit -r $(PROJECT_NAME)

.PHONY: typecheck
typecheck:
	mypy --python-version 3.10 --ignore-missing-imports --disallow-untyped-defs --disallow-untyped-calls $(PROJECT_NAME)/

.PHONY: clean
clean:
	- @find . -name "*.pyc" -exec rm -rf {} \;
	- @find . -name "__pycache__" -delete
	- @find . -name "*.pytest_cache" -exec rm -rf {} \;
	- @find . -name "*.mypy_cache" -exec rm -rf {} \;

.PHONY: run-server
run-server:
	python -m coffeeshop.infrastructure.server

.PHONY: run-client
run-client:
	python -m coffeeshop.infrastructure.client $(FILEPATH)

.PHONY: test
test:
	pytest tests/unit/ -vv

.PHONY: coverage
coverage:
	coverage run -m pytest tests/unit/ -vv
	coverage report -m
