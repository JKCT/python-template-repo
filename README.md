# Python Template Repository

A fully-featured python3 repository template with easy setup.

GitHub template repositories currently don't have native support for template variables or repository configuration. But this template does both, with a single command.

Modern, logical setup for all the essentials. Formatting, linting, testing, release, documentation, CICD and more.

# Template Repository Setup

Install [mise](https://mise.jdx.dev/getting-started.html), then run `mise run setup-repo` to replace template variables and configure repository.

## Next Steps

Things we unfortunately cannot do for you:

- Add users to the `CODEOWNERS` file.
- [Choose a license](https://choosealicense.com/). If changing from the default (Apache 2.0), change the `LICENSE` file in the repository root and update the `pyproject.toml` file's `license` and `classifiers` fields.
- [Add a secret](https://github.com/$$OWNER$$/$$REPO$$/settings/secrets/actions/new) with name `PYPI_TOKEN` and value of [your Pypi token](https://pypi.org/help/#apitoken) to enable CICD package publish to Pypi.
- Add pages to the documentation by adding Markdown files to `/docs` and updating the `mkdocs.yml` file's `nav` section. See the [Material for MkDocs guide](https://squidfunk.github.io/mkdocs-material/getting-started/).

## Features

### GitHub Repository Configuration

- Sets description.
- Set homepage to documentation.
- Enables GitHub Issues:
  - Custom issue templates for `Bug`, `Docs`, and `Feature`.
- Pull Request:
  - Custom Pull Request template.
  - Require squash merge and set merge commit title as PR title and message as PR description.
  - Delete branch on merge.
- Sets `main` branch protection rules:
  - Require CICD status checks to pass.
  - Require 1 review from a Code Owner that did not commit the last push.
  - Require linear commit history.
  - Dismiss stale reviews.
  - Lock branch.
  - Enable fork syncing.
  - Enforce rules for admins.

### GitHub Pages Documentation with Material for MkDocs

- Automatic setup and deployment.
- Links to GitHub Repository.
- Linked in README.md and Pypi package page.

### GitHub Actions CICD

- Runs all checks on Pull Request.
- Enforces version update.
- Automatically creates GitHub release and publishes to Pypi on merge to `main` branch.
- Automatically builds and deploys documentation to GitHub pages on merge to `main` branch.
- Status badge in README.md.

### Checks

`mise run pr` will run all Pull Request checks locally (format, lint, test).

#### Formatting

`mise run format` will:

- Sync contents of the package `__main__.py` file to the `Usage` python code block.
- Sync `README.md` to `/docs/index.md`
- Format python package and test code with `black`.

#### Linting

`mise run lint` will:

- Check formatting of python package and test code with `black`.
- Check linting of python package and test code with `pylint`.
- Check typing of python package and test code with `mypy`.
- Check `poetry` lockfile is up to date.

#### Testing

`mise run test` will:

- Run all unit tests and check for code coverage.

## Goals

- All tasks can be run either locally or in CICD with no special setup.
- All tasks are idempotent.
- Tasks can be customized without altering GitHub Actions workflow file. The same workflow file can be used and synced across multiple repositories.
- Common setup and workflow across different languages (Python and TypeScript).
- Easy to onboard to. Only requirement to start is [mise](https://mise.jdx.dev/getting-started.html) with no additional special installs.

## Why Mise?

[Mise](https://mise.jdx.dev/) is a modern tool manager/task runner/environment manager solution that works across lanuages. It captures everything needed for each development environment without polluting the system installations/binaries.

### As a Tool Manager vs. pyenv/nvm

- Doesn't use shims, reducing shell latency over shim solutions like pyenv.
- Polyglot: Works across multiple lanuages, not specific to python/node.

### As a Task Manager vs. Makefile

- Supports single line tasks and native shell scripts without special syntax.
- Runs task dependencies in parallel.
- Easy to include task metadata like descriptions.
- Able to list all tasks with descriptions via `mise tasks`.
