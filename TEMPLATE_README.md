# $$REPO$$

![CICD](https://github.com/$$OWNER$$/$$REPO$$/actions/workflows/cicd.yaml/badge.svg)

$$DESCRIPTION$$

## Getting Started

📖 Read [the documentation](https://$$OWNER$$.github.io/$$REPO$$/)!

## Usage

```python
"Module main."
import asyncio
import logging


async def main() -> int:
    "Main function."
    logger = logging.getLogger(__name__)
    logger.info("Hello world from $$REPO$$.")
    return 0


if __name__ == "__main__":
    asyncio.run(main())
```

## Local Developer Setup

Requirements:

- [mise](https://mise.jdx.dev/)
- [python](https://www.python.org/) $$PYTHON_VERSION$$ or greater
- [poetry](https://python-poetry.org/)

[Install mise](https://mise.jdx.dev/getting-started.html) then run `mise run init` to setup python, poetry, and install dependencies.

### Repository Mangement

This repository uses [mise](https://mise.jdx.dev/) for tool and task management.

List all available commands with `mise tasks`.

Run all pull request checks locally with `mise run pr`

### Package Management

This repository uses [poetry](https://python-poetry.org/) for python package management.

- `poetry install --sync` install/update dependencies.
- `poetry add` add a dependency ie. `poetry add black`.
- `poetry add -D` add a development dependency ie. `poetry add -D black`.
- `poetry remove` remove a dependency ie. `poetry remove black`.
- `poetry shell` activate the python virtual environment for access to installed packages.
- `exit` exit the python virtual environment.
