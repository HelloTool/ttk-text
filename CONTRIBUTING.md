# Contributing

Before contributing, please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md), platform policies, and relevant laws and regulations.

## Submit Issues

WIP

## Pull Requests

1. Ensure there are no related PRs.
2. Fork this repository.
3. Clone the repository locally using [Git](https://git-scm.com/).
4. Familiarize yourself with the project development methods.
5. Create a branch, such as `feature/xxx` or `bugfix/xxx`.
6. Write and commit your code.
7. Submit a Pull Request to this repository.

## Development

This project is managed using PDM. For more information about PDM, please refer to the [PDM documentation][PDMDocs].

### Setting Up the Environment

Before writing code, you need to set up the development environment.

1. Install PDM.
2. Install dependencies by running `pdm install`.

### Running the Example

```bash
pdm run example
```

## Standards

### Code Standards

**Python (`.py`):**

- Function parameters must include type annotations.
- Maximum line length: 120 characters.
- All other cases should follow [PEP 8](https://peps.python.org/pep-0008/).

### Git Commit Standards

Follow [Conventional Commits][ConventionalCommits].

[ConventionalCommits]: https://www.conventionalcommits.org/
[PDMDocs]: https://pdm-project.org/zh-cn/latest/
