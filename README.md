# Pre-commit-hook
Hands-on examples for getting started with using Pre-commit Hooks.

## Pre-commit Hook Overview
Pre-commit hooks are automated scripts that run before you commit your changes in Git. They act as gatekeepers, ensuring your code adheres to certain standards before it becomes part of your project's history.

## Setup

1. Create a virtual and activate virtual environment:

    ```bash
        python3 -m venv venv
        source hook/bin/activate
    ```

2. Install the pre-commit hook:

    ```bash
        pip install -r requirements.txt
    ```

3. create a configuration file called `.pre-commit-config.yaml`

    ```bash
        pre-commit sample-config > .pre-commit-config.yaml
    ```

    Note: You can find more supported hooks here: https://pre-commit.com/hooks.html

4. Run against all the files

    ```bash
        pre-commit run --all-files
    ```

5. You can also include other tool that use `pyproject.toml` such as black, isort, pytest and pylint in your pre-commit checks

    ```bash

        - repo: https://github.com/pycqa/isort
            rev: 5.12.0
            hooks:
            - id: isort
                name: isort (python)

        - repo: https://github.com/psf/black-pre-commit-mirror
            rev: 24.4.2
            hooks:
            - id: black
                language_version: python3.11

        - repo: local
            hooks:
            - id: pylint
                name: pylint
                entry: pylint
                language: system
                types: [python]
                args:
                [
                    # "-rn", # Only display messages
                    # "-sn", # Don't display the score
                    "--recursive=y"
                ]

        - repo: local
            hooks:
            - id: pytest
            name: pytest
            entry: pytest test
            language: system
            types: [python]
            pass_filenames: false
            always_run: true
    ```

6. To automate pre-commit checks, you have to install the git hook scripts.

    ```bash
        pre-commit install
    ```

7. Now pre-commit checks is done after every commits
