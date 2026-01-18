.PHONY: install lint test help

help:
	@echo "Available commands:"
	@echo "  make install - Install dependencies with uv"
	@echo "  make lint    - Run ruff check and format"
	@echo "  make test    - Run pytest with coverage"

install:
	@echo "📦 Installing dependencies..."
	@command -v uv >/dev/null 2>&1 || { \
		echo "⚠️  uv not found, installing..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	}
	@uv sync --extra dev

lint:
	@echo "🔍 Running ruff check..."
	@uv run ruff check --fix agentoak tests
	@echo "✨ Running ruff format..."
	@uv run ruff format agentoak tests

test:
	@echo "🧪 Running tests..."
	@uv run pytest --cov=agentoak -v
