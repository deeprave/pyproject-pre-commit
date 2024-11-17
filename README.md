pyproject-pre-commit
--------------------

Ths is a pre-commit hook that checks the syntax of pyproject.toml and ensures that any dependencies
with an entry in \[tool.uv.sources\] does not point to any local path.

This hook was developed out of frustration due to committing local paths which broke checks in CI.

