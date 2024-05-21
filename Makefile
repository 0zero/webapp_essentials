format:
	poetry run black bin src tests
	poetry run flake8 src tests
	poetry run isort .
	poetry run ruff check .

type-check:  
	poetry run mypy src

lint: format type-check
	@echo "All linters and formatters have been run successfully."

build:
	docker build -t webapp_essentials . -f Dockerfile