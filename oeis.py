"""
Tool that return a given sequence
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
import math
from math import factorial
import sys


__version__ = "0.0.1"


def parse_args():
    parser = argparse.ArgumentParser(description="Print a sweet sequence")
    parser.add_argument(
        "sequence",
        type=str,
        help="Define the sequence to run (e.g.: A181391)",
        nargs="?",
    )
    parser.add_argument("--list", action="store_true", help="List implemented series")
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Define the limit of the sequence, (default: 20)",
    )
    parser.add_argument(
        "--plot", action="store_true", help="Print a sweet sweet sweet graph"
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Define the starting point of the sequence (default: 0)",
    )

    return parser.parse_args()


class OEISRegistry:
    def __init__(self):
        self.series = {}

    def __call__(self, function):
        self.series[function.__name__] = function
        return function


oeis = OEISRegistry()


@oeis
def A181391(start=0, limit=20):
    """Van Eck's sequence: For n >= 1,
    if there exists an m < n such that a(m) = a(n),
    take the largest such m and set a(n+1) = n-m;
    otherwise a(n+1) = 0. Start with a(1)=0.
    """
    sequence = [0]
    last_pos = {}

    for i in range(start + limit):
        new_value = i - last_pos.get(sequence[i], i)
        sequence.append(new_value)
        last_pos[sequence[i]] = i

    return sequence[start : start + limit]


@oeis
def A006577(start, limit):
    """Number of halving and tripling steps to reach 1 in '3x+1' problem,
    or -1 if 1 is never reached.
    """

    def steps(n):
        if n == 1:
            return 0
        x = 0
        while True:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            x += 1
            if n < 2:
                break
        return x

    return [steps(n) for n in range(start, start + limit)]


@oeis
def A000290(start=0, limit=20):
    "The squares: a(n) = n^2."
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(i * i)
        x.append(i)

    return sequence


@oeis
def A000079(start=0, limit=20):
    "Powers of 2: a(n) = 2^n."
    seq = []
    for n in range(start, limit):
        seq.append(2 ** n)
    return seq


@oeis
def A000045(start=0, limit=20):
    "Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1."
    sequence = []
    sequence.append(0)
    sequence.append(1)
    for i in range(2, limit):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


@oeis
def A115020(start, limit):
    "Count backwards from 100 in steps of 7."
    result = []
    for n in range(100, 0, -7):
        if n >= 0:
            result.append(n)

    return result[start : start + limit]


@oeis
def A000040(start, end):
    "The prime numbers."
    result = []
    resultIndex = []
    i = 0
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                result.append(val)
                resultIndex.append(i)
                i = i + 1
    return result


@oeis
def A000010(start, limit):
    "Euler totient function phi(n): count numbers <= n and prime to n."

    def phi(n):
        numbers = []
        i = 0
        for i in range(n):
            if math.gcd(i, n) == 1:
                numbers.append(i)
        return len(numbers)

    return [phi(x) for x in range(start, start + limit)]


@oeis
def A000142(start=0, limit=20):
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
def A000217(start=0, limit=20):
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
def A008592(start, limit):
    "Multiples of 10: a(n) = 10 * n."
    end = limit + start
    my_list = []
    i = 0
    print("A008592 sequence:")
    while i < end:
        my_list.append(i * 10)
        i += 1
    return my_list[start:end]


def partitions(n):
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
def A000041(start, limit):
    "a(n) is the number of partitions of n (the partition numbers)."
    return [len(partitions(n)) for n in range(start, start + limit)]


@oeis
def A000203(start=0, limit=20):
    "a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n)."
    sequence = []
    if start == 0:
        start += 1
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
                    divisors.append(i / j)
        sequence.append(int(sum(divisors)))
    return sequence


@oeis
def A133058(start=0, limit=20):
    "a(0)=a(1)=1; for n>1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime, otherwise a(n) = a(n-1)/gcd(a(n-1),n). "
    sequence = []

    for i in range(0, start + limit):
        if i == 0 or i == 1:
            sequence.append(1)
        elif (math.gcd(i, sequence[i - 1])) == 1:
            sequence.append(sequence[i - 1] + i + 1)
        else:
            sequence.append(int(sequence[i - 1] / math.gcd(sequence[i - 1], i)))

    return sequence[start:]


def main():
    args = parse_args()
    if args.list:
        for name, function in oeis.series.items():
            print(
                "-", name, function.__doc__.replace("\n", " ").replace("     ", " "),
            )
        exit(0)
    if args.sequence not in oeis.series:
        print("Unimplemented serie", file=sys.stderr)
        exit(1)
    serie = oeis.series[args.sequence](args.start, args.limit)
    if args.plot:
        plt.plot(list(range(len(serie))), serie)
    else:
        print(serie)


if __name__ == "__main__":
    main()
