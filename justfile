lint:
  uv run -m ruff format .
  uv run -m ruff check --fix --unsafe-fixes .
  uv run -m flake8

test *args:
  uv run -m pytest {{ args }}

typing:
  uv run -m mypy src

_pre-commit *args:
  uvx --with pre-commit-uv pre-commit {{ args }}

pre-commit *args:
  @just _pre-commit run --all-files

check-all: lint typing pre-commit
