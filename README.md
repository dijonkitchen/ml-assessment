# Machine Learning Application Engineer Assessment

## Purpose

A successful ML app engineer will be able to contribute to our ML ambitions. This will involve developing and improving models, as well as building the infrastructure and tooling to deliver those models across our platform. This role is going to involve learning and growing. We're interested in evaluating any relevant skills to get a feel for how you might tackle some of our immediate challenges as well as how you might grow in the role.

## Instructions

There are three assessments included. The API and model assessments both directly relate to the kind of tools and work relevant to the position. The algorithm assessment is intended to test problem solving and understanding of the python language. You only need to pick two of these assessments to do. The intention is that this shouldn't take more than an hour or two to complete. Be prepared to discuss and extend your solutions.

## Setup and install

* Homebrew: https://brew.sh/
* pyenv: https://github.com/pyenv/pyenv#installation
* Poetry: https://python-poetry.org/docs/#installing-with-pipx

## Development

### Activate virtual environment:

```bash
poetry shell
```

### Exit virtual environment:

```bash
exit
```

### Install dependencies:

```bash
poetry install
```

To add new dependencies:
```bash
poetry add <dependency>
```

### Running

#### Algorithms

```
poetry run python algorithms/main.py
```
All tests passed in 0.9625127500039525 seconds!
