"""Tool that return a given sequence
"""
import argparse
from random import choice
import math
from math import factorial
from decimal import Decimal, localcontext
from typing import Collection, Dict, List, Callable
import sys
import os
from sympy import primefactors
from functools import reduce

import numpy as np
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
        "--limit", type=int, help="Qty of numbers to print.",
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


Serie = Callable[..., Collection[int]]


class OEISRegistry:
    def __init__(self) -> None:
        self.series: Dict[str, Serie] = {}

    def __call__(self, function: Serie) -> Serie:
        self.series[function.__name__] = function
        return function


oeis = OEISRegistry()


@oeis
def A181391(start: int = 0, limit: int = 20) -> Collection[int]:
    """Van Eck's sequence: For n >= 1,
    if there exists an m < n such that a(m) = a(n),
    take the largest such m and set a(n+1) = n-m;
    otherwise a(n+1) = 0. Start with a(1)=0.
    """
    sequence = [0]
    last_pos: Dict[int, int] = {}

    for i in range(start + limit):
        new_value = i - last_pos.get(sequence[i], i)
        sequence.append(new_value)
        last_pos[sequence[i]] = i

    return sequence[start : start + limit]


@oeis
def A006577(start: int = 0, limit: int = 20) -> Collection[int]:
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

    return [steps(n) for n in range(start, start + limit)]


@oeis
def A000290(start: int = 0, limit: int = 20) -> Collection[int]:
    "The squares: a(n) = n^2."
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(i * i)
        x.append(i)

    return sequence


@oeis
def A000079(start: int = 0, limit: int = 20) -> Collection[int]:
    "Powers of 2: a(n) = 2^n."
    seq = []
    for n in range(start, start + limit):
        seq.append(2 ** n)
    return seq


@oeis
def A000045(start: int = 0, limit: int = 20) -> Collection[int]:
    "Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1."
    sequence = [1, 1]
    for i in range(2, start + limit):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[start:]


@oeis
def A115020(start: int = 0, limit: int = 15) -> Collection[int]:
    "Count backwards from 100 in steps of 7."
    result = []
    for n in range(100, 0, -7):
        if n >= 0:
            result.append(n)

    return result[start : start + limit]


@oeis
def A000040(start: int = 1, limit: int = 20) -> Collection[int]:
    "Return all primes number between range"
    from sympy import sieve

    return list(sieve[start : start + limit])


@oeis
def A000010(start: int = 0, limit: int = 20) -> Collection[int]:
    "Euler totient function phi(n): count numbers <= n and prime to n."

    def phi(n: int) -> int:
        numbers = []
        i = 0
        for i in range(n):
            if math.gcd(i, n) == 1:
                numbers.append(i)
        return len(numbers)

    return [phi(x) for x in range(start, start + limit)]


@oeis
def A000142(start: int = 0, limit: int = 20) -> Collection[int]:
    """Factorial numbers: n! = 1*2*3*4*...*n
    (order of symmetric group S_n, number of permutations of n letters).
    """
    sequence = []
    colors = []
    x = []
    for i in range(start, start + limit):
        sequence.append(factorial(i))
        colors.append(np.random.rand())
        x.append(i)

    return sequence


@oeis
def A000217(start: int = 0, limit: int = 20) -> Collection[int]:
    "Triangular numbers: a(n) = binomial(n+1,2) = n(n+1)/2 = 0 + 1 + 2 + ... + n."
    sequence = []
    x = []
    for i in range(start, start + limit):
        if i + 1 < 2:
            sequence.append(0)
        else:
            sequence.append(factorial(i + 1) // factorial(2) // factorial((i + 1) - 2))

        x.append(i)

    return sequence


@oeis
def A008592(start: int = 0, limit: int = 20) -> Collection[int]:
    "Multiples of 10: a(n) = 10 * n."
    end = limit + start
    my_list = []
    i = 0
    print("A008592 sequence:")
    while i < end:
        my_list.append(i * 10)
        i += 1
    return my_list[start:end]


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
def A000041(start: int = 0, limit: int = 20) -> Collection[int]:
    "a(n) is the number of partitions of n (the partition numbers)."
    return [len(partitions(n)) for n in range(start, start + limit)]


@oeis
def A001220(start: int = 0, limit: int = 2) -> Collection[int]:
    "Wieferich primes: primes p such that p^2 divides 2^(p-1) - 1."
    sequence: List[int] = []
    i = 1
    while len(sequence) < start + limit:
        i += 1
        if is_prime(i) and (2 ** (i - 1) - 1) % (i ** 2) == 0:
            sequence.append(i)
    return sequence[start:]


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 7 == 0:
        return False
    elif n % 9 == 0:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


@oeis
def A000203(start: int = 1, limit: int = 20) -> Collection[int]:
    "a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n)."
    sequence = []
    for i in range(start, start + limit):
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
        sequence.append(int(sum(divisors)))
    return sequence


@oeis
def A000004(start: int = 0, limit: int = 20) -> Collection[int]:
    "Return an array of n occurence of 0"
    result = []
    for i in range(limit):
        result.append(0)
    return result


@oeis
def A001246(start: int = 0, limit: int = 20) -> Collection[int]:
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

    result = []
    for i in range(start, start + limit):
        result.append((catalan(i)) * catalan(i))
    return result


@oeis
def A001247(start: int = 0, limit: int = 20) -> Collection[int]:
    "Squares of Bell number"

    def bellNumber(start: int) -> int:
        bell = [[0 for i in range(start + 1)] for j in range(start + 1)]
        bell[0][0] = 1
        for i in range(1, start + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        return bell[start][0]

    result = []
    for i in range(start, start + limit):
        result.append(bellNumber(i) ** 2)
    return result


@oeis
def A133058(start: int = 0, limit: int = 20) -> Collection[int]:
    """a(0)=a(1)=1; for n>1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime,
    otherwise a(n) = a(n-1)/gcd(a(n-1),n).
    """
    sequence = []

    for i in range(0, start + limit):
        if i == 0 or i == 1:
            sequence.append(1)
        elif (math.gcd(i, sequence[i - 1])) == 1:
            sequence.append(sequence[i - 1] + i + 1)
        else:
            sequence.append(int(sequence[i - 1] / math.gcd(sequence[i - 1], i)))

    return sequence[start:]


@oeis
def A000005(start: int = 1, limit: int = 20) -> Collection[int]:
    "d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n."
    sequence = []

    for i in range(start, start + limit):
        divisors = 0
        for j in range(int(math.sqrt(i)) + 1):
            if j == 0:
                continue
            elif i % j == 0:
                if i / j == j:
                    divisors += 1
                else:
                    divisors += 2
        sequence.append(divisors)
    return sequence


@oeis
def A000108(start: int = 0, limit: int = 20) -> Collection[int]:
    """Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
    Also called Segner numbers.
    """
    sequence = []
    for i in range(start, start + limit):
        r = (factorial(2 * i) // factorial(i) // factorial(2 * i - i)) / (i + 1)
        sequence.append(int(r))

    return sequence


@oeis
def A007953(start: int = 0, limit: int = 20) -> Collection[int]:
    "Digital sum (i.e., sum of digits) of n; also called digsum(n)."
    sequence = []

    for n in range(start, start + limit):
        sequence.append(sum(int(d) for d in str(n)))

    return sequence


@oeis
def A000120(start: int = 0, limit: int = 20) -> Collection[int]:
    """1's-counting sequence: number of 1's in binary
    expansion of n (or the binary weight of n).
    """

    return ["{:b}".format(n).count("1") for n in range(start, start + limit)]


@oeis
def A001622(start: int = 0, limit: int = 20) -> Collection[int]:
    "Decimal expansion of golden ratio phi (or tau) = (1 + sqrt(5))/2."
    with localcontext() as ctx:
        ctx.prec = start + limit + 4
        tau = (1 + Decimal(5).sqrt()) / 2

        return [(math.floor(tau * 10 ** n) % 10) for n in range(start, start + limit)]


@oeis
def A007947(start: int = 1, limit: int = 20) -> Collection[int]:
    """Largest squarefree number dividing n:
    the squarefree kernel of n, rad(n), radical of n.
    """
    sequence = []
    for i in range(start, start + limit):
        if i < 2:
            sequence.append(1)
        else:
            n = reduce(lambda x, y: x * y, primefactors(i))
            sequence.append(n)

    return sequence


def show_oeis_list() -> None:
    for name, function in sorted(oeis.series.items(), key=lambda kvp: kvp[0]):
        if function.__doc__:
            print("-", name, function.__doc__.replace("\n", " ").replace("     ", " "))
        else:
            print("-", name)


@oeis
def A000326(start: int = 0, limit: int = 10) -> Collection[int]:
    """Pentagonal numbers: a(n) = n*(3*n-1)/2:"""
    return [n * (3 * n - 1) // 2 for n in range(start, start + limit)]


def main() -> None:
    args = parse_args()
    if args.list:
        show_oeis_list()
        exit(0)

    if args.random:
        args.sequence = choice(list(oeis.series.values())).__name__

    if not args.sequence:
        print(f"No sequence given, please see oeis --help, or try oeis --random")
        exit(1)

    if args.sequence not in oeis.series:
        print("Unimplemented serie", file=sys.stderr)
        exit(1)

    kwargs = {}
    if args.start:
        kwargs["start"] = args.start
    if args.limit:
        kwargs["limit"] = args.limit
    serie = oeis.series[args.sequence](**kwargs)

    if args.plot:
        plt.scatter(list(range(len(serie))), serie)
        plt.show()
    elif args.dark_plot:
        colors = []
        for i in range(len(serie)):
            colors.append(np.random.rand())
        with plt.style.context("dark_background"):
            plt.scatter(list(range(len(serie))), serie, s=50, c=colors, alpha=0.5)
        plt.show()
    else:
        print("#", args.sequence, end="\n\n")
        print(oeis.series[args.sequence].__doc__, end="\n\n")
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
