# Description (vf)

Ce projet vise à évaluer les candidats à des postes dans le domaine de la science des données en mettant l'accent sur l'
IA générative.
Pour ce faire, nous avons conçu un scénario hypothétique de reconnaissance optique de caractères (OCR).
Une société de location de voitures nous a demandé de traiter des formulaires de location de voitures,
manuscrits et dactylographiés, et de convertir les données au format JSON pour les intégrer dans un système tiers.
Vous trouverez les données et les étiquettes fournies par notre client fictif dans le répertoire "data",
plus précisément dans les dossiers "ocr_dataset_original_size" et "ocr_dataset_labels".
Le client attend des résultats précis, tout en sachant qu'il n'est pas possible d'atteindre une précision de 100 %.
Votre tâche consiste à développer un ou plusieurs modèles capables de répondre aux exigences du client.
Vous devrez évaluer l'efficacité relative de ces modèles. La méthodologie de cette évaluation vous appartient.
Une exigence cruciale du client est l'utilisation de modèles OpenAI. Le fichier principal contient un exemple
d'utilisation
de l'API OpenAI Vision pour la reconnaissance d'images. Vous recevrez également une clé API par courriel, qui doit être
placée dans un fichier .env dans le répertoire racine. Cette configuration vous permet d'effectuer vos tests sans
encourir de frais.
Pour la réalisation de ce projet, vous pouvez utiliser cette clé pour accéder à l’API de OpenAI.
La limite pour la clé est de 20$, alors vous devrez l’utiliser stratégiquement.

Note importante: comme vous êtes parmi les premier.e.s candidat.e.s à réaliser ce devoir, il se peut que vous trouviez
des problèmes ou des informations manquantes pour le réaliser. N’hésitez pas à nous écrire pour toutes questions.

# Description (ev)

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

Launch the installation using the following command if [Poetry](https://python-poetry.org/docs/) is not currently
installed.

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
