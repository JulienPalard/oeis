"""Implementation of a few integer sequences from the OEIS.
"""
import argparse
from random import choice
import math
from itertools import count
from math import factorial
from decimal import Decimal, localcontext
from typing import overload, Union, Dict, List, Callable, Iterable, Sequence, Optional
import sys
import os
from functools import reduce

import numpy as np
from sympy.ntheory import primefactors
import matplotlib.pyplot as plt


__version__ = "0.0.1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a sweet sequence")
    parser.add_argument(
        "sequence",
        type=str,
        help="Define the sequence to run (e.g.: A181391)",
        nargs="?",
    )
    parser.add_argument("--list", action="store_true", help="List implemented series")
    parser.add_argument(
        "--stop", type=int, help="End point of the sequence (excluded).", default=20
    )
    parser.add_argument(
        "--plot", action="store_true", help="Print a sweet sweet sweet graph"
    )
    parser.add_argument("--random", action="store_true", help="Pick a random sequence")
    parser.add_argument(
        "--file", action="store_true", help="Generates a png of the sequence's plot"
    )

    parser.add_argument(
        "--start", type=int, help="Define the starting point of the sequence.",
    )

    parser.add_argument(
        "--dark-plot", action="store_true", help="Print a dark dark dark graph"
    )

    return parser.parse_args()


SerieGenerator = Callable[..., Iterable[int]]


class IntegerSequence:
    def __init__(self, source: SerieGenerator, name: str, doc: Optional[str]) -> None:
        self.name = name
        self.doc = doc
        self._source = source
        self._source_iterator = iter(source())
        self._known: List[int] = []

    def _extend(self, n: int) -> None:
        """Grow the serie.
        """
        while len(self._known) < n:
            try:
                self._known.append(next(self._source_iterator))
            except StopIteration:
                break

    @overload
    def __getitem__(self, key: int) -> int:
        ...

    @overload
    def __getitem__(self, key: slice) -> Sequence[int]:
        ...

    def __getitem__(self, key: Union[int, slice]) -> Union[int, Sequence[int]]:
        if isinstance(key, slice):
            if key.start is not None and key.start < 0:
                raise ValueError("Expected a non-negative indice")
            else:
                self._extend(key.stop)
                return self._known[key.start : key.stop]
        else:
            if key < 0:
                raise ValueError("Expected a non-negative indice")
            try:
                return next(iter(self._source(start=key)))
            except TypeError:
                pass
            self._extend(key + 1)
            return self._known[key]


class OEISRegistry:
    def __init__(self) -> None:
        self.series: Dict[str, IntegerSequence] = {}

    def __getitem__(self, key: str) -> IntegerSequence:
        return self.series[key]

    def __call__(self, function: SerieGenerator) -> IntegerSequence:
        wrapped = IntegerSequence(
            function, name=function.__name__, doc=function.__doc__
        )
        self.series[function.__name__] = wrapped
        return wrapped


oeis = OEISRegistry()


@oeis
def A181391() -> Iterable[int]:
    """Van Eck's sequence:
    For n >= 1, if there exists an m < n such that a(m) = a(n), take
    the largest such m and set a(n+1) = n-m; otherwise a(n+1) =
    0. Start with a(1)=0.
    """
    last_pos: Dict[int, int] = {}
    yield 0
    cur_value = 0
    for i in count():
        next_value = i - last_pos.get(cur_value, i)
        last_pos[cur_value] = i
        yield next_value
        cur_value = next_value


@oeis
def A006577() -> Iterable[int]:
    """Number of halving and tripling steps to reach 1 in '3x+1' problem,
    or -1 if 1 is never reached.
    """

    def steps(n: int) -> int:
        if n == 1:
            return 0
        x = 0
        while True:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            x += 1
            if n < 2:
                break
        return x

    return (steps(n) for n in count())


@oeis
def A000290() -> Iterable[int]:
    "The squares: a(n) = n^2."
    return (n ** 2 for n in count())


@oeis
def A000079() -> Iterable[int]:
    "Powers of 2: a(n) = 2^n."
    return (2 ** n for n in count())


@oeis
def A001221() -> Iterable[int]:
    "Number of distinct primes dividing n (also called omega(n))."
    return (len(primefactors(n)) for n in count(1))


@oeis
def A000045() -> Iterable[int]:
    "Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1."
    a, b = (1, 1)
    yield 1
    while True:
        a, b = b, a + b
        yield a


@oeis
def A115020() -> Iterable[int]:
    "Count backwards from 100 in steps of 7."
    return [n for n in range(100, 0, -7)]


@oeis
def A000040() -> Iterable[int]:
    """Primes number.
    """
    from sympy import sieve

    for i in count(1):
        yield sieve[i]


@oeis
def A023811() -> Iterable[int]:
    "Largest metadrome (number with digits in strict ascending order) in base n."

    def largest_metadrome(n: int) -> int:
        result = 0
        for i, j in enumerate(range(n - 2, -1, -1), start=1):
            result += i * n ** j
        return result

    for n in count():
        yield largest_metadrome(n)


@oeis
def A000010() -> Iterable[int]:
    "Euler totient function phi(n): count numbers <= n and prime to n."

    def phi(n: int) -> int:
        numbers = []
        i = 0
        for i in range(n):
            if math.gcd(i, n) == 1:
                numbers.append(i)
        return len(numbers)

    return (phi(x) for x in count())


@oeis
def A000142() -> Iterable[int]:
    """Factorial numbers: n! = 1*2*3*4*...*n
    (order of symmetric group S_n, number of permutations of n letters).
    """
    return (factorial(i) for i in count())


@oeis
def A000217() -> Iterable[int]:
    "Triangular numbers: a(n) = binomial(n+1,2) = n(n+1)/2 = 0 + 1 + 2 + ... + n."
    for i in count():
        if i + 1 < 2:
            yield 0
        else:
            yield factorial(i + 1) // factorial(2) // factorial((i + 1) - 2)


@oeis
def A008592() -> Iterable[int]:
    "Multiples of 10: a(n) = 10 * n."
    return (10 * n for n in count())


def partitions(n: int) -> List[List[int]]:
    if n == 0:
        return [[0]]
    if n == 1:
        return [[1]]

    partition = [[n]]

    for i in range(1, n):
        for p in partitions(n - i):
            if [i] + p == sorted([i] + p):
                partition.append([i] + p)

    return partition


@oeis
def A000041() -> Iterable[int]:
    "a(n) is the number of partitions of n (the partition numbers)."
    return (len(partitions(n)) for n in count())


@oeis
def A001220() -> Iterable[int]:
    "Wieferich primes: primes p such that p^2 divides 2^(p-1) - 1."
    yield 1093
    yield 3511
    # No other has been found yet...
    # for i in count(3512):
    #     if i in sieve and (2 ** (i - 1) - 1) % (i ** 2) == 0:
    #         yield i


@oeis
def A008587(start: int = 0) -> Iterable[int]:
    "Multiples of 5."
    return (n * 5 for n in count(start))


@oeis
def A008589(start: int = 0) -> Iterable[int]:
    "Multiples of 7."
    return (n * 7 for n in count(start))


@oeis
def A000110() -> Iterable[int]:
    """Bell or exponential numbers: number of ways
    to partition a set of n labeled elements.
    """

    for n in count():
        bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
        bell[0][0] = 1
        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        yield bell[n][0]


@oeis
def A000203() -> Iterable[int]:
    "a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n)."
    for i in count(1):
        divisors = []
        for j in range(int(math.sqrt(i)) + 1):
            if j == 0:
                continue
            elif i % j == 0:
                if i / j == j:
                    divisors.append(j)
                else:
                    divisors.append(j)
                    divisors.append(i // j)
        yield int(sum(divisors))


@oeis
def A000004() -> Iterable[int]:
    "Return an array of n occurence of 0"
    while True:
        yield 0


@oeis
def A001246() -> Iterable[int]:
    "Squares of Catalan numbers"

    def catalan(n: int) -> int:
        if n == 0 or n == 1:
            return 1
        catalan = [0 for i in range(n + 1)]
        catalan[0] = 1
        catalan[1] = 1
        for i in range(2, n + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]
        return catalan[n]

    for i in count():
        yield catalan(i) ** 2


@oeis
def A001247() -> Iterable[int]:
    "Squares of Bell number"

    def bellNumber(start: int) -> int:
        bell = [[0 for i in range(start + 1)] for j in range(start + 1)]
        bell[0][0] = 1
        for i in range(1, start + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        return bell[start][0]

    for i in count():
        yield bellNumber(i) ** 2


@oeis
def A133058() -> Iterable[int]:
    """a(0)=a(1)=1; for n>1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime,
    otherwise a(n) = a(n-1)/gcd(a(n-1),n).
    """
    last = 1
    for i in count():
        if i == 0 or i == 1:
            yield 1
        elif (math.gcd(i, last)) == 1:
            last = last + i + 1
            yield last
        else:
            last = int(last / math.gcd(last, i))
            yield last


@oeis
def A000005() -> Iterable[int]:
    "d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n."
    for i in count(1):
        divisors = 0
        for j in range(int(math.sqrt(i)) + 1):
            if j == 0:
                continue
            elif i % j == 0:
                if i / j == j:
                    divisors += 1
                else:
                    divisors += 2
        yield divisors


@oeis
def A000108() -> Iterable[int]:
    """Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
    Also called Segner numbers.
    """
    for i in count():
        r = (factorial(2 * i) // factorial(i) // factorial(2 * i - i)) / (i + 1)
        yield int(r)


@oeis
def A007953() -> Iterable[int]:
    "Digital sum (i.e., sum of digits) of n; also called digsum(n)."
    for n in count():
        yield sum(int(d) for d in str(n))


@oeis
def A000120() -> Iterable[int]:
    """1's-counting sequence: number of 1's in binary
    expansion of n (or the binary weight of n).
    """

    return ("{:b}".format(n).count("1") for n in count())


@oeis
def A001622() -> Iterable[int]:
    "Decimal expansion of golden ratio phi (or tau) = (1 + sqrt(5))/2."
    with localcontext() as ctx:
        ctx.prec = 99999
        tau = (1 + Decimal(5).sqrt()) / 2
        for n in count():
            yield math.floor(tau * 10 ** n) % 10


@oeis
def A007947(start: int = 0) -> Iterable[int]:
    """Largest squarefree number dividing n:
    the squarefree kernel of n, rad(n), radical of n.
    """
    start += 1
    for i in count(start):
        if i < 2:
            yield 1
        else:
            yield reduce(lambda x, y: x * y, primefactors(i))


def show_oeis_list() -> None:
    for name, sequence in sorted(oeis.series.items(), key=lambda kvp: kvp[0]):
        if sequence.doc:
            print("-", name, sequence.doc.replace("\n", " ").replace("     ", " "))
        else:
            print("-", name)


@oeis
def A000326() -> Iterable[int]:
    """Pentagonal numbers: a(n) = n*(3*n-1)/2:"""
    return (n * (3 * n - 1) // 2 for n in count())


def main() -> None:
    args = parse_args()

    if args.list:
        show_oeis_list()
        exit(0)

    if args.random:
        args.sequence = choice(list(oeis.series.values())).name

    if not args.sequence:
        print(f"No sequence given, please see oeis --help, or try oeis --random")
        exit(1)

    if args.sequence not in oeis.series:
        print("Unimplemented serie", file=sys.stderr)
        exit(1)

    serie = oeis.series[args.sequence][args.start : args.stop]

    if args.plot:
        plt.scatter(list(range(len(serie))), serie)
        plt.show()
    elif args.dark_plot:
        colors = []
        for _i in range(len(serie)):
            colors.append(np.random.rand())
        with plt.style.context("dark_background"):
            plt.scatter(list(range(len(serie))), serie, s=50, c=colors, alpha=0.5)
        plt.show()
    else:
        print("#", args.sequence, end="\n\n")
        print(oeis.series[args.sequence].doc, end="\n\n")
        print(serie)

    if args.file:
        if args.plot or args.dark_plot:
            if not os.path.exists("graph"):
                print("No graph directory found, creating...")
                try:
                    os.mkdir("graph")
                except OSError:
                    print("Creation of the graph directory failed")
                else:
                    print("Successfully created the graph directory")
            plt.savefig(f"graph/{args.sequence}.png")
            print(f"Graph printed in graph/{args.sequence}.png")
        else:
            print("You cannot use --file without --plot or --dark_plot")


if __name__ == "__main__":
    main()
