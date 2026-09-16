# Use `uv` for Python Management

Always use `uv` as the package manager and Python toolchain for this project.

## Guidelines
- **Running Python Scripts**: Always use `uv run` to execute scripts (e.g., `uv run python main.py <mode>`), never run `python` directly without `uv run`.
- **Dependency Management**:
  - Add packages: `uv add <package>`
  - Remove packages: `uv remove <package>`
  - Sync/install dependencies: `uv sync`
  - Never use `pip install` or `pip uninstall` directly.
- **Virtual Environment**: Rely on `uv` to manage the environment (`.venv`). Do not use `pipenv`, `poetry`, `conda`, or raw `venv`.
- **Python Version**: Follow the project's configured Python version (`.python-version` and `pyproject.toml`).
