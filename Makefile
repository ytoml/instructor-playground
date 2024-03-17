fmt:
	poetry run black .
	poetry run isort .
lint:
	poetry run flake8p .
	poetry run mypy .
proxy:
	poetry run litellm --port 8000 --model $$ANTHROPIC_MODEL

# allow no tests
.PHONY: test
test:
	sh -c 'PYTHONPATH=. poetry run pytest . || ([ $$? = 5 ] && exit 0 || exit $$?)'
