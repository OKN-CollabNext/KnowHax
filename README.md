# KnowHax CollabNext Challenge

## Prerequisites

### Python

This code base is compatible with python 3.11 and above. To install python on your system
a tool like [pyenv](https://github.com/pyenv/pyenv) is convenient. Once pyenv is installed
you can install the python version for this project by running:

```bash
pyenv install 3.11.4
```

### Node

This code base is compatible with node 18 and above. Please use [the following instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
to install node for your operating system if needed.

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

You need a `.env` file to store secrets as follows:

```
OPENALEX_EMAIL=mailto@example.com
```

The OPENALEX_EMAIL secret is used to [speed up calls](https://docs.openalex.org/how-to-use-the-api/api-overview) to the OpenAlex REST API.

## Running

This project uses [Observable Framework](https://observablehq.com/framework/). You can run the site locally in development mode as follows

```bash
invoke install
invoke dev
```

The homepage will be launched in your browser at http://127.0.0.1:3000

## Deploying

Deployments to this project on the Observable Cloud take place through the **Deploy** GitHub Action whenever new commits are added to the `main` branch or manually [through the GitHub UI](https://github.com/OKN-CollabNext/KnowHax/actions/workflows/deploy.yaml).

## Invoke Commands

You can run various other commands using `invoke` as follows.

Deploy the site to Observable Cloud.

```bash
invoke deploy
```

Build the static web site locally.

```bash
invoke build
```

Manually case a graph.json refresh. This is needed because currently
observable framework doesn't notice if a dependent python module
has been changed when developing. It only monitors changes to
the particular page that is being displayed.

```bash
invoke touch
```

Delete local git branches that have already been merged.

```bash
invoke clean-branches
```
