
install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

build:
	uv build

package-install:
	uv tool install dist/*.whl

force_package:
	uv tool install --force dist/*.whl

lint:
	uv  run ruff check brain_games

