# Project Rules

## Python Environment and Package Management (`uv`)

Always use `uv` as the package manager and Python toolchain for this project.

- **Running Scripts**: Always execute scripts via `uv run` (e.g., `uv run python main.py <mode>`).
- **Dependencies**:
  - Add: `uv add <package>`
  - Remove: `uv remove <package>`
  - Sync: `uv sync`
  - Do not use raw `pip install` or modify environment packages outside `uv`.
- **Virtual Environment**: Use the environment managed by `uv` (`.venv`).
