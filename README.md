# OEIS

## Project

This project is the implementation of a few sequences from the [OEIS](https://oeis.org).


## Usage

To install it, run: `pip install oeis`.


### CLI usage

`oeis` can be used from command line as:

```bash
$ oeis --help
usage: oeis [-h] [--list] [--start START] [--stop STOP] [--plot] [--random] [--file] [--dark-plot] [sequence]

Print a sweet sequence

positional arguments:
  sequence       Define the sequence to run (e.g.: A181391)

optional arguments:
  -h, --help     show this help message and exit
  --list         List implemented series
  --start START  Define the starting point of the sequence.
  --stop STOP    End point of the sequence (excluded).
  --plot         Print a sweet sweet sweet graph
  --random       Pick a random sequence
  --file         Generates a png of the sequence's plot
  --dark-plot    Print a dark dark dark graph
```

Need a specific sequence?

```bash
$ oeis A000108
# A000108

Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
    Also called Segner numbers.

[1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
```

Lazy? Pick one by random:

```
$ oeis --random
# A000045

Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

Want to see something cool?

```
$ oeis A133058 --plot --stop 1200
```

![A133058 plotted](https://mdk.fr/A133058.png)


### Library usage

The `oeis` module expose sequences as Python Sequences:

```python3
>>> from oeis import A000045
>>> print(*A000045[:10], sep=", ")
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
>>> A000045[0] == A000045[1]
True
>>> A000045[100:101]
[573147844013817084101]
```


## Contributing

We are using the [black]((https://github.com/psf/black) coding style,
and `tox` to run some tests, so after creating a `venv`, installing
dev requirements via `pip install requirements-dev.txt`, run `tox` or
`tox -p auto` (parallel), it should look like this:

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
