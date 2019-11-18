"""
Tool that return a given sequence
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
import math

__version__ = "0.0.1"


def parse_args():
    parser = argparse.ArgumentParser(description="Print a sweet sequence")
    parser.add_argument(
        "sequence",
        metavar="S",
        type=str,
        help="Define the sequence to run (e.g.: A181391)",
    )
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


def A181391(start=0, limit=20, plot=False):
    sequence = [0]
    last_pos = {}

    for i in range(start + limit):
        new_value = i - last_pos.get(sequence[i], i)
        sequence.append(new_value)
        last_pos[sequence[i]] = i

    if plot:
        colors = []
        for i in range(start, start + limit):
            colors.append(np.random.rand())

        plt.scatter(
            range(start, start + limit),
            sequence[start : start + limit],
            s=50,
            c=colors,
            alpha=0.5,
        )
        plt.show()

    return sequence[start : start + limit]


def A000142(start=0, limit=20, plot=False):
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(math.factorial(i))
        x.append(i)

    if plot:
        plt.plot(x, sequence)
        plt.show()

    return sequence


def A000290(start=0, limit=20, plot=False):
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(i * i)
        x.append(i)

    if plot:
        plt.plot(x, sequence)
        plt.show()

    return sequence


def A000079(start=0, limit=20, plot=False):
    sequence = []
    for i in range(start, start + limit):
        sequence.append(2 ** i)

    if plot:
        plt.plot(sequence)
        plt.show()

    return sequence


def A000045(start=0, limit=20, plot=False):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    for i in range(2, limit):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    if plot:
        plt.plot(sequence)
        plt.show()

    return sequence


def A115020():
    result = []
    for n in range(100, 0, -7):
        if n >= 0:
            result.append(n)

    return result


def A000040(start, end, plot=False):
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
    if plot:
        plt.plot(resultIndex, result)
        plt.ylabel("some numbers")
        plt.show()

    return result


def A000010(n):
    numbers = []
    i = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)


def A000040(start=0, end=999, plot=False):
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
    if plot:
        plt.plot(resultIndex, result)
        plt.ylabel("some numbers")
        plt.show()
    else:
        return result


def partitions(n):

    if n == 0:
        return []
    if n == 1:
        return [[1]]

    partition = [[n]]

    for i in range(1, n):
        for p in partitions(n - i):
            if [i] + p == sorted([i] + p):
                partition.append([i] + p)

    return partition


def A000041(n):
    return len(partitions(n))


def main():

    args = parse_args()

    if args.sequence == "A181391":
        return A181391(args.start, args.limit, args.plot)
    elif args.sequence == "A000142":
        return A000142(args.start, args.limit, args.plot)
    elif args.sequence == "A000290":
        return A000290(args.start, args.limit, args.plot)
    elif args.sequence == "A000079":
        return A000079(args.start, args.limit, args.plot)
    elif args.sequence == "A000045":
        return A000045(args.start, args.limit, args.plot)
    elif args.sequence == "A115020":
        return A115020()[args.start : args.start + args.limit]
    elif args.sequence == "A000040":
        return A000040(args.start, args.limit, args.plot)
    elif args.sequence == "A000010":
        return [A000010(x) for x in range(1, args.limit)]
    elif args.sequence == "A000041":
        return A000041(args.start)


if __name__ == "__main__":
    print(main())
