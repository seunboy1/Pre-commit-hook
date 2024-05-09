# Pre-commit-hook
Hands-on examples for getting started with using Pre-commit Hooks.

## Pre-commit Hook Overview
Pre-commit hooks are automated scripts that run before you commit your changes in Git. They act as gatekeepers, ensuring your code adheres to certain standards before it becomes part of your project's history.

## Setup

1. Create a virtual environment:

    ```bash
        python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
        source hook/bin/activate
    ```

3. Install the pre-commit hook:

    ```bash
        pip install pre-commit
    ```

4. create a configuration file called `.pre-commit-config.yaml`

    ```bash
        pre-commit sample-config > .pre-commit-config.yaml
    ```

    Note: You can find more supported hooks here: https://pre-commit.com/hooks.html

5. Run against all the files

    ```bash
        pre-commit run --all-files
    ```

6. You can also include other tool such as black, iort in your pre-commit checks

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
    ```
   
7. To automate pre-commit checks, you have to install the git hook scripts.

    ```bash
        pre-commit install
    ```

8. Now pre-commit checks is done after every commits
