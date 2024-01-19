
# Lllm assignment

This project is used to evaluate candidates for d.s roles specialized in Generative AI.  

In that ocr use case, we are asked by a car rental company to read handwritten and typed car-rental form and convert
the result in a json format, so it can be exported to a third-party system.

Data and labels provided by the client can be read under the data directory, in the ocr_dataset_original_size
and the ocr_dataset_labels directories respectively.

The client wants accurate results, even if he is aware that 100% accuracy is not necessarily feasible.

Please, design one or many models to perform the task asked by the client.  Relative quality of the models must obviously
be evaluated in some way, but the exact way of doing it is given to the candidate

Important detail, the client want
to use Open AI models.  In the main file, you will find an example how the Open-AI Vision api 
can be used to read images and you are going to receive by mail and api key, that you can copy
under a .env, directly under the root directory, so you will be able to run your tests, without having
to pay the bill.


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
