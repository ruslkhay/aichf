# Overview 

**aichf** (AI Crypto Hedge Fund) is a project devoted to implementation 
for an AI agent-based automated cryptocurrency trading and risk 
management system.

The goal of this project is to create platform, that 
works with cryptocurrency and uses AI driven
approach for management.

## Installation

Choose folder on your computer, where you want to have this repository. 
The use next command to clone it:

```
git clone https://github.com/ruslkhay/aichf.git
```

Install PDM package manager and run:

```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
pdm install
```

In order to run formatting and linting manually use one of the following commands:

```bash
pre-commit run --files file.py
pre-commit run --all-files
```

# Content

1. [Hedge Fund Concept](docs/concept_presentation.md) - presentation of this
project concept
    * `fetch_data.ipynb` - download crypto data from binance
    * `mpt.ipynb` - Modern Portfolio Theory form multiple crypto currencies
    * `baseline_strategy.ipynb` - moving average strategy
    * `risk.ipynb` - Risk measures, ARCH, GARCH models

