# OEIS

## Project

This project is the implementation of a few sequences from the [OEIS](https://oeis.org).


## Usage

After installing the project in a venv using `flit install -s`, use
the `oeis` script:

```
$ oeis --random
# A000045

Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

Learn more by running `oeis --help`.


## Usage as a library

You can import sequences individually:

```python3
>>> from oeis import A000045
>>> print(*A000045[:10], sep=", ")
1, 1, 2, 3, 5, 8, 13, 21, 34, 55

```

Or as a dict:

```python3
>>> from oeis import oeis
>>> print(*oeis["A000045"][:10], sep=", ")
1, 1, 2, 3, 5, 8, 13, 21, 34, 55

```

All sequences can be accessed as normal Python sequences:

```python3
>>> A000045[0] == A000045[1]
True
>>> A000045[100:101]
[573147844013817084101]

```


## Contributing

We are using the [black]((https://github.com/psf/black) coding
style, and tox to run some tests, so after creating a venv, and `pip
install requirements-dev.txt`, run `tox` or `tox -p auto` (parallel), it
should look like this:

```
$ tox -p auto
✔ OK mypy in 11.807 seconds
✔ OK flake8 in 12.024 seconds
✔ OK black in 12.302 seconds
✔ OK py36 in 13.776 seconds
✔ OK py37 in 15.344 seconds
✔ OK py38 in 21.041 seconds
______________________________________ summary ________________________________________
  py36: commands succeeded
  py37: commands succeeded
  py38: commands succeeded
  flake8: commands succeeded
  mypy: commands succeeded
  black: commands succeeded
  congratulations :)
```
