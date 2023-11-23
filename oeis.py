"""Implementation of a few integer sequences from the OEIS."""
import argparse
import math
import sys
from decimal import Decimal, localcontext
from functools import lru_cache, reduce
from itertools import count
from random import choice, random
from typing import Callable, Dict, Iterable, Iterator, List, Sequence, Union, overload

# Version format is YYYY.MM.DD (https://calver.org/)
__version__ = "2023.3.10"


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Print a sweet sweet sequence")
    parser.add_argument(
        "sequence",
        type=str,
        help="Define the sequence to run (e.g.: A181391)",
        nargs="?",
    )
    parser.add_argument("--list", action="store_true", help="List implemented series")
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Define the starting point of the sequence.",
    )
    parser.add_argument(
        "--stop", type=int, help="End point of the sequence (excluded).", default=20
    )
    parser.add_argument(
        "--plot", action="store_true", help="Print a sweet sweet sweet graph"
    )
    parser.add_argument("--random", action="store_true", help="Pick a random sequence")
    parser.add_argument(
        "--file", help="Write a png of the sequence's plot to the given png file."
    )
    parser.add_argument(
        "--dark-plot", action="store_true", help="Print a dark dark dark graph"
    )
    return parser.parse_args()


SerieGenerator = Callable[..., Iterable[int]]


class IntegerSequence:  # pylint: disable=too-few-public-methods
    """This class holds information for a integer sequence.

    Its name, its description, a function to generate its values, and
    provide a nice cached access to it.
    """

    def __init__(self, offset, **kwargs):
        """Build a new integer sequence starting at the given offset."""
        self.offset = offset
        super().__init__(**kwargs)

    def check_key(self, key):
        """Check the given key is correct knowing the sequence offset."""
        if key < self.offset:
            raise IndexError(
                f"{type(self).__name__} starts at offset {self.offset}, not {key}."
            )

    def check_slice(self, key: slice) -> slice:
        """Check if the given slice is correct knowing the sequence offset.

        Returns a new slice object taking the offset into account.
        """
        start = key.start or 0
        if key.stop is None:
            raise IndexError("Infinite slices of sequences is not implemented yet.")
        if key.start is None and self.offset != 0:
            raise IndexError(
                f"Not providing a start index for {type(self).__name__} is "
                f"ambiguous, as it starts at offset {self.offset}."
            )
        if start < self.offset:
            raise IndexError(
                f"{type(self).__name__} starts at offset {self.offset}, not {start}."
            )
        return slice(start - self.offset, key.stop - self.offset, key.step)

    @overload
    def __getitem__(self, key: int) -> int:
        """Return a value from an integer sequence."""

    @overload
    def __getitem__(self, key: slice) -> Sequence[int]:
        """Return a slice from an integer sequence."""

    def __getitem__(self, key: Union[int, slice]) -> Union[int, Sequence[int]]:
        """Return a slice or a value from an integer sequence."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[int]:
        """Iterate over the integer sequence."""
        for i in count(self.offset):
            yield self[i]


class IntegerSequenceFromGenerator(IntegerSequence):
    """IntegerSequence based on a generator.

    Can be used like:

    >>> s = IntegerSequenceFromGenerator(source=count)
    >>> s[:10]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def __init__(self, source: SerieGenerator, **kwargs) -> None:
        """Build a new sequence."""
        self._source = source
        self._source_iterator = iter(source())
        self._known: List[int] = []
        super().__init__(**kwargs)

    def __iter__(self) -> Iterator[int]:
        """Iterate over an integer sequence."""
        return iter(self._source())

    def _extend(self, n: int) -> None:
        """Grow the serie."""
        while len(self._known) < n:
            try:
                self._known.append(next(self._source_iterator))
            except StopIteration:
                break

    @overload
    def __getitem__(self, key: int) -> int:
        """Return a value from an integer sequence."""

    @overload
    def __getitem__(self, key: slice) -> Sequence[int]:
        """Return a slice from an integer sequence."""

    def __getitem__(self, key: Union[int, slice]) -> Union[int, Sequence[int]]:
        """Return a value from the sequence (or a slice of it)."""
        if isinstance(key, slice):
            key = self.check_slice(key)
            self._extend(key.stop)
            return self._known[key]
        self.check_key(key)
        try:
            return next(iter(self._source(start=key - self.offset)))
        except TypeError:
            pass
        self._extend(key + 1)
        return self._known[key - self.offset]


class IntegerSequenceFromFunction(
    IntegerSequence
):  # pylint: disable=too-few-public-methods
    """IntegerSequence based on a function.

    Can be used like:

    >>> s = IntegerSequenceFromFunction(source=lambda x: x)
    >>> s[:10]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def __init__(self, source: Callable[[int], int], **kwargs) -> None:
        """Build a new sequence."""
        self._source = lru_cache(maxsize=4096)(source)
        self._known: List[int] = []
        super().__init__(**kwargs)

    @overload
    def __getitem__(self, key: int) -> int:
        """Return a value from an integer sequence."""

    @overload
    def __getitem__(self, key: slice) -> Sequence[int]:
        """Return a slice from an integer sequence."""

    def __getitem__(self, key: Union[int, slice]) -> Union[int, Sequence[int]]:
        """Return a value from the sequence (or a slice of it)."""
        if isinstance(key, slice):
            self.check_slice(key)
            return [
                self._source(i) for i in range(key.start or 0, key.stop, key.step or 1)
            ]
        self.check_key(key)
        return self._source(key)


class OEISRegistry:
    """A dict-like object to store OEIS sequences.

    Used as a decorator, wrapping simple generators to full
    IntegerSequence instances.
    """

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self.series: Dict[str, IntegerSequence] = {}

    def __getitem__(self, key: str) -> IntegerSequence:
        """Return a sequence by name."""
        return self.series[key]

    def print_list(self) -> None:
        """Print a list of OEIS series.

        Like:
        - A000004 Return an array of n occurence of 0
        - A000005 d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n.
        - ...
        """
        for name, sequence in sorted(self.series.items(), key=lambda kvp: kvp[0]):
            if sequence.__doc__:
                print(
                    "-", name, sequence.__doc__.replace("\n", " ").replace("     ", " ")
                )

    def from_(self, wrapper_type, to_wrap, offset=0):
        """Register a new integer sequence, wrapping it in wrapper_type."""
        wrapped = type(
            to_wrap.__name__,
            (wrapper_type,),
            {"__doc__": to_wrap.__doc__},
        )(to_wrap, offset=offset)
        self.series[to_wrap.__name__] = wrapped
        return wrapped

    def from_function(
        self, offset=0
    ) -> Callable[[Callable[[int], int]], IntegerSequenceFromFunction]:
        """Register a new integer sequence, implemented as a function."""

        def wrapper(function: Callable[[int], int]):
            return self.from_(IntegerSequenceFromFunction, function, offset)

        return wrapper

    def from_generator(
        self, offset=0
    ) -> Callable[[SerieGenerator], IntegerSequenceFromGenerator]:
        """Register a new integer sequence, implemented as a generator."""

        def wrapper(function: SerieGenerator) -> IntegerSequenceFromGenerator:
            return self.from_(IntegerSequenceFromGenerator, function, offset)

        return wrapper


oeis = OEISRegistry()


@oeis.from_function(offset=1)
def A000037(n: int) -> int:
    """Give Numbers that are not squares (or, the nonsquares).

    a(n) = A000194(n) + n = floor(1/2 *(1 + sqrt(4*n-3))) + n.
    - Jaroslav Krizek, Jun 14 2009
    """
    from math import floor, sqrt

    return floor(1 / 2 * (1 + sqrt(4 * n - 3))) + n


@oeis.from_generator(offset=1)
def A181391() -> Iterable[int]:
    """Van Eck's sequence.

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


@oeis.from_function(offset=1)
def A006577(n: int) -> int:
    """Give the number of halving and tripling steps to reach 1 in '3x+1' problem."""
    x = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        x += 1
    return x


@oeis.from_function()
def A000290(n: int) -> int:
    """Squares numbers: a(n) = n^2."""
    return n**2


@oeis.from_function()
def A000079(n: int) -> int:
    """Powers of 2: a(n) = 2^n."""
    return 2**n


@oeis.from_function(offset=1)
def A001221(n: int) -> int:
    """omage(n).

    Number of distinct primes dividing n.
    """
    from sympy.ntheory import primefactors

    return len(primefactors(n))


@oeis.from_generator()
def A000045() -> Iterable[int]:
    """Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1."""
    a, b = (0, 1)
    while True:
        yield a
        a, b = b, a + b


@oeis.from_generator()
def A000032() -> Iterable[int]:
    """Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1."""
    a, b = (2, 1)
    while True:
        yield a
        a, b = b, a + b


@oeis.from_function()
def A000119(n: int) -> int:
    """Give the number of representations of n as a sum of distinct Fib. numbers."""

    def f(x, y, z):
        if x < y:
            return 0**x
        return f(x - y, y + z, y) + f(x, y + z, y)

    return f(n, 1, 1)


@oeis.from_function()
def A000121(n: int) -> int:
    """Give Number of representations of n as a sum of Fibonacci numbers.

    (1 is allowed twice as a part).
    a(0) = 1; for n >= 1, a(n) = A000119(n) + A000119(n-1). - Peter Munn, Jan 19 2018
    """
    if n == 0:
        return 1
    return A000119[n] + A000119[n - 1]


@oeis.from_generator()
def A115020() -> Iterable[int]:
    """Count backwards from 100 in steps of 7."""
    for i in range(100, 0, -7):
        yield i


@oeis.from_function(offset=1)
def A000040(n: int) -> int:
    """Primes number."""
    from sympy import sieve

    return sieve[n]


@oeis.from_function(offset=1)
def A023811(n: int) -> int:
    """Largest metadrome.

    (number with digits in strict ascending order) in base n.
    """
    result = 0
    for i, j in enumerate(range(n - 2, -1, -1), start=1):
        result += i * n**j
    return result


@oeis.from_function(offset=1)
def A000010(n: int) -> int:
    """Euler totient function phi(n): count numbers <= n and prime to n."""
    numbers = []
    i = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)


@oeis.from_function()
def A000142(n: int) -> int:
    """Factorial numbers: n! = 1*2*3*4*...*n.

    (order of symmetric group S_n, number of permutations of n letters).
    """
    return math.factorial(n)


@oeis.from_function()
def A000217(n: int):
    """Triangular numbers: a(n) = binomial(n+1,2) = n(n+1)/2 = 0 + 1 + 2 + ... + n."""
    return n * (n + 1) // 2


@oeis.from_function()
def A008592(n: int) -> int:
    """Multiples of 10: a(n) = 10 * n."""
    return 10 * n


@oeis.from_function()
def A000041(n: int) -> int:
    """Parittion numbers.

    a(n) is the number of partitions of n (the partition numbers).
    """
    parts = [0] * (n + 1)
    parts[0] = 1
    for value in range(1, n + 1):
        for j in range(value, n + 1):
            parts[j] += parts[j - value]
    return parts[n]


@oeis.from_generator(offset=1)
def A001220() -> Iterable[int]:
    """Wieferich primes: primes p such that p^2 divides 2^(p-1) - 1."""
    yield 1093
    yield 3511
    # No other has been found yet...
    # for i in count(3512):
    #     if i in sieve and (2 ** (i - 1) - 1) % (i ** 2) == 0:
    #         yield i


@oeis.from_function()
def A008587(n: int) -> int:
    """Multiples of 5."""
    return n * 5


@oeis.from_function()
def A008589(n: int) -> int:
    """Multiples of 7."""
    return n * 7


@oeis.from_function()
def A000110(n: int) -> int:
    """Bell or exponential numbers.

    Number of ways to partition a set of n labeled elements.
    """
    bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]


@oeis.from_function(offset=1)
def A000203(i: int) -> int:
    """Give sum of the divisors of n.

    a(n) = sigma(n). Also called sigma_1(n).
    """
    divisor_sum = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisor_sum += j
            if i // j != j:
                divisor_sum += i // j
    return divisor_sum


@oeis.from_function()
def A000004(n: int) -> int:  # pylint: disable=unused-argument
    """Return an infinite sequence of 0."""
    return 0


@oeis.from_function()
def A001246(n: int) -> int:
    """Squares of Catalan numbers."""
    return A000108[n] ** 2  # pylint: disable=unsubscriptable-object


@oeis.from_function()
def A001247(n: int) -> int:
    """Squares of Bell number."""
    return A000110[n] ** 2  # pylint: disable=unsubscriptable-object


@oeis.from_generator()
def A133058() -> Iterable[int]:
    """« Fly straight, dammit » sequence.

    a(0)=a(1)=1; for n>1, a(n) = a(n-1) + n + 1 if a(n-1) and n are coprime,
    otherwise a(n) = a(n-1)/gcd(a(n-1),n).
    """
    last = 1
    yield 1
    yield 1
    for i in count(2):
        if (math.gcd(i, last)) == 1:
            last = last + i + 1
        else:
            last = int(last / math.gcd(last, i))
        yield last


@oeis.from_function(offset=1)
def A000005(i: int) -> int:
    """d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n."""
    divisors = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if i / j == j:
                divisors += 1
            else:
                divisors += 2
    return divisors


@oeis.from_function()
def A000108(i: int) -> int:
    """Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).

    Also called Segner numbers.
    """
    return math.factorial(2 * i) // math.factorial(i) ** 2 // (i + 1)


@oeis.from_function()
def A007953(n: int) -> int:
    """Digital sum (i.e., sum of digits) of n; also called digsum(n)."""
    return sum(int(d) for d in str(n))


@oeis.from_function(offset=1)
def A265326(n: int) -> int:
    """Give n-th prime minus its binary reversal."""
    from sympy.ntheory import prime

    p = prime(n)
    pbinrev = int(bin(p)[:1:-1], 2)
    return p - pbinrev


@oeis.from_function()
def A000120(n: int) -> int:
    """1's-counting sequence.

    number of 1's in binary expansion of n (or the binary weight of
    n).
    """
    return f"{n:b}".count("1")


@oeis.from_generator(offset=1)
def A001622() -> Iterable[int]:
    """Decimal expansion of golden ratio phi (or tau) = (1 + sqrt(5))/2."""
    with localcontext() as ctx:
        ctx.prec = 10
        start = 0
        while True:
            ctx.prec *= 10
            phi = (1 + Decimal(5).sqrt()) / 2
            for n in range(start, ctx.prec - 1):
                yield math.floor(phi * 10**n) % 10
            start = n + 1


@oeis.from_function(offset=1)
def A007947(i: int) -> int:
    """Largest squarefree number dividing n.

    The squarefree kernel of n, rad(n), radical of n.
    """
    from sympy.ntheory import primefactors

    if i < 2:
        return 1
    return reduce(lambda x, y: x * y, primefactors(i))


@oeis.from_function()
def A000326(n: int) -> int:
    """Pentagonal numbers: a(n) = n*(3*n-1)/2."""
    return n * (3 * n - 1) // 2


@oeis.from_function(offset=1)
def A165736(n: int) -> int:
    """Give n^n^n^... modulo 10^10."""
    x = n
    for t in range(1, 11):
        x = pow(n, x, pow(10, t))
    return x


@oeis.from_generator(offset=1)
def A001462() -> Iterable[int]:
    """Golomb sequence."""
    sequence = [0, 1, 2, 2]
    for term in sequence[1:]:
        yield term
    n = 3
    while True:
        new_terms = [n for i in range(sequence[n])]
        for term in new_terms:
            yield term
        sequence.extend(new_terms)
        n += 1


@oeis.from_function()
def A004767(n: int) -> int:
    """Integers of a(n) = 4*n + 3."""
    return 4 * n + 3


@oeis.from_function()
def A004086(i: int) -> int:
    """Digit reversal of i."""
    result = 0
    while i > 0:
        unit = i % 10
        result = result * 10 + unit
        i = i // 10
    return result


@oeis.from_function(offset=0)
def A008588(i: int) -> int:
    """Nonnegative multiples of 6."""
    return i * 6


@oeis.from_generator(offset=1)
def A001969() -> Iterable[int]:
    """Evil numbers: numbers with an even number of 1's in their binary expansion."""
    return (i for i in count() if f"{i:b}".count("1") % 2 == 0)


@oeis.from_function(offset=1)
def A064367(n: int) -> int:
    """Show result of a(n) = 2^n mod prime(n).

    Or 2^n = k*prime(n) + a(n) with integer k.
    """
    from sympy.ntheory import prime

    return 2**n % prime(n)


@oeis.from_function()
def A007089(n: int) -> int:
    """Numbers in base 3."""
    if n == 0:
        return 0
    digits: list = []
    while n:
        n, r = divmod(n, 3)
        digits += str(r)
    o = "".join(reversed(digits))
    return int(o)


@oeis.from_function()
def A002275(n: int) -> int:
    """Repunits: (10^n - 1)/9. Often denoted by R_n."""
    if n == 0:
        return 0
    return int("1" * n)


@oeis.from_function()
def A133613(i):
    """Last digits of the graham number."""
    x = 3
    for t in range(1, i + 2):
        x = pow(3, x, pow(10, t))
        z = x // pow(10, int(t - 1))
    return z


@oeis.from_generator(offset=1)
def A183613() -> Iterable[int]:
    """Backward concatenation of A133613.

    a(n) = 3^^(n+1) modulo 10^n.
    """
    concatenation = 0
    for i in iter(A133613):
        concatenation = concatenation * 10 + i
        yield int(str(concatenation)[::-1])


@oeis.from_function()
def A070939(i: int = 0) -> int:
    """Length of binary representation of n."""
    return len(f"{i:b}")


@oeis.from_function(offset=1)
def A001223(n: int) -> int:
    """Gaps between primes."""
    return A000040[n + 1] - A000040[n]


@oeis.from_generator(offset=1)
def A002182() -> Iterable[int]:
    """Highly composite numbers.

    numbers n where d(n), the number of divisors of n (A000005), increases to a record.
    """
    record = 0
    from sympy import divisor_count

    yield 1
    for n in count(2, 2):
        divisors = divisor_count(n)
        if divisors > record:
            record = divisors
            yield n


@oeis.from_generator(offset=0)
def A065722() -> Iterable[int]:
    """Primes that when written in base 4, then reinterpreted in base 10, again give primes."""
    for p in A000040:  # pylint: disable=not-an-iterable
        # Refer: https://github.com/pylint-dev/pylint/issues/9251
        if _is_patterson_prime(p):
            yield p


def _is_patterson_prime(n):
    import numpy as np
    from sympy.ntheory import isprime

    base_four_repr = np.base_repr(n, base=4)
    base_ten_repr = int(base_four_repr)
    return isprime(base_ten_repr)


def main() -> None:  # pylint: disable=too-many-branches
    """Command line entry point."""
    args = parse_args()

    if args.list:
        oeis.print_list()
        return

    if args.random:
        args.sequence = choice(list(oeis.series.keys()))

    if not args.sequence:
        print(
            "No sequence given, please see oeis --help, or try oeis --random",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.sequence not in oeis.series:
        print("Unimplemented serie", file=sys.stderr)
        sys.exit(1)

    sequence = oeis.series[args.sequence]
    if args.start is None:
        args.start = sequence.offset

    if args.start < sequence.offset:
        print(f"{args.sequence} starts at offset {sequence.offset}", file=sys.stderr)
        sys.exit(1)

    serie = sequence[args.start : args.stop]

    if args.plot:  # pragma: no cover
        import matplotlib.pyplot as plt

        plt.scatter(list(range(len(serie))), serie)
        plt.show()
    elif args.dark_plot:  # pragma: no cover
        import matplotlib.pyplot as plt

        colors = []
        for _i in range(len(serie)):
            colors.append(random())
        with plt.style.context("dark_background"):
            plt.scatter(list(range(len(serie))), serie, s=50, c=colors, alpha=0.5)
        plt.show()
    else:
        print("#", args.sequence, end="\n\n")
        print(oeis.series[args.sequence].__doc__, end="\n\n")
        print(*serie, sep=", ")

    if args.file:
        import matplotlib.pyplot as plt

        plt.scatter(list(range(len(serie))), serie)
        plt.savefig(args.file)
        print(f"Graph printed in {args.file}")


if __name__ == "__main__":
    main()
