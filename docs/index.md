# $$REPO$$

![CICD](https://github.com/$$OWNER$$/$$REPO$$/actions/workflows/cicd.yaml/badge.svg)

$$DESCRIPTION$$

# Template Repository Setup

Run `mise run setup-repo` to replace template variables and configure repository.

Then delete this section of the README and see Next Steps.

## Next Steps

- Add users to the [CODEOWNERS](./CODEOWNERS) file.
- [Choose a license](https://choosealicense.com/). If changing from the default (Apache 2.0), change the [LICENSE](./LICENSE) file in the repository root and update the [pyproject.toml](./pyproject.toml) file's `license` and `classifiers` fields.
- [Add a secret](https://github.com/$$OWNER$$/$$REPO$$/settings/secrets/actions/new) with name `PYPI_TOKEN` and value of [your Pypi token](https://pypi.org/help/#apitoken) to enable package publish to Pypi.
- Add pages to the documentation by adding Markdown files to [/docs](./docs) and updating the [mkdocs.yml](./mkdocs.yml) file's `nav` section. See the [Material for MkDocs guide](https://squidfunk.github.io/mkdocs-material/getting-started/).

Then delete this section of the README.

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
