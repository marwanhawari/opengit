<p align="center">
  <img width=60% height=auto src="https://github.com/marwanhawari/opengit/raw/main/docs/opengit_logo.png" alt="opengit logo"/>
  
</p>

[![PyPI version](https://badge.fury.io/py/opengit.svg)](https://badge.fury.io/py/opengit)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/opengit)](https://pypi.org/project/opengit/)
[![Build Status](https://github.com/marwanhawari/opengit/actions/workflows/build.yml/badge.svg)](https://github.com/marwanhawari/opengit/actions)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/marwanhawari/opengit/blob/main/CODE_OF_CONDUCT.md)
[![GitHub](https://img.shields.io/github/license/marwanhawari/opengit?color=blue)](https://github.com/marwanhawari/opengit/blob/main/LICENSE)

# Description
A simple command-line tool to open the remote repository of a local git repository. No set-up. No configuration.

# Installation
The `opengit` package can be installed directly using `pip`.
```
pip install opengit
```

# Usage
* Run `opengit` from inside a local git repository. For example, when running from inside the `fastapi` repository:
```
$ opengit
Opening https://github.com/tiangolo/fastapi.git
```

* Alternatively, run `opengit` on a specified directory. For example when running on the `uvicorn` directory:
```
$ opengit uvicorn/
Opening https://github.com/encode/uvicorn.git
```

### Options
```
usage: opengit [-h] [directory]

positional arguments:
  directory   Specify a directory or leave empty for the current directory.

optional arguments:
  -h, --help  show this help message and exit
```

