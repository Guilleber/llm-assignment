> **Notes**
>
> Before following the installation procedure, rename the `project_name` and `root` folder names.
> Then, rename the `name` under `tool.poetry` in `pyproject.toml`.

# PROJECT NAME
...

## Install

### Project dependencies
This project uses [Poetry](https://python-poetry.org/docs/) to manage dependencies.

#### Install [Poetry](https://python-poetry.org/docs/#installation)

Launch the installation using the following command if [Poetry](https://python-poetry.org/docs/) is not currently installed.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Add Poetry to your $PATH
Add
```text
export PATH="$HOME/.local/bin:$PATH"
```
to your `.bashrc` or `.zshrc`

#### Install dependencies
```bash
poetry install
```

#### Install the pre-commit hooks
```bash
poetry run pre-commit install
```

## Usage
...
