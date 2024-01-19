
# Lllm assignment


This project aims to assess candidates for data science roles with a focus on Generative AI. 
We have devised a hypothetical Optical Character Recognition (OCR) scenario for this purpose. 
A car rental company has tasked us with processing both handwritten and typed car-rental forms, 
converting the data into JSON format for integration into a third-party system.

You'll find the data and labels provided by our fictional client in the 'data' directory, 
specifically in the 'ocr_dataset_original_size' and 'ocr_dataset_labels' folders.

The client expects precise results, understanding that achieving 100% accuracy may not be possible.

Your task is to develop one or more models capable of fulfilling the client's requirements. 
You'll need to evaluate the relative effectiveness of these models. The methodology for this evaluation is up to you.

A crucial requirement from the client is the use of OpenAI models. In the main file, 
there's an example of how the OpenAI Vision API can be employed for image recognition. 
You will also receive an API key via email, which should be placed in a .env file in the root directory.
This setup allows you to conduct your tests without incurring any costs.


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
