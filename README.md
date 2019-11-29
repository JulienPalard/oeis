# OEIS

## Project

Implement some [OEIS](https://oeis.org) sequences.

## Usage

After installing the project in a venv using `flit install -s`, use the `oeis` script:

```
$ oeis --random
# A000045

Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

Learn more by running `oeis --help`.


## Side goals

Demo:
- argparse
- pytest
- pylint
- tox
- mypy
- flake8
- bandit
- flake8-bugbear
- black
- travis
- hypothesis
- flit

## Contributing

We are using coding style `black` (https://github.com/psf/black).