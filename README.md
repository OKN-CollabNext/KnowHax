# KnowHax CollabNext Challenge

## Prerequisites

### Python

This code base is compatible with python 3.11 and above. To install python on your system
a tool like [pyenv](https://github.com/pyenv/pyenv) is convenient. Once pyenv is installed
you can install the python version for this project by running:

```bash
pyenv install 3.11.4
```

### Git

Please [follow the instructions on GitHub](https://github.com/git-guides/install-git) to install git on your system.

### Poetry

Please [follow the instractions on the Poetry website](https://python-poetry.org/docs/#installation) to install poetry on your system.

## Getting Started

After cloning this repo for the first time you need to create a virtual environment:

```bash
python -m venv .venv
```

And activate it or choose it as the python environment for the project in your IDE.

```bash
source .venv/bin/activate
```

You can then install project dependencies as follows:

```bash
poetry install
```

## Running

This project uses [Taipy](https://www.taipy.io/). You can run the site locally as follows

```bash
invoke run
```

The homepage will be launched in your browser at http://127.0.0.1:5000
