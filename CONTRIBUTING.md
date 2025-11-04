
# Contributing to pillar_gguf_scanner

Thank you for your interest in contributing! We welcome bug reports, feature requests, and pull requests. Following the guidelines below will help ensure smooth review and integration.

## Table of Contents
- [How to Contribute](#how-to-contribute)  
- [Development Setup](#development-setup)  
- [Branching & Pull Request Workflow](#branching--pull-request-workflow)  
- [Testing & CI Requirements](#testing--ci-requirements)  
- [Coding Style & Best Practices](#coding-style--best-practices)  
- [Reporting Issues](#reporting-issues)  
- [Feature Requests](#feature-requests)  
- [Code of Conduct](#code-of-conduct)  

---

## How to Contribute

1. Fork the repository.  
2. Clone your fork locally and set the upstream remote:
   ```bash
   git clone https://github.com/your-username/pillar_gguf_scanner.git
   cd pillar_gguf_scanner
   git remote add upstream https://github.com/pillar-labs/pillar_gguf_scanner.git
````

3. Create a new feature or fix branch off `main`:

   ```bash
   git checkout -b feat/your-feature-name
   ```
4. Make your changes.
5. Ensure all tests pass and linting/static checks are clean.
6. Push your branch and open a Pull Request (PR) against the `main` branch of the upstream repository.
7. In your PR description, explain *what* you changed and *why*, referencing any related issue(s).
8. The maintainers will review and may request changes — please respond promptly.

---

## Branching & Pull Request Workflow

* The `main` branch is always considered the stable release line.
* New features and bug-fixes should be developed in a feature branch (e.g., `feat/add-xxx` or `fix/yyy`).
* Avoid making large sweeping changes in one PR; smaller, focused contributions are easier to review and merge.
* All PRs must pass Continuous Integration (CI) checks before merging.

---

## Development Setup

1. Ensure you have Python installed (the project uses the `uv` tool for environment management).
2. From your project root, install dependencies:

   ```bash
   uv sync --group test
   ```
3. You may run the tests locally:

   ```bash
   uv run pytest
   ```

   You can also run linting or typing checks:

   ```bash
   uv run ruff check .
   uv run ruff format --check .
   uv run mypy src
   ```

---

## Testing & CI Requirements

This project uses a CI workflow configured under `.github/workflows/ci.yml`. The following checks must pass on every PR:

* **Linting**: `uv run ruff check .`
* **Format checking**: `uv run ruff format --check .`
* **Type checking**: `uv run mypy src`
* **Unit tests with coverage**:

  ```bash
  uv run pytest \
    --cov=pillar_gguf_scanner \
    --cov-report=term-missing \
    --cov-report=xml
  ```
* **Coverage upload**: Ensures the coverage artifact `coverage.xml` is generated and uploaded by CI.

**Tip**: Before submitting a PR, run all of the above locally to ensure your contribution aligns with the CI pipeline.

---

## Coding Style & Best Practices

* Follow PEP 8 formatting and maintain clear, consistent style.
* Use type annotations throughout for maintainability and clarity.
* Write clear and concise docstrings for all new public functions and classes.
* When modifying heuristics or adding rules (e.g., a new `PatternRule`), include tests covering both positive and negative cases.
* Consider performance and memory usage — the library may process large model headers and should remain efficient.
* Maintain backward compatibility whenever possible. If a breaking change is required, document it clearly and update versioning accordingly.

---

## Reporting Issues

Found a bug or unexpected behaviour? Please open an issue and provide:

* A clear title and description of the problem.
* Steps to reproduce the behaviour (including inputs and outputs).
* Any stack trace, error messages, or logs.
* Version of the library (e.g., via `pip show pillar-gguf-scanner` or `git rev-parse HEAD`).
* If possible, a minimal code snippet or test case that reproduces the issue.

---

## Feature Requests

We welcome ideas for new features! When proposing a feature:

* Open an issue and label it “enhancement” or “feature request”.
* Explain the motivation: what problem it solves and why it's valuable.
* Describe a proposed API (if applicable) or how you envision using it.
* If you plan to implement it, mention that in the issue so contributors don’t duplicate work.

---

## Code of Conduct

This project adopts the [Contributor Covenant](https://www.contributor-covenant.org/) — we expect all participants in the community to uphold a welcoming, respectful, and inclusive environment.

---

Thank you for contributing and helping make **pillar_gguf_scanner** stronger and more robust!
